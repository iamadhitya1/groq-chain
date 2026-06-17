from setuptools import setup, find_packages

setup(
    name="groq-chain",
    version="1.0.1",
    author="M. Adhitya",
    author_email="adhitya5119@gmail.com",
    description="Dead-simple Groq LLM chaining in Python. Chain prompts with .step() — no LangChain needed.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/iamadhitya1/groq-chain",
    project_urls={
        "Homepage": "https://iamadhitya.vercel.app",
        "Source": "https://github.com/iamadhitya1/groq-chain",
        "Rewrite Labs": "https://rewritelabs.vercel.app",
    },
    packages=find_packages(),
    install_requires=["groq>=0.4.0"],
    python_requires=">=3.9",
    license="MIT",
    keywords=["groq", "llm", "chain", "ai", "nlp", "prompt-chaining",
              "groq-api", "llama", "langchain-alternative", "llm-pipeline",
              "ai-pipeline", "python-ai", "groq-python"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
