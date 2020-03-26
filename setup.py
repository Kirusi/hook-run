from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="hook-run",
    version="1.0.0",
    author="Kirusi Msafiri",
    author_email="kirusi.msafiri@gmail.com",
    description="Run commands using Python virtual environment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kirusi/hook-run",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development",
        "Topic :: Utilities",
    ],
    package_dir={"": "src"},
    py_modules=["hookrun"],
    python_requires="~=3.7",
    entry_points={"console_scripts": ["hook-run = hookrun:run",]},
)
