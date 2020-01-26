import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pi-status",
    version="0.0.1",
    author="Sam Poder",
    author_email="23samuel.p@gwa.edu.sg",
    description="An application that allows you to check the status of your Raspberry Pi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sampoder/pi-status",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['psutil >= 5.6.7', 'flask >= 1.1.1']
)