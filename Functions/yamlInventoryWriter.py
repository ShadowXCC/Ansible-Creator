#https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html
def writeTitle(name):
    return name + ":\n"

#The "host" var can be a hostname or IP address
def writeEntry(host):
    return "\t" + host + "\n"