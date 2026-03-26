from setuptools import setup, find_packages

setup(
    name="web_scraper_project",          # Project name (change this)
    version="0.1.0",
    author="Your Name",
    author_email="your_email@example.com",
    description="A web scraping project using Python and Selenium",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "selenium",
        "pandas"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)