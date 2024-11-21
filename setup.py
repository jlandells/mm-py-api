from setuptools import setup, find_packages

setup(
    name="mattermost_api",  # Name of your library
    version="1.0.0",  # Initial version
    packages=find_packages(),  # Automatically find the package(s)
    install_requires=["requests"],  # Dependencies
    description="A simple library for making Mattermost API calls",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mattermost_api",  # Replace with your GitHub repo URL
    author="Your Name",
    author_email="your.email@example.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version
)