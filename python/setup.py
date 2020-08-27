from setuptools import setup

PACKAGE_NAME = "mypy-protobuf"
PACKAGE_VERSION = "1.23.0"


setup(
    name="mypy-protobuf",
    version=f"{PACKAGE_VERSION}+grpc.wix",
    description="Generate mypy stub files from protobuf specs",
    keywords="mypy proto dropbox",
    license="Apache License 2.0",
    author="Nipunn Koorapati",
    author_email="nipunn@dropbox.com",
    py_modules=["mypy_protobuf"],
    url="https://github.com/dropbox/mypy-protobuf",
    download_url="https://github.com/dropbox/mypy-protobuf/archive/v1.23.tar.gz",
    install_requires=["protobuf>=3.6.0"],
    entry_points={
        "console_scripts": [
            "protoc-gen-mypy = mypy_protobuf:main",
            "protoc-gen-mypy_grpc = mypy_protobuf:grpc",
        ],
    },
    scripts=["protoc_gen_mypy.bat"],
)
