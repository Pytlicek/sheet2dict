import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sheet2dict",
    version="0.0.9",
    author="Tomas Pytel",
    author_email="pytlicek@gmail.com",
    description="Simple XLSX and CSV to dictionary converter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pytlicek/sheet2dict",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["openpyxl"],
    python_requires=">=3.6",
)
