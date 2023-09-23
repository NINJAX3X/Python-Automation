import netmiko
from netmiko import ConnectHandler
import sys
import time

aruba_osswitch = {
                    "device_type": "aruba_osswitch",
                    "ip": "10.15.40.14",
                    "username": "username",
                    "password": "password",
                    "global_delay_factor" : 2,
                                                        }

net_connect = ConnectHandler(**aruba_osswitch)


commands = [
            'configure terminal',
            'snmpv3 enable',
            'initial',
            'initial',
            'n',
            'y',
                                                            ]

output = net_connect.send_multiline_timing(commands, multiline = True)

print(output)

print("\n""Done")

net_connect.disconnect()
