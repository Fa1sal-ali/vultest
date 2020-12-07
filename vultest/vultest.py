# Author: Faisal Ali
# Creation Date: Dec, 05 2020
# Version: 0.1.0
# Revision Date: NA

# Import libraries
import ipaddress
import paramiko as pmk
import re
import time

def test_ip(deviceip: str) -> bool:
    
    """
    Take the ip address as an input and check
    whether its a valid ip or not and return the result.

    :param deviceip: ip address for the device
    :return: boolean stating whether ip is valid or not
    """

    # Defining an empty dictionary to store the result
    resultdict = dict()

    resultdict['deviceip'] = deviceip
    try:
        _ = str(ipaddress.ip_address(deviceip))
        resultdict['ipflag'] = True # Set flag to True since it is valid
        resultdict['Status'] = 'Valid IP'
    except ValueError:
        resultdict['ipflag'] = False # Set flag to False since it is invalid
        resultdict['Status'] = 'Not a Valid IP'
    finally:
        return resultdict

def device_login(username: str, password: str, deviceip: str) -> object and dict:

    """
    Use provided Credentials & Device IP to login 
    into the device and return the SSH channel along with result.

    :param username: username for accessing device
    :param password: password for accessing device
    :param deviceip: ip address for the device
    :return: SSH channel and dictionary containing the result
    """

    # Defining an empty channel variable and dictionary for storing the result
    ssh = None
    resultdict = dict()

    # Test the IP provided
    iptestresult = test_ip(deviceip)
    
    if (iptestresult['ipflag'] != True):
        return ssh, iptestresult
    else:
        resultdict['deviceip'] = deviceip
        try:
            ssh_pre = pmk.SSHClient()
            ssh_pre.set_missing_host_key_policy(pmk.AutoAddPolicy())
            ssh_pre.connect(hostname=deviceip, username=username, password=password, port=22, timeout=10, look_for_keys=False, allow_agent=False) # Connecting to device
            ssh = ssh_pre.invoke_shell() # Invoking shell
            resultdict['loginflag'] = True
            resultdict['Status'] = 'Login Success'
        
        except pmk.ssh_exception.AuthenticationException: # If credentials do not work
            resultdict['loginflag'] = False
            resultdict['Status'] = 'Authentication Failed'

        except pmk.ssh_exception.NoValidConnectionsError: # If unable to connect to device
            resultdict['loginflag'] = False
            resultdict['Status'] = 'Unable to connect'

        except Exception as error: # For any unknown exception
            resultdict['loginflag'] = False
            resultdict['Status'] = error

    return ssh, resultdict

def send_command(username: str, password: str, deviceip: str, command: str) -> dict:
    
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

    if command != '':
        # Logging the device and returning the channel
        ssh, login_result = device_login(username, password, deviceip)

        if ('loginflag' in login_result and login_result['loginflag'] != True) or ('ipflag' in login_result and login_result['ipflag'] != True):
            return login_result
        else:
            resultdict['deviceip'] = deviceip
            resultdict['command'] = command
            ssh.send("terminal length 0\n") # Show the ouput without any breaks or pauses (CISCO Specific)
            ssh.send("\n")
            time.sleep(1)
            ssh.send(command + "\n") # Triggering the command
            time.sleep(10)
            outputa = ssh.recv(999999) # Recieving the output
            ssh.close() # Closing the session
            outputb = outputa.decode('utf-8') # Decoding the output
            cmd_output = outputb.split("\n",5)[5] # Removing lines that are not required
            resultdict['cmd_output'] = cmd_output
            resultdict['cmdflag'] = True
    else:
        resultdict['cmdflag'] = False
        resultdict['Status'] = 'Command Field Empty'
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

    if pattern != '':
        # Get the output of the command from the device
        command_result = send_command(username, password, deviceip, command)
    
        if ('loginflag' in command_result and command_result['loginflag'] != True) or ('cmdflag' in command_result and command_result['cmdflag'] != True) or ('ipflag' in command_result and command_result['ipflag'] != True):
            return command_result
        else:
            cmd_output = command_result['cmd_output']
            patternsearch = re.search(pattern, cmd_output) # Searching the pattern in output of the command
            result['deviceip'] = deviceip
            result['Command'] = command 
            result['Pattern'] = pattern
            if patternsearch == None:
                result['Status'] = 'Missing'
            else:
                result['Status'] = 'Present'
    else:
        result['patternflag'] = False
        result['Status'] = 'Empty Pattern Field'
    return result