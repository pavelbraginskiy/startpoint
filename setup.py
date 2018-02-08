from setuptools import setup, find_packages

setup(
    name="IsMain",
    version="0.1",
    packages=find_packages(),
    install_requires=['docutils>=0.3'],
    package_data={
        '': ['*.txt', '*.rst'],
    },
    author="pavelbraginskiy",
    author_email="pavelbraginskiy@hotmail.com",
    description="A better entry point than if __name__ == '__main__'",
    license="MIT",
    url="https://github.com/pavelbraginskiy/ismain/tree/master"

)
