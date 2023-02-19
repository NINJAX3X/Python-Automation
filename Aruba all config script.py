from netmiko import ConnectHandler
import sys
import time

print("\n")

print("--------------------------This script is only valid for Aruba OS Switches---------------------------")
print("--------------------------Kindly follow the script instructions as it is----------------------------")

time.sleep(2)
print("\n")

print("---------------------Before running script configure MGMT vlan, password manager,------------------------")
print("----------------IP address and port 1 which connects to PC as an access port in MGMT vlan----------------")

time.sleep(2)
print("\n")

print("Commands to configure the above is as following: ""\n""1) Configure terminal""\n""2) vlan (MGMT vlan ID)""\n""3) untagged 1""\n""4) ip address (x.x.x.x x.x.x.x)")

time.sleep(1)
print("\n")

value = input("Have you configured (yes/no)?:  ")

if value == "yes":
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
        break
    elif 128 <= int(f_o) <= 254:
        print ("Gatewy will be 129")
        x = '.129'
        break
    else:
        print("Define a valid octet between (2-254)")

def_gat = 'x.x.'+str(t_o)+str(x)

ip = '{}.{}.{}.{}'.format(x,x,t_o,f_o)

aruba_osswitch = {
    "device_type": "aruba_osswitch",
    "ip": ip,
    "username": "usernamet",
    "password": "password",     
}

net_connect = ConnectHandler(**aruba_osswitch)

print("\n")

net_connect.send_command(input(">>>>>>>>>>>>>>>>>>>>>>Press_Enter>>>>>>>>>>>>>>>>>>>>>>"))

time.sleep(2)

config_commands1 = ['configure terminal',
                    'hostname '+str(Host),
                    'banner motd / ',
                    banner text should be here with proper syntax
                    '/',
                    'console idle-timeout 1800',
                    'console idle-timeout serial-usb 1800',
                    'dhcp-snooping',
                    'dhcp-snooping authorized-server x.x.x.x',
                    'dhcp-snooping authorized-server x.x.x.x',
                    'dhcp-snooping authorized-server x.x.x.x',
                    'logging syslog server ip',
                    'timesync sntp',
                    'ntp server x.x.x.x',
                    'time timezone 330',
                    'ip default-gateway '+str(def_gat),
                    'no telnet-server',
                    'tacacs-server host x.x.x.x key password',
                    'aaa authentication login privilege-mode',
                    'aaa authentication ssh login tacacs local',
                    'aaa authentication ssh enable tacacs local',
                    'snmp-server contact name location '+str(loc), 
                    'snmpv3 targetaddress xxx params xxx x.x.x.x',
                    'snmpv3 group managerpriv user name sec-model ver3',
                    'snmpv3 targetaddress name params all x.x.x.x',
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
    elif ports == '24':
        net_connect.send_config_set(config_commands1[:45])
        untagged = '2-24'
        tagged = '25-28'
    elif ports == '48':
        net_connect.send_config_set(config_commands1)
        untagged = '2-48'
        tagged = '49-52'
    else:
        print("Enter valid number of ports which are mentioned (8/24/48):  ")

net_connect.disconnect()

time.sleep(3)

b_vlan = "{}{}".format(a,xx)

c_vlan = "{}{}".format(a,xx)

d_vlan = "{}{}".format(a,xx)

e_vlan = "{}{}".format(a,xx)

f_vlan = "{}{}".format(a,xx)

g_vlan = "{}{}".format(a,xx)

h_vlan = "{}{}".format(a,xx)

i_vlan = "{}{}".format(a,xx)

j_vlan = "{}{}".format(a,xx)

k_vlan = "{}{}".format(a,xx)

l_vlan = "{}{}".format(a,xx)

m_vlan = "{}{}".format(a,xx)

n_vlan = "{}{}".format(a,xx)

o_vlan = "{}{}".format(a,xx)

p_vlan = "{}{}".format(a,xx)

q_vlan = "{}{}".format(a,xx)

time.sleep(2)

net_connect = ConnectHandler(**aruba_osswitch)

config_commands2 = ['configure terminal',
                    'vlan '+str(b_vlan),
                    'name DHCPxx',
                    'tagged '+str(tagged),
                    'exit',
                    'vlan '+str(c_vlan),
                    'name DHCPxx',
                    'untagged '+str(untagged),
                    'tagged '+str(tagged),
                    'exit',
                    'vlan '+str(d_vlan),
                    'name DHCPxx',
                    'tagged '+str(tagged),
                    'exit',
                    'vlan '+str(e_vlan),
                    'name DHHCPxx',
                    'tagged '+str(tagged),
                    'exit',
                    'vlan '+str(f_vlan),
                    'name DHCPxx',
                    'tagged '+str(tagged),
                    'exit',
                    'vlan '+str(g_vlan),
                    'name DHCPxx',
                    'tagged '+str(tagged),
                    'exit',
                    'vlan '+str(h_vlan),
                    'name DHCPxx',
                    'tagged '+str(tagged),
                    'exit',
                    'vlan '+str(i_vlan),
                    'name DHCPxx',
                    'tagged '+str(tagged),
                    'exit',
                    'vlan ' +str(j_vlan),
                    'name DHCPxx',
                    'tagged '+str(tagged),
                    'exit',
                    'vlan '+str(k_vlan),
                    'name DHCPxx',
                    'tagged '+str(tagged),
                    'exit',
                    'vlan '+str(l_vlan),
                    'name DHCPxx',
                    'tagged '+str(tagged),
                    'exit',
                    'vlan '+str(m_vlan),
                    'name DHCPxx',
                    'tagged '+str(tagged),
                    'exit',
                    'vlan '+str(n_vlan),
                    'name DHCPxx',
                    'tagged '+str(tagged),
                    'exit',
                    'vlan '+str(o_vlan),
                    'name DHCPxx',
                    'tagged '+str(tagged),
                    'exit',
                    'vlan '+str(p_vlan),
                    'name DHCPxx',
                    'tagged '+str(tagged),
                    'exit',
                    'vlan '+str(q_vlan),
                    'name DHCPxx',
                    'tagged '+str(tagged),
                    'exit',
                    'exit'

                                             ]

net_connect.send_config_set(config_commands2)

time.sleep(2)

net_connect.disconnect()

print("\n")

print("CONFIG DONE....")
