def mainMenu():
    m = ""
    m += "1. Create Inventory File\n"
    m += "2. Create a Play\n"
    m += "3. Fix spacing in already created playbook\n"
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
    m = ""
    m += "1. Present (Make sure that this pacakge is installed)\n"
    m += "2. Absent (Make sure that this package is NOT installed)\n"
    m += "3. Latest (Make sure that this package is the most up to date available)\n"
    m += "4. Build-dep (Make sure that the dependencies for this package are installed)\n"
    m += "5. Fixed (???)"

    return m

def aptUpgradeMenu():
    m = ""
    m += "1. No (Default Value, don't upgrade)\n"
    m += "2. Yes (Runs an \"aptitude safe-upgrade\")\n"
    m += "3. Safe (Same functionality as \"Yes\")\n"
    m += "4. Full (Runs an \"aptitude full-upgrade\")\n"
    m += "5. Dist (Runs an \"apt-get dist-upgrade\")"

    return m




# from enum import Enum

# class MainMenuOption(Enum):
#     CREATE_INVENTORY_FILE = "1. Create Inventory File"
#     CREATE_PLAY = "2. Create a Play"
#     FIX_PLAYBOOK_SPACING = "3. Fix spacing in already created playbook"
#     CLOSE_PROGRAM = "X. Close Program"

# class InventoryCreationMenuOption(Enum):
#     ADD_TITLE_LINE = "1. Add a new title line (Example: [Title Goes Here])"
#     ADD_HOST_LINE = "2. Add a new host/IP line (Example: \"8.8.8.8\" or \"HOSTNAME\")"
#     WRITE_TO_FILE_AND_EXIT = "W. Write to file and exit"
#     CANCEL_AND_EXIT = "C. Cancel and exit"

# class YamlInventoryCreationMenuOption(Enum):
#     ADD_TITLE_LINE = "1. Add a new title line (Example: Title:)"
#     ADD_HOST_LINE = "2. Add a new host/IP line (Example: INDENT\"8.8.8.8\" or \"HOSTNAME\")"
#     WRITE_TO_FILE_AND_EXIT = "W. Write to file and exit"
#     CANCEL_AND_EXIT = "C. Cancel and exit"

# class AptStatesMenuOption(Enum):
#     PRESENT = "1. Present (Make sure that this pacakge is installed)"
#     ABSENT = "2. Absent (Make sure that this package is NOT installed)"
#     LATEST = "3. Latest (Make sure that this package is the most up to date available)"
#     BUILD_DEP = "4. Build-dep (Make sure that the dependencies for this package are installed)"
#     FIXED = "5. Fixed (???)"

# class AptUpgradeMenuOption(Enum):
#     NO = "1. No (Default Value, don't upgrade)"
#     YES = "2. Yes (Runs an \"aptitude safe-upgrade\")"
#     SAFE = "3. Safe (Same functionality as \"Yes\")"
#     FULL = "4. Full (Runs an \"aptitude full-upgrade\")"
#     DIST = "5. Dist (Runs an \"apt-get dist-upgrade\")"

# def get_main_menu() -> str:
#     """Returns the main menu as a string."""
#     m = ""
#     m += f"{MainMenuOption.CREATE_INVENTORY_FILE.value}\n"
#     m += f"{MainMenu #ChatGPT never finished the code here