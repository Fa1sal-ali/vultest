from setuptools import find_packages, setup

setup(
    name='vultest',
    packages=find_packages(include=['vultest']),
    version='0.1.2',
    description='Vultest is a python library for testing router vulnerability.',
    author='Faisal Ali',
    author_email='fzl.ali33@gmail.com',
    url='https://github.com/Fa1sal-ali/vultest',
    license='MIT',
    install_requires=['ipaddress==1.0.23','paramiko==2.6.0'],
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    platforms="Linux; MacOS X; Windows",
    python_requires='>=3.8'
)