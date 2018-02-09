import sys

from setuptools import setup, find_packages
reqs = ['docutils>=0.3']

if sys.version_info < (3,2):
    reqs += ["funcsigs>=1.0.2"]

setup(
    name="startpoint",
    version="1.3.1",
    packages=["startpoint"],
    install_requires=reqs,
    package_data={
        '': ['*.md'],
    },
    author="Pavel Braginskiy",
    author_email="pavelbraginskiy@hotmail.com",
    description="A better entry point than if __name__ == '__main__'",
    license="MIT",
    url="https://github.com/pavelbraginskiy/ismain/tree/master"
   
)
