from setuptools import find_packages, setup

setup(
    name='vultest-fa1zali',
    packages=find_packages(),
    version='0.1.0',
    description='A python module for testing router vulnerability',
    author='Faisal Ali',
    author_email='fzl.ali33@gmail.com',
    url='https://github.com/Fa1sal-ali/vultest',
    license='MIT',
    install_requires=['ipaddress','paramiko','re','time'],
    python_requires='>=3.8'
)