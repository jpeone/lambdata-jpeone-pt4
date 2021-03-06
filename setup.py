# setup.py file
from setuptools import find_packages, setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="lambdata-jpeone-pt4",
    version="1.3.18.01",
    author="Felix Peone",
    author_email="topsecret@gmail.com",
    description="For example purposes",
    long_description=long_description,
    long_description_content_type="text/markdown",  # required if using md file
    # license="MIT",
    url="https://github.com/jpeone/lambdata-jpeone-pt4",
    # keywords="",
    packages=find_packages(),
    install_requires=[
        'pandas',
        'scikit-learn'
    ]
)
