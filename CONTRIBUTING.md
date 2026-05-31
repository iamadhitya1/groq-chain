# Contributing to groq-chain

PRs welcome. Here's how to get started.

## Setup

```bash
git clone https://github.com/iamadhitya1/groq-chain
cd groq-chain
pip install -e .
pip install groq
```

## Project structure

```
groqchain/
  __init__.py   # exports GroqChain
  chain.py      # main GroqChain class
  step.py       # Step dataclass
```

## What's in scope

- Bug fixes
- New chaining features (parallel steps, conditional steps)
- Support for streaming responses
- Better error messages
- Documentation fixes

## Guidelines

- **One dependency max** (`groq`) — don't add more
- Keep the API flat and readable — `.step().step().run()` style
- No breaking changes to existing `.step()` / `.run()` / `.run_all()` signatures without a major version bump
- Add a usage example in the docstring if adding a new method
- One feature or fix per PR

## Submitting a PR

1. Fork the repo
2. Create a branch: `git checkout -b feat/your-feature-name`
3. Make your change
4. Open a PR against `main` with a clear title and description of what changed and why

Set `GROQ_API_KEY` in your environment to test against the real API.

---

MIT © 2025 M Adhitya · [Rewrite Labs](https://rewritelabs.vercel.app)
