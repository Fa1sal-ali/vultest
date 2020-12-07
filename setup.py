from setuptools import find_packages, setup

setup(
    name='vultest',
    packages=find_packages(),
    version='0.1.0',
    description='A python module for testing router vulnerability',
    author='Faisal Ali',
    license='MIT',
    install_requires=['ipaddress','paramiko','re','time'],
)