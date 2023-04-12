vlan=input("indique el numero de vlan:")
nombre=input("indique su nombre:")
interface=input("indique la interface:")
interface2=input("indique interface modo troncal:")

print('''
      vlan''',vlan)
print("name",nombre)
print("                                                    ")
print("interface", interface)
print("Switchport mode Access")
print("Switchport Access Vlan",vlan)
print("Description ***PC",nombre,"***")
print('''Duplex full
Speed 100
Spanning-tree portfast''')
print("                                                    ")
print("interface",interface2)
print('''Switchport trunk allowed vlan add 10
                                                    
Para validar la configuración ejecute lo siguiente:

Show interface trunk
Show vlan
Show  interfaces''', interface, "switchport")