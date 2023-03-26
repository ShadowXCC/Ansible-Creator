def playStart(modName):
    name = input("What would you like to name this play: ")

    return "- name: " + name + "\n" + "\tansible.builtin." + modName + "\n"

def defYNQuestionAnswer(question):
    return input(question + " (Y/N)? ").lower() == "y"

def seThings():
    r = ""
    r += selevel()
    r += serole()
    r += setype()
    r += seuser()

    return r

#############################################################################################
# Above are more generic functions
#
# Below are line creators for modules
#############################################################################################

def attributes(question):
    if input(question + " (Y/N)? ").lower() == "y":
        o += "\t\tattributes" + input("What attributes do you want (see documentation): ") + "\n"

def backup():
    r = ""
    if input("Do you want to automatically create a backup file (Y/N)? ").lower() == "y":
        r = "\t\tbackup: true\n"

    return r

def decrypt():
    r = ""

    if input("Do you NOT want to auto decrypt the source files (Y/N)? ").lower() == "y":
        r = "\t\tdecrypt: false\n"

    return r

def group():
    r = ""
    if input("Do you want the resulting file system to be owned by a specified group (Y/N)? ").lower() == "y":
        r = "\t\tgroup: " + input("Enter the group name you want to own the resulting file: ") + "\n"

    return r

def mode():
    r = ""

    if input("Do you want to specify the permissions the resulting file should have (Y/N)? ").lower() == "y":
        r = "\t\tmode: " + input("Enter the permissions for the resulting file: ") + "\n"

    return r

def owner():
    r = ""

    if input("Do you want to specify the user to own the resulting file (Y/N)? ").lower() == "y":
        r = "\t\towner: " + input("Enter the username of the new owner: ") + "\n"

    return r

def regexp(question):
    r = ""

    if input(question + " (Y/N)? ").lower() == "y":
            o += "\t\tregexp: " + input("Enter the regular expression: ") + "\n"

    return r

# NOT APPLICABLE YET pass in "true" for the originating machine being default, or pass in "r" for the remote machine being false
def remote_src():
    r = ""

    choice = input("Are the files being worked with located on the remote machine (Y/N)? ").lower()

    if choice == "y":
        r = "\t\tremote_src: true"
    elif choice == "n":
        r = "\t\tremote_src: false"

    return r

def selevel():
    r = ""

    if input("Do you want to specify an SELinux level/range/MLS/MCS for this action (Y/N)? ").lower() == "y":
        r = "\t\tselevel: " + input("Enter the SELinux level/range: ") + "\n"

    return r

def serole(): 
    r = ""

    if input("Do you want to specify an SELinux role for this action (Y/N)? ").lower() == "y":
        r = "\t\tserole: " + input("Enter the SELinux role: ") + "\n"

    return r

def setype():
    r = ""

    if input("Do you want to specify an SELinux type for this action (Y/N)? ").lower() == "y":
        r = "\t\tsetype: " + input("Enter the SELinux type: ") + "\n"

    return r

def seuser():
    r = ""

    if input("Do you want to specify an SELinux user for this action (Y/N)? ").lower() == "y":
        r = "\t\tseuser: " + input("Enter the SELinux user: ") + "\n"

    return r

# This function only works if the default of state is "present", and the only other option is "absent"
def stateAbsentPresent():
    r = ""

    if input("Do you want to ensure that the key is absent/revoked (Y/N)? ").lower() == "y":
        r = "\t\tstate: absent\n"

    return r

def unsafe_writes():
    r = ""

    if input("Do you want to allow unsafe writes to occur, only if the atomic operations fail (Y/N)? ").lower() == "y":
        r = "\t\tunsafe_writes: true\n"

    return r

def update_cache():
    r = ""

    if input("Do you want to update the apt cache (Y/N)? ").lower() == "y":
        r = "\t\tupdate_cache: true\n"

    return r

def update_cache_retries():
    r = ""

    if input("Do you want to set an amount of retries to update the apt cache (Y/N)? ").lower() == "y":
            r = "\t\tupdate_cache_retries: " + input("How many retries for updating the apt cache? ") + "\n"

    return r

def update_cache_retry_max_delay():
    r = ""

    if input("Do you want to set how long in between each apt cache update attempt (Y/N)? ").lower() == "y":
        r = "\t\tupdate_cache_retry_max_delay: " + input("How many seconds do you want in between each attempt to update the apt cache? ") + "\n"
    
    return r

def validate():
    r = ""

    if input("Do you want to specify a validation command to be ran, before the resulting file gets copied into place (Y/N)? ").lower() == "y":
        r = "\t\tvalidate: " + input("Enter the validation command: ") + "\n"

    return r

def validate_certs():
    r = ""

    if input("Do you want to disable SSL certificate validation (Y/N)? ").lower() == "y":
        r = "\t\tvalidate_certs: false\n"
    
    return r