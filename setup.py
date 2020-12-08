from setuptools import find_packages, setup

setup(
    name='vultest',
    packages=find_packages(include=['vultest']),
    version='0.1.0',
    description='Vultest is a python library for testing router vulnerability.',
    author='Faisal Ali',
    author_email='fzl.ali33@gmail.com',
    url='https://github.com/Fa1sal-ali/vultest',
    platform='any',
    license='MIT',
    install_requires=['ipaddress','paramiko'],
    python_requires='>=3.8'
)