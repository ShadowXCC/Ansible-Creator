def playStart(modName):
    name = input("What would you like to name this play: ")

    return "- name: " + name + "\n" + "\tansible.builtin." + modName + "\n"

# This function only works if the default of state is "present", and the only other option is "absent"
def stateAbsentPresent():
    r = ""

    if input("Do you want to ensure that the key is absent/revoked (Y/N)? ").lower() == "y":
        r = "\t\tstate: absent\n"

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

def validate_certs():
    r = ""

    if input("Do you want to disable SSL certificate validation (Y/N)? ").lower() == "y":
        r = "\t\tvalidate_certs: false\n"
    
    return r