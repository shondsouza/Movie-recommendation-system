from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Project configuration
REPO_NAME = "MovieMatch"
AUTHOR_USER_NAME = "ShonDsouza"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['flask', 'requests', 'numpy', 'pandas']


setup(
    name=Movie-recommendation-system,
    version="1.0.0",
    author="Shon Dsouza",
    description="A modern movie recommendation system with machine learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shondsouza/Movie-recommendation-system.git", 
    author_email="shondsouza11@gmail.con", 
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)
