from setuptools import setup, find_packages

setup(
    name="groq-chain",
    version="1.0.0",
    author="M Adhitya",
    description="Dead-simple Groq LLM chaining. No bloat.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/iamadhitya1/groq-chain",
    packages=find_packages(),
    install_requires=["groq>=0.4.0"],
    python_requires=">=3.9",
    license="MIT",
    keywords=["groq", "llm", "chain", "ai", "nlp"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
