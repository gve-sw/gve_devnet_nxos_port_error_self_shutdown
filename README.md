# gve_devnet_nxos_port_error_self_shutdown
Check the ports of a Nexus switch to ensure input error is less than a predefined threshold, otherwise the port is shutdown. 
This Python script will take the list of Nexus devices in the inventory file, based on IP addresses, and check every interface for input errors. It will continue to check based on a polling wait period indefinitely. When the error of a specific port is above a custom threshold, the port will be disabled.

## Contacts
* Kevin Chen (kevchen3@cisco.com)

## Solution Components
* Nexus 9000 Switch

## Related Sandbox Environment

This sample code can be tested using a Cisco dCloud demo instance that contains ** Nexus Switches **

To use the code in this repository, the Nexus switches must be configured for NX API. To enable NX API on the switch, use 

```
conf t
feature nxapi
```

![/IMAGES/NXAPI.png](/IMAGES/NXAPI.png)



## Installation/Configuration

1. Clone this repository with `git clone [repository link]`
 
2. add the required information in the .env file and inventory.csv file

```python
# Add any settings in environemnt file.  Below is an example:
# Nexus Switch IP address and Username and Password
# Authorization header is generated from the username and password with basic auth Base64 

SWITCHIPLIST = inventory.csv
USERNAME = admin
PASSWORD = password

```

inventory.csv is a file listing all the IP addresses of the switches to be checked by this script. 

```
192.168.1.1
192.168.2.1
192.168.3.1
```

3. Set up a Python virtual environment. Make sure Python 3 is installed in your environment, and if not, you may download Python [here](https://www.python.org/downloads/). Once Python 3 is installed in your environment, you can activate the virtual environment with the instructions found [here](https://docs.python.org/3/tutorial/venv.html).

4. Install the requirements with `pip3 install -r requirements.txt`



## Usage


To launch the script:


    $ python main.py

This will start the script to run indefinitely. The timer can be set to customise the information collection period in main.py. 

# Screenshots

![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
