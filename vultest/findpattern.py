# Author: Faisal Ali
# Creation Date: Dec, 05 2020
# Version: 0.1.0
# Revision Date: NA

# Import libraries
from netmiko import ConnectHandler, redispatch
import regex
import ipaddress

def testip(deviceip: str) -> bool:
    """
    Take the ip address as an input and check
    whether its a valid ip or not and return the result.

    :param deviceip: ip address for the device
    :return: boolean stating whether ip is valid or not
    """
        
    try:
        _ = str(ipaddress.ip_address(deviceip))
        ipflag = True
    except ValueError:
        ipflag = False
    finally:
        return ipflag

def testpattern(username: str, password: str, deviceip: str, command: str, pattern: str ) -> dict:

    """
    Login into the router, trigger the provided command,
    find the required pattern provided by the user and 
    return the output.

    :param username: username for accessing router
    :param password: password for accessing router
    :param deviceip: ip address for the device
    :param command: command to be triggered on the device
    :param pattern: pattern to be searched in output of the triggered command
    :return: dictionary containing details and result
    """
    # Defining an empty dictionary for storing the result
    resultdict = dict()

    # Test the IP provided
    iptestresult = testip(deviceip)

    if (iptestresult != True):
        resultdict['IP'] = deviceip
        resultdict['Status'] = 'Not a valid IP'
        return resultdict
    else:
        pass