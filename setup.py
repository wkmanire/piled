from setuptools import setup

setup(
    name="Piled",
    version="0.0.1",
    package_dir = {"": "src"},
    packages=["piled", "piled.schema"],
    url="https://github.com/wkmanire/piled",
    license=" LGPL-2.1 License",
    author="wkmanire",
    author_email="williamkmanire@gmail.com",
    description="An experimental compiler that generates python modules from Tiled map editor JSON files."
)
