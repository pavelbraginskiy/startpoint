from setuptools import setup, find_packages

setup(
    name="startpoint",
    version="1.1",
    packages=["startpoint"],
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
