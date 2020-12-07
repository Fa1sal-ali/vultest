# Author: Faisal Ali
# Creation Date: Dec, 05 2020
# Version: 0.1.0
# Revision Date: NA

# Import libraries
import ipaddress
import paramiko as pmk
import regex
import time

def test_ip(deviceip: str) -> bool:
    
    """
    Take the ip address as an input and check
    whether its a valid ip or not and return the result.

    :param deviceip: ip address for the device
    :return: boolean stating whether ip is valid or not
    """
    try:
        _ = str(ipaddress.ip_address(deviceip))
        ipflag = True # Set flag to True since it is valid
    except ValueError:
        ipflag = False # Set flag to False since it is invalid
    finally:
        return ipflag

def send_command(username: str, password: str, deviceip: str, command: str):
    
    """
    Use provided Credentials & Device IP to login 
    into the device, trigger the provided Command,
    and return the output.

    :param username: username for accessing device
    :param password: password for accessing device
    :param deviceip: ip address for the device
    :param command: command to be triggered on the device
    :return: dictionary containing the result
    """

    # Defining an empty dictionary for storing the result
    resultdict = dict()
    cmd_output = ""
    try:
        ssh_pre = pmk.SSHClient()
        ssh_pre.set_missing_host_key_policy(pmk.AutoAddPolicy())
        ssh_pre.connect(hostname=deviceip, username=username, password=password, port=22, timeout=10, look_for_keys=False, allow_agent=False) # Connecting to device
        ssh = ssh_pre.invoke_shell() # Invoking sheel
        ssh.send("terminal length 0\n") # Removing the paging of output
        ssh.send("\n")
        time.sleep(1)
        ssh.send(command + "\n") # Triggering the command
        time.sleep(10)
        outputa = ssh.recv(999999) # Recieving the output
        ssh.close() # Closing the session
        outputb = outputa.decode('utf-8') # Encoding the output
        cmd_output = outputb.split("\n",5)[5] # Removing lines that are not required
        resultdict['cmd_output'] = cmd_output
        resultdict['cmdflag'] = True
        resultdict['Status'] = 'Output Recieved'
    
    except pmk.ssh_exception.AuthenticationException:
        resultdict['cmd_output'] = cmd_output
        resultdict['cmdflag'] = False
        resultdict['Status'] = 'Authentication Failed'

    except Exception as error:
        resultdict['cmd_output'] = cmd_output
        resultdict['cmdflag'] = False
        resultdict['Status'] = error

    finally:
        return resultdict

def test_pattern(username: str, password: str, deviceip: str, command: str, pattern: str ) -> dict:

    """
    Login into the device, trigger the provided command,
    find the required pattern provided by the user and 
    return the output.

    :param username: username for accessing device
    :param password: password for accessing device
    :param deviceip: ip address for the device
    :param command: command to be triggered on the device
    :param pattern: pattern to be searched in output of the triggered command
    :return: dictionary containing the result
    """
    # Defining an empty dictionary for storing the result
    result = dict()
    command_result = dict()

    # Test the IP provided
    iptestresult = test_ip(deviceip)

    if (iptestresult != True):
        result['IP'] = deviceip
        result['Status'] = 'Not a valid IP'
        return result
    else:
        # Get the output of the command from the device
        command_result = send_command(username, password, deviceip, command)
        if command_result['cmdflag'] != True:
            return command_result
        else:
            cmd_output = command_result['cmd_output']
        