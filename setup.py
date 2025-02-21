from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="liara-python-sdk",
    version="0.1.0",
    author="shabane",
    author_email="m.mohamadshabane@gmail.com",
    description="A Python SDK for interacting with the Liara platform.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shabane/liaraPythonSDK",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    keywords=["liara", "sdk", "cloud", "platform"],
)