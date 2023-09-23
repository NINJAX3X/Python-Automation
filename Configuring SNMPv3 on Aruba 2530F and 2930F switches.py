import netmiko
from netmiko import ConnectHandler
import sys

#Inorder to run this script you need to configure few things first through console.

aruba_osswitch = {
                    "device_type": "aruba_osswitch",
                    "ip": "10.15.40.14", #Enter the Management IP address of the switch, through this it will take SSH.
                    "username": "username", #Enter the local or TACACS/RADIUS username and password.
                    "password": "password",
                    "global_delay_factor" : 2, #This will keep a delay of 2 seconds for every command it will send it to the switch.
                                                        }

net_connect = ConnectHandler(**aruba_osswitch) #Taking SSH of the switch

#In the Aruba switches there are multiple prompts that are asked after enabling snmpv3.
#So accordingly I have set the commands to send it to the switch.
#This set of commands will create an snmpv3 user 'initial' with password 'initial'.
#You can change this later

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
