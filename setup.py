from setuptools import setup, find_packages

setup(
    name="phishing-detection-system",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.104.1",
        "uvicorn>=0.24.0",
        "scikit-learn>=1.3.2",
        "numpy>=1.24.3",
        "pandas>=2.0.3",
        "requests>=2.31.0",
        "beautifulsoup4>=4.12.2",
        "nltk>=3.8.1",
        "textblob>=0.17.1",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="Machine learning-based phishing detection system",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/phishing-detection-system",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)