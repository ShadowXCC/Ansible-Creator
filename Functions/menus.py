def mainMenu():
    m = ""
    m += "1. Create Inventory File\n"
    m += "2. Create a Play\n"
    m += "X. Close Program\n"
    m += "\n"
    m += "Please select an option: "

    return m

def iniInvMenu():
    m = "\n"
    m += "1. Add a new title line (Example: [Title Goes Here])\n"
    m += "2. Add a new host/IP line (Example: \"8.8.8.8\" or \"HOSTNAME\"\n"
    m += "W. Write to file and exit\n"
    m += "C. Cancel and exit\n"
    m += "\n"
    m += "Please select an option: "

    return m

def yamlInvMenu():
    m = "\n"
    m += "WARNING: This program can only create simple YAML formatted inventories.\n"
    m += "1. Add a new title line (Example: Title:)\n"
    m += "2. Add a new host/IP line (Example: INDENT\"8.8.8.8\" or \"HOSTNAME\"\n"
    m += "W. Write to file and exit\n"
    m += "C. Cancel and exit\n"
    m += "\n"
    m += "Please select an option: "

    return m

def aptStatesMenu():
    m = "\n"
    m += "1. Present (Make sure that this pacakge is installed)"
    m += "2. Absent (Make sure that this package is NOT installed)"
    m += "3. Latest (Make sure that this package is the most up to date available)"
    m += "4. Build-dep (Make sure that the dependencies for this package are installed)"
    m += "5. Fixed (???)"