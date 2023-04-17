import sys

import Functions.menus as menus
import Functions.iniInventoryWriter as IIW
import Functions.yamlInventoryWriter as YIW
import Functions.playWriters as PW
import Functions.playWriterHelpers as PWH
import Functions.searchModules as search
import Functions.yamlFormatter as formatter

invFN = "inventory.yml"

print("----------------------------------------------------------------------------------------------------------")
print("WARNING: THIS PROGRAM WILL OVERWRITE ANY FILES IN THIS DIRECTORY NAMED \"inventory.yaml\" or \"playbook.yaml\"")
print("WARNING: THIS PROGRAM ASSUMES A MINIMAL ANSIBLE VERSION OF 2.4 (October 1st 2017)")
print("----------------------------------------------------------------------------------------------------------")

print("Hello, welcome to the Ansible Generator")
print("Please note, all words in parentheses are valid options for responding to prompts.\n")

while True:
    cMM = input(menus.mainMenu())
    print() # Prints a new line for spacing

    if cMM == "1":
        cInvFormat = input("Ini Format (INI) or Yaml Format (YAML) or (?) ")
        if "ini" in cInvFormat.lower():
            cont = True
            holder = ""
            while cont:
                choice = input(menus.iniInvMenu())

                if choice == "1":
                    name = input("Please enter the title: ")
                    holder += IIW.writeTitle(name)

                elif choice == "2":
                    host = input("Please enter the hostname/IP: ")
                    print() #This just prints a new line for spacing
                    holder += IIW.writeEntry(host)

                elif choice.lower() == "c":
                    cont = False

                elif choice.lower() == "w":
                    with open(invFN, "w", encoding='UTF-8') as f:
                        f.write(holder)

                    cont = False

                else:
                    print("Incorrect input, try again.")

        elif "yaml" in cInvFormat.lower():
            cont = True
            holder = ""
            titleAlreadySelected = False

            while cont:
                choice = input(menus.yamlInvMenu())
                if choice == "1":
                    name = input("Please enter the title: ")
                    if titleAlreadySelected == False:
                        holder += YIW.writeTitle(name)
                        titleAlreadySelected = True
                    elif titleAlreadySelected == True:
                        holder += "\n" + YIW.writeTitle(name)
                        titleAlreadySelected = False

                elif choice == "2":
                    host = input("Please enter the hostname/IP: ")
                    print() #This just prints a new line for spacing
                    holder += YIW.writeEntry(host)

                elif choice.lower() == "c":
                    cont = False

                elif choice.lower() == "w":
                    with open(invFN, "w", encoding='UTF-8') as f:
                        f.write(holder)

                    cont = False

                else:
                    print("Incorrect input, try again.")
    elif cMM == "2":
        while True:
            searchTerm = input("What kind of play do you want to create (\"X\" to cancel): ")
            if searchTerm.lower() != "x":
                options = search.searchModules(searchTerm)

                print("Matches for \"" + searchTerm + "\":")
                i = 1
                for item in options:
                    print(str(i) + ". " + item)
                    i += 1

                optionLength = len(options)
                selection = -1
                if optionLength > 1:
                    selection = input("\nWhich option (1-" + str(i-1) + "): ")
                elif optionLength == 1:
                    selection = 0
                elif optionLength == 0:
                    choice = PWH.y_or_n_quest("Search term not found, try again")
                    if choice.lower == "n":
                        a = False

                if selection != -1: #a != False and selection != -1:
                    selection = int(selection)
                    module = options[selection - 1]

                    if PWH.y_or_n_quest("\"" + module + "\" play selected. Is this correct?"):
                        functionCallVal = PW.funcs[module]()
                        if functionCallVal != None: print(functionCallVal)#print(PW.funcs[module]()) #https://stackoverflow.com/questions/12495218/using-user-input-to-call-functions
                    else:
                        if PWH.y_or_n_quest("Would you like to search again"):
                            break
            else:
                break

        # Search for play ✔
        # Allow user to select from search results ✔
        # Prompt user for all info need to create proper formatted play
        # Output play to user ✔ and possibly to file if they want

    elif cMM == "3":
        formatter.toFile(input("What is the name of the file: "))
        print()



    elif cMM.lower() == "x":
        print()
        sys.exit()

    # else:
    #     print("Else1")
    # val = input("Please enter a search term")
