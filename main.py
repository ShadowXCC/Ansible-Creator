import os

import Functions.menus as menus
import Functions.iniInventoryWriter as IIW
import Functions.yamlInventoryWriter as YIW
import Functions.playWriters as PW
import Functions.searchModules as search

print("----------------------------------------------------------------------------------------------------------")
print("WARNING: THIS PROGRAM WILL OVERWRITE ANY FILES IN THIS DIRECTORY NAMED \"inventory.yaml\" or \"playbook.yaml\"")
print("WARNING: THIS PROGRAM ASSUMES A MINIMAL ANSIBLE VERSION OF 2.0 (January 2016)")
print("----------------------------------------------------------------------------------------------------------")

print("Hello, welcome to the Ansible Generator")
print("Please note, all words in parentheses are valid options for responding to prompts.\n")

while True:
    cMM = input(menus.mainMenu())
    print() #This just prints a new line for spacing

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
                    f = open("inventory.yml", "w")
                    f.write(holder)
                    f.close()

                    cont = False

                else:
                    print("Incorrect input, try again.")

        if "yaml" in cInvFormat.lower():
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
                    f = open("inventory.yml", "w")
                    f.write(holder)
                    f.close()

                    cont = False

                else:
                    print("Incorrect input, try again.")
    if cMM == "2":
        print()
        #print(PW.add_host())
        
        # Search for play
        search.searchModules()
        # Allow user to select from search results
        # Prompt user for all info need to create proper formatted play
        # Output play to user and possibly to file if they want
    if cMM.lower() == "x":
        print()
        exit()
    
    # else:
    #     print("Else1")
    # val = input("Please enter a search term")
