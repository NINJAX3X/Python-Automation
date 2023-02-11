import sys

t_o = input("Enter 3rd octet of IP address:  ")

print("\n")

f_o = input("Enter 4th octet of IP address:  ")

print("\n")

if int(f_o) <= 126:
    print ("Gateway will be 1")
    x = '.1'
else:
    print ("Gatewy will be 129")
    x = '.129'

def_gat = '10.15.'+str(t_o)+str(x)

output = def_gat

print("\n")

print("The outpur is: " ,output)
sys.exit()




