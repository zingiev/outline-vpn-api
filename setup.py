# -*-coding:utf-8-*-

from setuptools import setup

setup(
    name="outline-vpn-api",
    version="1.0.0",
    packages=[
        ".",
    ],
    url="https://github.com/jadolg/outline-vpn-api/",
    license="MIT",
    author="Jorge Alberto Díaz Orozco (Akiel)",
    author_email="diazorozcoj@gmail.com",
    description="Python API wrapper for Outline VPN",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    install_requires=("requests",),
)
