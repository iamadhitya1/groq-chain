class Step:
    """A single prompt step in a GroqChain."""

    def __init__(self, template: str, output_key: str = "output", **static_vars):
        """
        Args:
            template:    Prompt string with {variable} placeholders.
            output_key:  Key used to pass this step's output to the next step.
            **static_vars: Variables resolved at definition time.
        """
        self.template = template
        self.output_key = output_key
        self.static_vars = static_vars

    def render(self, context: dict) -> str:
        """Render the prompt template with the given context."""
        merged = {**self.static_vars, **context}
        try:
            return self.template.format(**merged)
        except KeyError as e:
            raise ValueError(f"Missing variable {e} in prompt template: {self.template!r}")
