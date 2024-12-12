from setuptools import setup, find_packages

setup(
    name="aider-install",
    version="0.0.5",
    packages=find_packages(),
    description="Installer for the aider CLI tool.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Paul Gauthier",
    author_email="paul@aider.chat",
    url="https://github.com/Aider-AI/aider-install",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "uv",
    ],
    entry_points={
        'console_scripts': [
            'aider-install=aider_install.main:install_aider',
        ],
    },
)
