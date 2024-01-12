import os
import csv
import time
from NXapi import *
from urllib3.exceptions import InsecureRequestWarning

# Disable warnings for testing purposes
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

switchIpList = os.environ.get("SWITCHIPLIST")
username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")

threshold = 0  # error threshold for the port input error
timer = 300  # waiting period in seconds between each poll

with open(switchIpList) as file:
    switchIpList = list(csv.reader(file, delimiter=","))

while True:

    for switch in switchIpList:
        switchIp = switch[0]
        baseUrl = "https://"+switchIp+":443"

        try:
            session = startSession(baseUrl, username, password)
        except:
            print(f"Cannot connect to switch {switchIp}")
            continue

        intList = getInterfaces(baseUrl, session)

        for interface in intList:
            # looping through all the interfaces on the device
            try:
                # get the interface type, management interfaces are skipped
                interfaceType = interface["type"]
                temp, interfaceNumber = mysplit(interface["interface"])
            except:
                print("interface type not supported, skipping ",
                      interface["interface"])
                continue

            errorNo = getIntErrors(
                interfaceType, interfaceNumber, session, baseUrl)
            if int(errorNo) >= threshold:
                intShutDown(interfaceType, interfaceNumber, session, baseUrl)
                print(
                    f"Port {interface['interface']} has {errorNo} errors, shutting down. ")

    time.sleep(timer)
