# VULTEST (Vulnerability Tester)
Vultest is a python library for testing router vulnerability.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install vultest.

The source code is currently hosted on GitHub at: https://github.com/Fa1sal-ali/vultest

Binary installers for the latest released version are available at the [Python Package Index - PyPi](https://pypi.org/project/vultest/)

```bash
pip install vultest
```
## Usage

```python
from vultest import vultest

vultest.test_ip(deviceip = '') # returns if ip is valid or not
vultest.test_ping(deviceip = '') # returns if ip is reachable or not
vultest.device_login(username = '', password = '', deviceip = '') # returns a channel for communicating with device and a dictionary with result
vultest.send_command(username = '', password = '', deviceip = '', command = '') # returns the output of the command triggered on the device
vultest.test_pattern(username = '', password = '', deviceip = '', command = '', pattern = '') # returns whether the pattern present in the output of the command or not
```

## Dependencies

[ipaddress](https://github.com/phihag/ipaddress)

[paramiko](https://github.com/paramiko/paramiko)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://github.com/Fa1sal-ali/vultest/blob/main/LICENSE)