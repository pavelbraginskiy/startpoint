from setuptools import setup
setup(
    name="ismain",
    version="0.1",
    packages=["ismain"],
    install_requires=['docutils>=0.3'],
    package_data={
        '': ['*.md'],
    },
    author="Pavel Braginskiy",
    author_email="pavelbraginskiy@hotmail.com",
    description="A better entry point than if __name__ == '__main__'",
    license="MIT",
    url="https://github.com/pavelbraginskiy/ismain/tree/master"
   
)
