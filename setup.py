"""Add support for SoftLayer uploads
"""

from os import path
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md')) as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="backwork-upload-cos",
    version="0.3.0",
    description="Backwork plug-in for IBM Cloud Object Storage uploads.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/IBM/backwork-upload-cos",
    author="Michael Lin",
    author_email="michael.lin1@ibm.com",
    license="Apache 2",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: POSIX :: Linux",
        'License :: OSI Approved :: Apache Software License',
        "Topic :: Database",
        "Topic :: System :: Archiving :: Backup",
        "Topic :: Utilities"
    ],
    packages=find_packages(),
    install_requires=[
        "backwork",
        "ibm-cos-sdk>=2.4.4"
    ],
    entry_points={
        "backwork.uploads": [
            "cos=cos:CloudObjectStorageUpload"
        ],
        "backwork.shows": [
            "cos=cos:CloudObjectStorageShow"
        ],
        "backwork.downloads": [
            "cos=cos:CloudObjectStorageDownload"
        ]
    }
)
