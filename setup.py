from setuptools import setup, find_packages

setup(
    name='scraperweapon',
    version='1.0.0',
    description='A revolutionary web scraping library',
    author='SumedhP',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'playwright',
    ],
    python_requires='>=3.7',
)
