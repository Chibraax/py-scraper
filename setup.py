from setuptools import setup, find_packages
import py_scraper
 

setup(
    name='py_scraper',
    version=py_scraper.__version__,
    packages=find_packages(),
    author="Chibraax",
    author_email="?",
    description="Proxy scraper using requests and bs4.\n Scrap HTTP/HTTPS/SOCKS proxy.\n Each proxy is stored with his country.",
    long_description=open('README.md').read(),
    install_requires= ["requests","bs4"]
    url='https://github.com/Chibraax/',
)
