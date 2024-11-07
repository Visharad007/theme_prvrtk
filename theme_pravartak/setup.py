from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

setup(
    name="theme_pravartak",  # Replace with your app's name
    version="0.0.1",
    description="theme for ERPNext",
    author="Visharad",
    author_email="vish@gmail.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
