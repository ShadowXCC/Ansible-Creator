"""
Displays a list of choices to the user based on the given question, and returns the user's selected option.

Args:
- quest (str): The question to ask the user.
- choices (list[str]): The list of choices to display to the user.
- module (str, optional): The module to which the selected option corresponds. Defaults to an empty string.
    - A "" returns a well formatted line for a module
    - "num" returns just the position of the proper choice
    - Anything else returns the user's selection's content/answer

Returns:
- str|int: If module is not specified, returns a formatted string representing the selected option and its corresponding module.
            If module is "num", returns the integer value of the selected option.
            Otherwise, returns the string value of the selected option.
"""
def ans_from_list(quest, choices, module=""):
    if quest.lower() == "state": quest = "Do you want to specify a state for this operation"

    if y_or_n_quest(quest):
        i = 1
        for o in choices:
            print(str(i) + ". " + o.capitalize())

            i += 1

        c = int(input("Which option: "))

        if module.lower() == "num":
            return c
        elif not module:
            return "\t\t" + module + ": " + choices[c - 1]
        else:
            return choices[c - 1]

            #print(options[choice])
            # if options[choice] == ans:
            #     return options[choice]

def genericLine(word, inner):
    return "\t\t" + word + ": " + inner + "\n"

def generic2PartLine(word, outer, inner):
    r = ""
    if y_or_n_quest(outer):
        r += "\t\t" + word + ": " + inner + "\n"

    return r

def generic2PartLineWithInput(word, outer, question):
    r = ""
    if y_or_n_quest(outer):
        r += "\t\t" + word + ": " + input(question) + "\n"

    return r

def generic2Part2Lines(word1, outer, inner1, word2, inner2):
    r = ""
    if y_or_n_quest(outer):
        r += "\t\t" + word1 + ": " + inner1 + "\n"
        r += "\t\t" + word2 + ": " + inner2 + "\n"

    return r

def generic2PartWithInput(word1, outer, question1, word2, question2):
    r = ""
    if y_or_n_quest(outer):
        r += "\t\t" + word1 + ": " + question1 + "\n"
        r += "\t\t" + word2 + ": " + question2 + "\n"

    return r

# format = 0, returns a list with nothing on the original line
# format = 1, returns a list with a "|" on the original line
def multiAns(ans, format = 0):
    if " " in ans:
        if format == 1: r += "\n"
        pList = ans.split()
        if format == (0 or 1):
            for item in pList:
                r += "\t\t\t- " + item + "\n"
    else:
        return ans
    
    return r

def playStart(modName):
    name = input("What would you like to name this play: ")

    return "- name: " + name + "\n" + "\tansible.builtin." + modName + ":\n"

def seThings():
    r = ""
    r += selevel()
    r += serole()
    r += setype()
    r += seuser()

    return r

#def get_y_or_n(question):
def y_or_n_quest(question):
    """
    Asks the user a yes or no question and returns True if the user answers "y", False if the user answers "n".
    """
    return input(question + " (Y/N)? ").lower() == "y"

#######################################################################################################
# Above are more generic functions
#
# Below are line creators for modules
#######################################################################################################

def attributes(question):
    # r = ""
    # generic2PartLine("attributes", question, input("What attributes do you want (see documentation): "))
    # if y_or_n_quest(question):
    #     r = "\t\tattributes" + input("What attributes do you want (see documentation): ") + "\n"
    return generic2PartLine("attributes", question, input("What attributes do you want (see documentation): "))

def backup():
    # r = ""
    # if y_or_n_quest("Do you want to automatically create a backup file"):
    #     r = "\t\tbackup: true\n"
    return generic2PartLine("backup", "Do you want to automatically create a backup file", "true")

def decrypt():
    # r = ""
    # if y_or_n_quest("Do you NOT want to auto decrypt the source files"):
    #     r = "\t\tdecrypt: false\n"
    return generic2PartLine("decrypt", "Do you NOT want to auto decrypt the source files", "false")

def group():
    # r = ""
    # if y_or_n_quest("Do you want the resulting file system to be owned by a specified group"):
    #     r = "\t\tgroup: " + input("Enter the group name you want to own the resulting file: ") + "\n"
    return generic2PartLine("group", "Do you want the resulting file system to be owned by a specified group", input("Enter the group name you want to own the resulting file: "))

# def hour():
#     r = ""
#     if y_or_n_quest("Do you want to specify an amount of hours"):
#         r = "\t\thour: " + input("Enter the amount of hours: ") + "\n"

#     return r

def minute():
    # r = ""
    # if y_or_n_quest("Do you want to specify an amount of minutes"):
    #     r = "\t\tminute: " + input("Enter the amount of minutes: ") + "\n"
    return generic2PartLine("minute", "Do you want to specify an amount of minutes", input("Enter the amount of minutes: "))

def mode():
    # r = ""
    # if y_or_n_quest("Do you want to specify the permissions the resulting file should have"):
    #     r = "\t\tmode: " + input("Enter the permissions for the resulting file: ") + "\n"
    return generic2PartLine("mode", "Do you want to specify the permissions the resulting file should have", input("Enter the permissions for the resulting file: "))

def msg(question):
    # r = ""
    # if y_or_n_quest(question):
    #     r += "\t\tmsg: " + input("Enter the message: ") + "\n"
    return generic2PartLine("msg", question, input("Enter the message: "))

def packagesName():
    r = "\t\tname:"
    packages = input("Enter the name(s) of the package(s), with spaces separating multiple package names: ")
    if " " in packages:
        r += "\n"
        pList = packages.split()
        for item in pList:
            r += "\t\t\t- " + item + "\n"
    else:
        r += packages
    
    return r

def owner():
    # r = ""
    # if y_or_n_quest("Do you want to specify the user to own the resulting file"):
    #     r = "\t\towner: " + input("Enter the username of the new owner: ") + "\n"
    return generic2PartLine("owner", "Do you want to specify the user to own the resulting file", input("Enter the username of the new owner: "))

def regexp(question):
    # r = ""
    # if y_or_n_quest(question + ""):
    #     r = "\t\tregexp: " + input("Enter the regular expression: ") + "\n"
    return generic2PartLine("regexp", question, input("Enter the regular expression: "))

# NOT APPLICABLE YET pass in "true" for the originating machine being default, or pass in "r" for the remote machine being false
def remote_src():
    r = ""
    
    # choice = input("Are the files being worked with located on the remote machine").lower()

    # if choice == "y":
    #     r = "\t\tremote_src: true"
    # elif choice == "n":
    #     r = "\t\tremote_src: false"

    if y_or_n_quest("Are the files being worked with located on the remote machine"):
        r = "\t\tremote_src: true"
    else:
        r = "\t\tremote_src: false"

    return r

def second():
    # r = ""
    # if y_or_n_quest("Do you want to specify an amount of seconds"):
    #     r = "\t\tsecond: " + input("Enter the amount of seconds: ") + "\n"
    return generic2PartLine("second", "Do you want to specify an amount of seconds", input("Enter the amount of seconds: "))

def selevel():
    # r = ""
    # if y_or_n_quest("Do you want to specify an SELinux level/range/MLS/MCS for this action"):
    #     r = "\t\tselevel: " + input("Enter the SELinux level/range: ") + "\n"
    return generic2PartLine("selevel", "Do you want to specify an SELinux level/range/MLS/MCS for this action", input("Enter the SELinux level/range: "))

def serole():
    # r = ""
    # if y_or_n_quest("Do you want to specify an SELinux role for this action"):
    #     r = "\t\tserole: " + input("Enter the SELinux role: ") + "\n"
    return generic2PartLine("serole", "Do you want to specify an SELinux role for this action", input("Enter the SELinux role: "))

def setype():
    # r = ""
    # if y_or_n_quest("Do you want to specify an SELinux type for this action"):
    #     r = "\t\tsetype: " + input("Enter the SELinux type: ") + "\n"
    return generic2PartLine("setype", "Do you want to specify an SELinux type for this action", input("Enter the SELinux type: "))

def seuser():
    # r = ""
    # if y_or_n_quest("Do you want to specify an SELinux user for this action"):
    #     r = "\t\tseuser: " + input("Enter the SELinux user: ") + "\n"
    return generic2PartLine("seuser", "Do you want to specify an SELinux user for this action", input("Enter the SELinux user: "))

# def state(options):
#     if y_or_n_quest("Do you want to specify a state for this operation"):
#         i = 1
#         for o in options:
#             print(str(i) + ". " + o)

#             i += 1

#         choice = int(input("Which option "))

#         return "\t\tstate: " + options[choice - 1]



#         #print(options[choice])
#         # if options[choice] == ans:
#         #     return options[choice]


# This function only works if the default of state is "present", and the only other option is "absent"
def stateAbsentPresent(question):
    # r = ""
    # if y_or_n_quest(question):
    #     r = "\t\tstate: absent\n"
    return generic2PartLine("state", question, "absent")

def unsafe_writes():
    # r = ""
    # if y_or_n_quest("Do you want to allow unsafe writes to occur, only if the atomic operations fail"):
    #     r = "\t\tunsafe_writes: true\n"
    return generic2PartLine("unsafe_writes", "Do you want to allow unsafe writes to occur, only if the atomic operations fail", "true")

def update_cache():
    # r = ""
    # if y_or_n_quest("Do you want to update the apt cache"):
    #     r = "\t\tupdate_cache: true\n"
    return generic2PartLine("update_cache", "Do you want to update the apt cache", "true")

def update_cache_retries():
    # r = ""
    # if y_or_n_quest("Do you want to set an amount of retries to update the apt cache"):
    #     r = "\t\tupdate_cache_retries: " + input("How many retries for updating the apt cache? ") + "\n"
    return generic2PartLine("update_cache_retries", "Do you want to set an amount of retries to update the apt cache", input("How many retries for updating the apt cache? "))

def update_cache_retry_max_delay():
    # r = ""
    # if y_or_n_quest("Do you want to set how long in between each apt cache update attempt"):
    #     r = "\t\tupdate_cache_retry_max_delay: " + input("How many seconds do you want in between each attempt to update the apt cache? ") + "\n"
    return generic2PartLine("update_cache_retry_max_delay", "Do you want to set how long in between each apt cache update attempt", input("Enter the amount of seconds you want between each apt cache update attempt: "))

def validate():
    # r = ""
    # if y_or_n_quest("Do you want to specify a validation command to be ran, before the resulting file gets copied into place"):
    #     r = "\t\tvalidate: " + input("Enter the validation command: ") + "\n"
    return generic2PartLine("validate", "Do you want to specify a validation command to be ran, before the resulting file gets copied into place", input("Enter the validation command: "))

def validate_certs():
    # r = ""
    # if y_or_n_quest("Do you want to disable SSL certificate validation"):
    #     r = "\t\tvalidate_certs: false\n"
    return generic2PartLine("validate_certs", "Do you want to disable SSL certificate validation", "false")
