import sys

print("\n")

t_o = input("Enter 3rd octet of IP address:  ")

print("\n")

f_o = input("Enter 4th octet of IP address:  ")

print("\n")

if 2 <= int(f_o) <= 126:
    print ("Gateway will be 1")
    x = '.1'
elif 128 <= int(f_o) <= 254:
    print ("Gatewy will be 129")
    x = '.129'
else:
    print("Define a valid octet between (1-254)")
    sys.exit()

def_gat = '10.15.'+str(t_o)+str(x)

output = def_gat

print("\n")

print("The output is: " ,output)
sys.exit()



