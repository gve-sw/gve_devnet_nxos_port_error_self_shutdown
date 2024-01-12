import requests
import json
import re
import os
from requests.auth import HTTPBasicAuth
import pybase64


def mysplit(s):
    index = re.search(r"\d", s)
    intType = s[:index.start()]
    intNumber = s[index.start():]
    return intType, intNumber


def BasicGen():
    username = os.environ.get("USERNAME")
    password = os.environ.get("PASSWORD")
    basicAuth = "Basic " + pybase64.standard_b64encode(
        bytes(username + ":" + password, 'utf-8')).decode('utf-8')

    return basicAuth


def getIntErrors(interfaceType, interfaceNumber, session, baseUrl):
    # Get interface input errors

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': BasicGen()

    }

    url = baseUrl + \
        "/api/mo/sys/intf/phys-["+interfaceType + \
        interfaceNumber+"]/dbgIfIn.json"

    response = session.get(url, headers=headers)
    response = json.loads(response.text)
    try:
        return response["imdata"][0]["rmonIfIn"]["attributes"]["errors"]
    except:
        print("port does not have data.")
        return 0


def intShutDown(interfaceType, interfaceNumber, session, baseUrl):
    # Shut down the interface

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': BasicGen()
    }
    url = baseUrl + "/api/mo/sys/intf.json"

    payload = json.dumps(
        {
            "interfaceEntity": {
                "children": [
                    {
                        "l1PhysIf": {
                            "attributes": {
                                "id": interfaceType+interfaceNumber,
                                "adminSt": "down",
                                "userCfgdFlags": "admin_layer"
                            }
                        }
                    }
                ]
            }
        }
    )

    response = session.post(url, headers=headers, data=payload)


def startSession(baseUrl, username, password):
    # Authentication with the switch
    url = baseUrl + "/api/aaaLogin.json"

    session = requests.Session()

    payload = json.dumps({
        "aaaUser": {
            "attributes": {
                "name": username,
                "pwd": password
            }
        }
    })
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'

    }
    session.post(url, headers=headers, data=payload,
                 verify=False, auth=(username, password))
    return session


def getInterfaces(baseUrl, session):
    url = baseUrl + "/ins"

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': BasicGen()

    }
    payload = json.dumps({
        "ins_api": {
            "version": "1.0",
            "type": "cli_show",
            "chunk": "0",
            "sid": "1",
            "input": "show interface brief",
            "output_format": "json"
        }
    })

    response = session.post(url, headers=headers, data=payload)
    intList = json.loads(response.text)[
        "ins_api"]["outputs"]["output"]["body"]["TABLE_interface"]["ROW_interface"]

    return intList
