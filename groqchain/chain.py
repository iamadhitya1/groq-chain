import os
from typing import Optional
from .step import Step

try:
    from groq import Groq
except ImportError:
    raise ImportError("groq package required. Install with: pip install groq")


class GroqChain:
    """
    Dead-simple Groq LLM chain. No bloat. No abstractions.

    Usage:
        chain = GroqChain(api_key="gsk_...")

        # Single call
        result = chain.run("Summarize this: {text}", text="...")

        # Multi-step chain
        result = (
            GroqChain(api_key="gsk_...")
            .step("Extract 3 key points from: {text}", output_key="points", text="...")
            .step("Write a tweet based on these points: {points}")
            .run()
        )
    """

    DEFAULT_MODEL = "llama-3.3-70b-versatile"

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = DEFAULT_MODEL,
        temperature: float = 0.7,
        max_tokens: int = 1024,
        system: Optional[str] = None,
    ):
        """
        Args:
            api_key:      Groq API key. Falls back to GROQ_API_KEY env var.
            model:        Groq model ID (default: llama-3.3-70b-versatile).
            temperature:  Sampling temperature (default: 0.7).
            max_tokens:   Max output tokens per call (default: 1024).
            system:       Optional system prompt applied to all steps.
        """
        self._api_key = api_key or os.environ.get("GROQ_API_KEY")
        if not self._api_key:
            raise ValueError(
                "Groq API key required. Pass api_key= or set GROQ_API_KEY env var."
            )
        self._client = Groq(api_key=self._api_key)
        self._model = model
        self._temperature = temperature
        self._max_tokens = max_tokens
        self._system = system
        self._steps: list[Step] = []
        self._context: dict = {}

    # ── Builder API ────────────────────────────────────────────────────────────

    def step(self, template: str, output_key: str = "output", **vars) -> "GroqChain":
        """Add a prompt step to the chain."""
        self._steps.append(Step(template, output_key, **vars))
        return self

    def context(self, **vars) -> "GroqChain":
        """Inject variables into the chain context."""
        self._context.update(vars)
        return self

    # ── Execution ──────────────────────────────────────────────────────────────

    def run(self, prompt: Optional[str] = None, **vars) -> str:
        """
        Execute the chain. If a prompt string is given, runs a single call.
        Returns the final output as a string.
        """
        if prompt:
            # Single-shot shorthand: chain.run("Do X with {text}", text="...")
            merged = {**self._context, **vars}
            rendered = Step(prompt).render(merged)
            return self._call(rendered)

        if not self._steps:
            raise ValueError("No steps defined. Use .step() or pass a prompt to .run().")

        ctx = {**self._context, **vars}
        last_output = ""

        for i, s in enumerate(self._steps):
            rendered = s.render(ctx)
            output = self._call(rendered)
            ctx[s.output_key] = output
            last_output = output

        return last_output

    def run_all(self, **vars) -> dict:
        """Run the chain and return all step outputs as a dict."""
        ctx = {**self._context, **vars}
        results = {}

        for s in self._steps:
            rendered = s.render(ctx)
            output = self._call(rendered)
            ctx[s.output_key] = output
            results[s.output_key] = output

        return results

    # ── Internal ───────────────────────────────────────────────────────────────

    def _call(self, prompt: str) -> str:
        messages = []
        if self._system:
            messages.append({"role": "system", "content": self._system})
        messages.append({"role": "user", "content": prompt})

        response = self._client.chat.completions.create(
            model=self._model,
            messages=messages,
            temperature=self._temperature,
            max_tokens=self._max_tokens,
        )
        return response.choices[0].message.content.strip()

    # ── Reset ──────────────────────────────────────────────────────────────────

    def reset(self) -> "GroqChain":
        """Clear all steps and context."""
        self._steps.clear()
        self._context.clear()
        return self
