import setuptools
import pistatus

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pistatus",
    version="1.0.0.1",
    author="Sam Poder",
    author_email="23samuel.p@gwa.edu.sg",
    description=
    "An application that allows you to check the status of your Raspberry Pi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={'console_scripts': ['pistatus=pistatus.__main__:main']},
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.6',
    install_requires=[
          'psutil',

      ],
    )
