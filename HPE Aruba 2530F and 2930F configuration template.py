from netmiko import ConnectHandler
import sys
import time

print("\n")

print("-----------------------This script is only valid for Aruba OS Switches only-------------------------")
print("--------------------------Kindly follow the script instructions as it is----------------------------")

time.sleep(2)

print("\n")

print("---------------------Before running script configure MGMT vlan, password manager,------------------------")
print("----------------IP address and port 1 which connects to PC as an access port in MGMT vlan----------------")

time.sleep(2)

print("\n")

print("Commands to configure the above is as following: ""\n""1) Configure terminal""\n""2) vlan (MGMT vlan ID)""\n""3) untagged 1""\n""4) ip address (10.15.x.x 255.255.255.128)")

time.sleep(1)

print("\n")

value = input("Have you configured (yes/no)?:  ")

if value == "yes" or value == "y":
    print("Executing Script...")
else:
    print("Exiting...")
    sys.exit()

print("\n")

Host = input("Enter the Hostname of switch:  ")

print("\n")

loc = input("Enter the location of the switch:  ")

print("\n")

while True:

        t_o = input("Enter 3rd octet of IP address:  ")
        if len(str(t_o)) == 2 and 10 <= int(t_o) <= 254:
            a = t_o[0]
            break
    
        elif len(str(t_o)) == 3 and 100 <= int(t_o) <= 254:
            a = t_o[0:2]
            break

        else:
            print("Enter a valid third octet between (1-254) ")

while True:

    f_o = input("Enter 4th octet of IP address:  ")
    if 2 <= int(f_o) <= 126:
        print ("Gateway will be 1")
        x = '.1'
        mgmt = '01'
        break
    elif 128 <= int(f_o) <= 254:
        print ("Gatewy will be 129")
        x = '.129'
        mgmt = '02'
        break
    else:
        print("Define a valid octet between (2-254)")

def_gat = '10.15.'+str(t_o)+str(x)

ip = '{}.{}.{}.{}'.format(10,15,t_o,f_o)

aruba_osswitch = {
    "device_type": "aruba_osswitch",
    "ip": ip,
    "username": "username",
    "password": "Password",     
}

net_connect = ConnectHandler(**aruba_osswitch)

print("\n")

net_connect.send_command(input(">>>>>>>>>>>>>>>>>>>>>>Press_Enter>>>>>>>>>>>>>>>>>>>>>>"))

print("\n")

time.sleep(2)

config_commands1 = ['configure terminal',
                    'hostname '+str(Host),
                    'banner motd / ',
                    #Enter the banner message of the day.
                    '/',
                    'console idle-timeout 1800',
                    'console idle-timeout serial-usb 1800',
                    'dhcp-snooping',
                    'dhcp-snooping authorized-server x.x.x.x',
                    'dhcp-snooping authorized-server x.x.x.x',
                    'dhcp-snooping authorized-server x.x.x.x',
                    'logging x.x.x.x',
                    'timesync ntp',
                    'ntp server x.x.x.x',
                    'ip default-gateway '+str(def_gat),
                    'no telnet-server',
                    'tacacs-server host x.x.x.x key Password',
                    'aaa authentication login privilege-mode',
                    'aaa authentication ssh login tacacs local',
                    'aaa authentication ssh enable tacacs local',
                    'snmp-server contact username location '+str(loc),
                    'snmpv3 group managerpriv user username sec-model ver3',
                    'snmpv3 targetaddress user params all x.x.x.x',
                    'spanning-tree',
                    'spanning-tree 1-8 bpdu-protection',
                    'write memory',
                    'exit',
                    'configure terminal',
                    'spanning-tree 9-24 bpdu-protection',
                    'write memory',
                    'exit',
                    'configure terminal',
                    'spanning-tree 25-48 bpdu-protection',
                    'write memory',
                    'exit'
                                                           ]


while True:
    ports = input("Enter the number of ports (8/24/48) for which you want to configure:  ")
    if ports == '8':
        net_connect.send_config_set(config_commands1[:41])
        untagged = '2-8'
        tagged = '9-10'
        break
    elif ports == '24':
        net_connect.send_config_set(config_commands1[:45])
        untagged = '2-24'
        tagged = '25-28'
        break
    elif ports == '48':
        net_connect.send_config_set(config_commands1)
        untagged = '2-48'
        tagged = '49-52'
        break
    else:
        print("Enter valid number of ports which are mentioned (8/24/48):  ")

net_connect.disconnect()

print("Configuring VLANs...")

print("\n")

time.sleep(3)

b_vlan = "{}{}".format(a,11)

c_vlan = "{}{}".format(a,12)

d_vlan = "{}{}".format(a,21)

e_vlan = "{}{}".format(a,22)

f_vlan = "{}{}".format(a,31)

g_vlan = "{}{}".format(a,32)

h_vlan = "{}{}".format(a,41)

i_vlan = "{}{}".format(a,42)

j_vlan = "{}{}".format(a,51)

k_vlan = "{}{}".format(a,52)

l_vlan = "{}{}".format(a,61)

m_vlan = "{}{}".format(a,62)

n_vlan = "{}{}".format(a,81)

o_vlan = "{}{}".format(a,82)

p_vlan = "{}{}".format(a,91)

q_vlan = "{}{}".format(a,92)

r_vlan = "{}{}".format(a,mgmt)

time.sleep(2)

net_connect = ConnectHandler(**aruba_osswitch)

config_commands2 = ['configure terminal',
                    'vlan '+str(b_vlan),
                    'name DHCP11',
                    'tagged '+str(tagged),
                    'exit',
                    'vlan '+str(c_vlan),
                    'name DHCP12',
                    'untagged '+str(untagged),
                    'tagged '+str(tagged),
                    'exit',
                    'vlan '+str(d_vlan),
                    'name DHCP21',
                    'tagged '+str(tagged),
                    'exit',
                    'vlan '+str(e_vlan),
                    'name DHHCP22',
                    'tagged '+str(tagged),
                    'exit',
                    'vlan '+str(f_vlan),
                    'name DHCP31',
                    'tagged '+str(tagged),
                    'exit',
                    'vlan '+str(g_vlan),
                    'name DHCP32',
                    'tagged '+str(tagged),
                    'exit',
                    'vlan '+str(h_vlan),
                    'name DHCP41',
                    'tagged '+str(tagged),
                    'exit',
                    'vlan '+str(i_vlan),
                    'name DHCP42',
                    'tagged '+str(tagged),
                    'exit',
                    'vlan ' +str(j_vlan),
                    'name PRINTER51',
                    'tagged '+str(tagged),
                    'exit',
                    'vlan '+str(k_vlan),
                    'name PUNCHING52',
                    'tagged '+str(tagged),
                    'exit',
                    'vlan '+str(l_vlan),
                    'name FIX61',
                    'tagged '+str(tagged),
                    'exit',
                    'vlan '+str(m_vlan),
                    'name FIX62',
                    'tagged '+str(tagged),
                    'exit',
                    'vlan '+str(n_vlan),
                    'name RF81',
                    'tagged '+str(tagged),
                    'exit',
                    'vlan '+str(o_vlan),
                    'name RF82',
                    'tagged '+str(tagged),
                    'exit',
                    'vlan '+str(p_vlan),
                    'name CCTV91',
                    'tagged '+str(tagged),
                    'exit',
                    'vlan '+str(q_vlan),
                    'name CCTV92',
                    'tagged '+str(tagged),
                    'exit',
                    'vlan '+str(r_vlan),
                    'name MGMT',
                    'tagged '+str(tagged),
                    'exit'

                                             ]

net_connect.send_config_set(config_commands2)

time.sleep(2)

net_connect.disconnect()

print("Configuring SNMPv3...")

print("\n")

net_connect = ConnectHandler(**aruba_osswitch)

commands = [
            'configure terminal',
            'snmpv3 enable',
            'initial',
            'initial',
            'n',
            'y',
            'snmpv3 only',
            'snmpv3 user username auth md5 auth password priv aes privacy password',
            'no snmpv3 user initial',
            'allow-unsupported-transceiver',
            'y',
            'exit',
                                                            ]

output = net_connect.send_multiline_timing(commands, multiline = True)

print("Configuration has been done...")

net_connect.disconnect()
