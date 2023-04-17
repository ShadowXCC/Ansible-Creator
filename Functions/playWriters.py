from . import playWriterHelpers as PWH
from . import menus

#---------------------------------------------------------
# Variables

baseModuleName = "\tansible.builtin."
funcs = {} # Located at very bottom of file
rrssList = ["reloaded", "restarted", "started", "stopped"]

#---------------------------------------------------------

def add_host():
    o = ""
    o += PWH.playStart("add_host")

    o += PWH.genericLine("name", input("\nExample: \"ip:portnumber\"\n" + "Enter the hostname/IP address you are adding a host to: "))
    # o += "\t\tname: " + input("\nExample: \"ip:portnumber\"\n" + "Enter the hostname/IP address you are adding a host to: ") + "\n"
    
    o += PWH.generic2PartLine("groups", "Would you like to add the \"groups\" parameter to this play", PWH.multiAns(input("Enter the group name(s), with spaces separating multiple group names: ")))
    # if PWH.y_or_n_quest("Would you like to add the \"groups\" parameter to this play"):
    #     o += "\t\tgroups:"
    #     groups = PWH.multiAns(input("Enter the group name(s), with spaces separating multiple group names: "))

    o += PWH.generic2Part2Lines("ansible_host", "Does the host you need to reach exist through a tunnel", input("Enter the hostname of the tunnel: "),
                                "ansible_port", input("Enter the port number of the tunnel: "))
    # if PWH.y_or_n_quest("Does the host you need to reach exist through a tunnel"):
    #     o += "\t\tansible_host: " + input("Enter the hostname of the tunnel: ") + "\n"
    #     o += "\t\tansible_port: " + input("What is the port number of the tunnel? ") + "\n"

    o += PWH.generic2PartLine("loop", "Do you want this play to loop", input("How many times do you want this play to loop: "))
    # if PWH.y_or_n_quest("Do you want this play to loop"):
    #     o += "\tloop: " + input("How many times do you want this play to loop: ") + "\n"

    return o

def apt():
    o = ""
    o += PWH.playStart("apt")
    o += PWH.packagesName()

    if PWH.y_or_n_quest("Do you need more specialized options for the \"apt\" task, 25 questions"):
        o += PWH.generic2PartLine("state", "Do you want to specify a required state for these packages", 
                                  PWH.ans_from_list("Enter the desired state for this package", ["present", "absent", "latest", "build-dep", "fixed"]))

        o += PWH.generic2PartLine("allow_change_held_packages", "Do you need to change the version of a held package", "true")
        # if PWH.y_or_n_quest("Do you need to change the version of a held package"):
        #     o += "\t\tallow_change_held_packages: true\n"
        o += PWH.generic2PartLine("allow_downgrade", "Do you want to allow the specified packages to downgrade if specified", "true")
        # if PWH.y_or_n_quest("Do you want to allow the specified packages to downgrade if specified"):
        #     o += "\t\tallow_downgrade: true\n"
        o += PWH.generic2PartLine("allow_unauthenticated", "Do you want packages that aren't/cannot be authenticated to still be installed", "true")
        # if PWH.y_or_n_quest("Do you want packages that aren't/cannot be authenticated to still be installed"):
        #     o += "\t\tallow_unauthenticated: true\n"
        o += PWH.generic2PartLine("autoclean", "Do you want to autoclean the local repository", "true")
        # if PWH.y_or_n_quest("Do you want to autoclean the local repository"):
        #     o += "\t\tautoclean: true\n"
        o += PWH.generic2PartLine("autoremove", "Do you want to autoremove unnused packages", "true")
        # if PWH.y_or_n_quest("Do you want to autoremove unnused packages"):
        #     o += "\t\tautoremove: true\n"
        o += PWH.generic2PartLine("cache_valid_time", "Do you want to update the apt cache if older than a set number of seconds", input("How many seconds is too old for the apt cache (Seconds): "))
        # if PWH.y_or_n_quest("Do you want to update the apt cache if older than a set number of seconds"):
        #     o += "\t\tcache_valid_time: " + input("How many seconds is too old for the apt cache (Seconds): ") + "\n"
        o += PWH.generic2PartLine("clean", "Do you want to clear out the local repository of package files", "true")
        # if PWH.y_or_n_quest("Do you want to clear out the local repository of package files"):
        #     o += "\t\tclean: true\n"
        o += PWH.generic2PartLine("deb", "Do you want to provide a path to a \".deb\" file on the remote machine", input("What is the path: ")) # This option controls the default input to the policy engine. It creates a default pin at priority 990 using the specified release string. The preferences file may further override this setting. In short, this option lets you have simple control over which distribution packages will be retrieved from. Some common examples might be -t '2.1*' or -t unstable.
        # if PWH.y_or_n_quest("Do you want to provide a path to a \".deb\" file on the remote machine"):
        #     o += "\t\tdeb: " + input("What is the path: ") + "\n" # This option controls the default input to the policy engine. It creates a default pin at priority 990 using the specified release string. The preferences file may further override this setting. In short, this option lets you have simple control over which distribution packages will be retrieved from. Some common examples might be -t '2.1*' or -t unstable.
        o += PWH.generic2PartLine("default_release", "-t option for \"apt\"", input("How high of a priority is this? "))
        # if PWH.y_or_n_quest("-t option for \"apt\""):
        #     o += "\t\tdefault_release: " + input("How high of a priority is this? ") + "\n"
        o += PWH.generic2PartLine("dpkg_options", "Do you need dpkg options", input("dpkg options: "))
        # if PWH.y_or_n_quest("Do you need dpkg options"):
        #     o += "\t\tdpkg_options: " + input("dpkg options: ") + "\n"
        o += PWH.generic2PartLine("fail_on_autoremove", "Do you want to guarantee no packages will be auto removed", "true")
        # if PWH.y_or_n_quest("Do you want to guarantee no packages will be auto removed"):
        #     o += "\t\tfail_on_autoremove: true\n"
        o += PWH.generic2PartLine("force", "Do you want to force the install to install no matter what", "true")
        # if PWH.y_or_n_quest("Do you want to force the install to install no matter what"):
        #     o += "\t\tforce: true\n"
        o += PWH.generic2PartLine("force_apt_get", "Do you want to use \"apt-get\" instead of \"apt\"", "true")
        # if PWH.y_or_n_quest("Do you want to use \"apt-get\" instead of \"apt\""):
        #     o += "\t\tforce_apt_get: true\n"
        o += PWH.generic2PartLine("install_recommends", "Do you want to install recommended packages", "true")
        # if PWH.y_or_n_quest("Do you want to install recommended packages"):
        #     o += "\t\tinstall_recommends: true\n"
        o += PWH.generic2PartLine("lock_timeout", "Do you want to set how long to wait to aquire a lock on the apt db", input("Enter a time in seconds: "))
        # if PWH.y_or_n_quest("Do you want to set how long to wait to aquire a lock on the apt db"):
        #     o += "\t\tlock_timeout: " + input("Enter a time in seconds: ") + "\n"
        o += PWH.generic2PartLine("Do you only want to upgrade packages if they are already installed", "only_upgrade", "true")
        # if PWH.y_or_n_quest("Do you only want to upgrade packages if they are already installed"):
        #     o += "\t\tonly_upgrade: true\n"
        o += PWH.generic2PartLine("policy_rc_d", "Do you want to force the exit code of \"/usr/sbin/policy-rc.d\"", input("What exit code do you want forced: "))
        # if PWH.y_or_n_quest("Do you want to force the exit code of \"/usr/sbin/policy-rc.d\""):
        #     o += "\t\tpolicy_rc_d: " + input("What exit code do you want forced: ") + "\n"
        o += PWH.generic2PartLine("purge", "If the state is set to absent, do you want to force a purge of configuration files", "true")
        # if PWH.y_or_n_quest("If the state is set to absent, do you want to force a purge of configuration files"):
        #     o += "\t\tpurge: true\n"
        o += PWH.generic2PartLine("update_cache", "Do you want to update the apt cache", "true")
        # if PWH.y_or_n_quest("Do you want to update the apt cache"):
        #     o += "\t\tupdate_cache: true\n"
        o += PWH.update_cache_retries()
        o += PWH.update_cache_retry_max_delay()
        o += PWH.generic2PartLine("upgrade", "Do you want to upgrade packages", PWH.ans_from_list("Enter a choice: ", ["no", "yes", "safe", "full", "dist"]))

    return o

def apt_key():
    o = ""
    o += PWH.playStart("apt_key")
    o += PWH.generic2PartLine("data", "Do you want to specify raw keyfile contents to add to the keyring", input("Enter the raw keyfile data: "))
    # if PWH.y_or_n_quest("Do you want to specify raw keyfile contents to add to the keyring"):
    #     o += "\t\tdata: " + input("Enter the raw keyfile data: ") + "\n"
    o += PWH.generic2PartLine("file", "Do you want to specify the path to a keyfile on the remote machine", input("Enter the keyfile's path on the remote machine: "))
    # if PWH.y_or_n_quest("Do you want to specify the path to a keyfile on the remote machine"):
    #     o += "\t\tfile: " + input("Enter the keyfile's path on the remote machine: ") + "\n"
    o += PWH.generic2PartLine("keyring", "Do you want to specify the path to the keyring file on the remote machine, should be in \"/etc/apt/trusted.gpg.d/\"", input("Enter the full path to the keyring file: "))
    # if PWH.y_or_n_quest("Do you want to specify the path to the keyring file on the remote machine, should be in \"/etc/apt/trusted.gpg.d/\""):
    #     o += "\t\tkeyring: " + input("Enter the full path to the keyring file: ") + "\n"
    o += PWH.generic2PartLine("keyserver", "Do you want to specify a keyserver", input("Enter the URL of the keyserver: "))
    # if PWH.y_or_n_quest("Do you want to specify a keyserver"):
    #     o += "\t\tkeyserver: " + input("Enter the URL of the keyserver: ") + "\n"

    h = PWH.stateAbsentPresent("Do you want to ensure that the key is absent/revoked")
    if h != "":
        o += h
        o += "\t\tid: " + input("Enter the key's identifier: ") + "\n"
    elif PWH.y_or_n_quest("Do you want to specify a key identifier"):
        o += "\t\tid: " + input("Enter the key's identifier: ") + "\n"
        o += PWH.genericLine("id", input("Enter the key's identifier: "))

    o += PWH.generic2PartLine("url", "Do you want to specify a URL to retrieve the key from", input("What is the URL to retrieve the key from? "))
    # if PWH.y_or_n_quest("Do you want to specify a URL to retrieve the key from"):
    #     o += "\t\turl: " + input("What is the URL to retrieve the key from? ") + "\n"
    o += PWH.validate_certs()

    return o

def apt_repository():
    o = ""
    o += PWH.playStart("apt_repository")

    print("\nHelp: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_repository_module.html#parameters")
    o += PWH.genericLine("repo", input("From the above link, what is the source string for the repository: "))
    # o += "\t\trepo: " + input("From the above link, what is the source string for the repository: ") + "\n"
    o += PWH.generic2PartLine("codename", "Do you want to override the distribution codename used for PPA repositories", input("Enter the distribution codename: "))
    # if PWH.y_or_n_quest("Do you want to override the distribution codename used for PPA repositories"):
    #     o += "\t\tcodename: " + input("Enter the distribution codename: ") + "\n"
    o += PWH.generic2PartLine("filename", "Do you want to specify the filename of the added repository", input("Enter the filename (without any file extension): "))
    # if PWH.y_or_n_quest("Do you want to specify the filename of the added repository"):
    #     o += "\t\tfilename: " + input("Enter the filename (without any file extension): ") + "\n"
    o += PWH.generic2PartLine("install_python_apt", "Do you want to automatically try to install the Python apt library", "false")
    # if PWH.y_or_n_quest("Do you want to automatically try to install the Python apt library"):
    #     o += "\t\tinstall_python_apt: false\n"
    o += PWH.generic2PartLine("mode", "Do you want to set a mode/permission octal for this repo", input("Enter the mode/permission octal for this repo (ex: 0644): "))
    # if PWH.y_or_n_quest("Do you want to set a mode/permission octal for this repo"):
    #     o += "\t\tmode: " + input("Enter the mode/permission octal for this repo (ex: 0644): ") + "\n"
    
    o += PWH.stateAbsentPresent("Do you want the source string state set to absent")
    o += PWH.update_cache()
    o += PWH.update_cache_retries()
    o += PWH.update_cache_retry_max_delay()
    o += PWH.validate_certs()

    return o

def assemble():
    o = ""
    o += PWH.playStart("assemble")
    o += "\t\tdest: " + input("What do you want to name the output file of this play: ") + "\n"
    o += "\t\tsrc: " + input("What is the path of the directory that you want \"assembled\": ") + "\n"

    if PWH.y_or_n_quest("Do you need more specialized options for the \"assemble\" task, 13 questions"):

        print("https://docs.ansible.com/ansible/latest/collections/ansible/builtin/assemble_module.html#parameter-attributes")
        o += PWH.attributes("Do you want to set any attributes for the resulting file")
        o += PWH.backup()
        o += PWH.decrypt()
        if PWH.y_or_n_quest("Do you want to specify a delimiter to separate file contents"):
            o += "\t\tdeliminiter: " + input("What delimiter do you want to use: ") + "\n"
        o += PWH.group()
        if PWH.y_or_n_quest("Do you want this operation to include hidden files in the assembling"):
            o += "\t\tignore_hidden: true\n"
        o += PWH.mode()
        o += PWH.owner()
        o += PWH.regexp("Do you want to use a regular expression to specify files to be assembled, using Python syntax")
        o += PWH.remote_src()
        o += PWH.seThings()
        o += PWH.unsafe_writes()
        o += PWH.validate()

    return o

def Assert():
    print("WARNING: This currently only accepts a SINGLE assertion per each play created.")

    o = ""
    o += PWH.playStart("assert")

    assertion = input("What do you want to be asserted: ")
    o += "\t\tthat:\n\t\t\t- " + assertion + "\n"
    if PWH.y_or_n_quest("Do you want to specify a fail message"):
        o += "\t\tfail_msg: " + input("Enter the fail message: ") + "\n"
    if PWH.y_or_n_quest("Do you want to specify a success message"):
        o += "\t\tsuccess_msg: " + input("Enter the success message: ") + "\n"

    return o

def async_status():
    o = ""
    o += PWH.playStart("async_status")

    o += "\t\tjid: " + input("What is the job or task identifier for the asynchronous task: ") + "\n"
    if PWH.y_or_n_quest("Do you want to also clean up the async job cache for the specified ID"):
        o += "\t\tmode: cleanup\n"
    return o

def blockinfile():
    o = ""
    o += PWH.playStart("blockinfile")

    o += "\t\tpath: " + input("What is the path to the file being edited: ") + "\n"
    i = input("Enter the text (with newlines/enters replaced with a \"|\"): ").replace("|", "\n\t\t\t")
    o += "\t\tblock: |\n\t\t\t" + i + "\n"

    c = PWH.ans_from_list("How do you want to specify where the text being added goes?", ["Insert Before", "Insert After"], "num")
    if c == 1:
        c = PWH.ans_from_list("", ["EOF (End of File)", "Literal Match/Regular Expression (Regex)"], "num")
        if c == 1:
            c = "EOF"
        else:
            c = input("What match/expression should your text be inserted after: ")
        
        o += "\t\tinsertafter: " + c + "\n"
    elif c == 2:
        c = PWH.ans_from_list("", ["BOF (Beginning of File)", "Literal Match/Regular Expression (Regex)"], "num")
        if c == 1:
            c = "BOF"
        else:
            c = input("What match/expression should your text be interted before: ")

        o += "\t\tinsertbefore: " + c + "\n"

    print("https://docs.ansible.com/ansible/latest/collections/ansible/builtin/blockinfile_module.html#parameter-attributes")
    o += PWH.attributes("Do you want to set any attributes for the file being worked on")
    o += PWH.backup()

    if PWH.y_or_n_quest("Do you want to include a line that marks the beginning and end of the text block being managed by Ansible"):
        print("It is good practice to make your marker a comment, including whatever include appropriate to whatever file type you are modifying.")
        print("Make sure to include the value \"{{mark}}\" within your chosen marker line.")
        o += "\t\tmarker: \"" + input("Enter the desired marker line: ") + "\"\n"
        o += "\t\tmarker_begin: " + input("In the beginning marker line, what should \"{{mark}}\" be replaced with: ") + "\n"
        o += "\t\tmarker_end: " + input("In the ending marker line, what should \"{{mark}}\" be replaced with: ") + "\n"

    if PWH.y_or_n_quest("Do you want this play to create a file, if it does not already exist"):
        o += "\t\tcreate: true\n"
    o += PWH.group()
    o += PWH.mode()
    o += PWH.owner()
    o += PWH.seThings()
    o += PWH.stateAbsentPresent("Do you want the block to not be present")
    o += PWH.unsafe_writes()
    o += PWH.validate()

    return o

def command():
    #command module
    o = ""
    o += PWH.playStart("command")

    # argv
    # chdir
    # cmd
    # creates
    # free_form
    # removes
    # stdin
    # stdin_add_newline
    # strip_empty_ends

    return o

def copy():
    #copy module
    o = ""
    o += PWH.playStart("copy")
    #dest

    print("https://docs.ansible.com/ansible/latest/collections/ansible/builtin/copy_module.html")
    o += PWH.attributes("Do you want the copied files to have any specific attributes?")
    o += PWH.backup()
    # checksum 
    # content 
    o+= PWH.decrypt()
    # directory_mode 
    # follow 
    # force 
    o += PWH.group()
    # local_follow 
    o += PWH.mode()
    o += PWH.owner()
    o += PWH.remote_src()    
    o += PWH.seThings()
    # src 
    o += PWH.unsafe_writes()
    o += PWH.validate()

    return o

def cron():
    #cron module
    o = ""
    o += PWH.playStart("cron")

    #name


    o += PWH.backup()
    # cron_file 
    # day 
    # disabled 
    # env 
    # hour 
    # insertafter 
    # insertbefore 
    # job 
    # minute 
    # month 
    # special_time 
    o += PWH.stateAbsentPresent("Do you want the job/environment variable to be absent")
    # user
    # weekday

    return o

def debconf():
    #debconf module
    o = ""
    o += PWH.playStart("debconf")

    # name

    # question 
    # unseen 
    # value 
    # vtype
    vtype = ""

    if vtype == "password":
        o += "\t\tno_log: true\n"

    return o

def debug():
    o = ""
    o += PWH.playStart("debug")

    print("Only a custom message OR a variable being debug can be set at once.")
    o += PWH.msg("Do you want to set a custom message?")
    if "msg: " not in o:
        o += "\t\tvar: " + input("Enter the name of the variable to be debugged: ") + "\n"
    if PWH.y_or_n_quest("Do you want to specify a verbosity level for this debug play"):
        vNum = PWH.ans_from_list("", ["Verbose (-v)", "Very Verbose (-vv)", "Very Very Verbose (-vvv)", "4 (This is a valid option, but what it does is a mystery)"], "num")
        
        o += "\t\tverbosity: " + vNum + "\n"

    return o

def dnf():
    #dnf module
    o = ""
    o += PWH.playStart("dnf")
    # name

    # allow_downgrade 
    # allowerasing 
    # autoremove 
    # bugfix 
    # cacheonly 
    # conf_file 
    # disable_excludes 
    # disable_gpg_check 
    # disable_plugin
    # disablerepo 
    # download_dir 
    # download_only 
    # enable_plugin 
    # enablerepo 
    # exclude 
    # install_repoquery 
    # install_weak_deps 
    # installroot
    # list 
    # lock_timeout 
    # nobest 
    # releasever 
    # security 
    # skip_broken 
    # sslverify 
    # complicatedState 
    o += PWH.update_cache()
    # update_only 
    o += PWH.validate_certs()


    return o

def dpkg_selections():
    o = ""
    o += PWH.playStart("dpkg_selections")

    o += "\t\tname: " + input("Enter the name of the package, whose state is to be set/modified: ") + "\n"
    o += "\t\tselection: " + PWH.ans_from_list("What state do you want to set the package(s) too? ", ["Install (Installs a new package)", "Uninstall (Unistalls an existing package)", "Hold (Prevents updating the package if a newer version is available)", "Purge (Removes the package and its configs)"]) + "\n"

    return o

def expect():
    o = ""
    o += PWH.playStart("expect")
    o += "\t\tcommand: " + input("Enter the command to be ran: ") + "\n"
    i = PWH.multiAns(input("Enter the response(s), with a space separating multiple answers: "))
    o += "\t\tresponses: " + i + "\n"

    if PWH.y_or_n_quest("Do you want to change the directory prior to the running of the command"):
        o += "\t\tchdir: " + input("Enter the directory path to change to: ") + "\n"
    if PWH.y_or_n_quest("Do you want your responses typed visibly"):
        o += "\t\techo: true\n"
    if PWH.y_or_n_quest("Do you want to stop the running of the command if a specified file exists"):
        o += "\t\tcreates: " + input("Enter the path to the file: ") + "\n"
    if PWH.y_or_n_quest("Do you want to stop the running of the command if a specified file does NOT exist"):
        o += "\t\tremoves: " + input("Enter the path to the file: ") + "\n"
    if PWH.y_or_n_quest("Do you want to set a timeout, in seconds, to wait for the expected"):
        o += "\t\ttimeout: " + input("Enter the timeout time in seconds: ") + "\n"

    return o

def fail():
    o = ""
    o += PWH.playStart("fail")
    o += PWH.msg("Do you want to set a custom message for when this play causes an exception")

    return o

def fetch():
    #fetch module
    o = ""
    o += PWH.playStart("fetch")

    o += PWH.genericLine("src", input("Enter the remote path containing the target"))
    o += PWH.genericLine("dest", input("Enter the local location where you want the target to be saved"))


    o += PWH.generic2PartLine("fail_on_missing", "Do you want the task to still succeed if it cannot interact with the target file", "false")
    #o += PWH.genericLine("fail_on_missing", "For some reason, do you want the task to still succeed if it cannot see the target file", "")
    
    print("https://docs.ansible.com/ansible/latest/collections/ansible/builtin/fetch_module.html#parameter-flat")
    o += PWH.generic2PartLine("flat", "Do you want to override the default behavior of appending hostname/path/to/file to the destination", "true")
    o += PWH.generic2PartLine("validate_checksum", "Do you want to not validate the copied file's checksum", "false")

    return o

def file():
    #file module
    o = ""
    o += PWH.playStart("file")
    #path

    # access_time
    # access_time_format
    print("https://docs.ansible.com/ansible/latest/collections/ansible/builtin/file_module.html#parameter-attributes")
    o += PWH.attributes("Do you want the created file to have any specific attributes")
    # follow
    # force
    o += PWH.group()
    o += PWH.mode()
    # modification_time
    # modification_time_format
    o += PWH.owner()
    # recurse
    o += PWH.seThings()
    # src
    # complicatedState
    o += PWH.unsafe_writes()

    return o

def find():
    #find module
    o = ""
    o += PWH.playStart("find")
    # paths

    # age 
    # age_stamp 
    # contains 
    # depth 
    # excludes 
    # file_type 
    # follow 
    # get_checksum 
    # hidden 
    # patterns 
    # read_whole_file 
    # recurse 
    # size
    # use_regex

    return

def gather_facts():
    o = ""
    o += PWH.playStart("gather_facts")

    print("NOTE: Disabling parallelization will guarantee the order of facts gathered, but at the expense of performance.")
    if PWH.y_or_n_quest("Do you want to disable parallel fact gathering"):
        o += "\t\tparallel: false\n"

    return o

def get_url():
    #get_url module
    o = ""
    o += PWH.playStart("get_url")
    # dest

    print("https://docs.ansible.com/ansible/latest/collections/ansible/builtin/replace_module.html#parameter-attributes")
    o += PWH.attributes("Do you want the downloaded file to have any specific attributes")
    o += PWH.backup()
    # checksum 
    # ciphers 
    # client_cert 
    # client_key 
    # decompress 
    # force 
    # force_basic_auth 
    o += PWH.group()
    # headers
    # http_agent 
    o += PWH.mode()
    o += PWH.owner()
    o += PWH.seThings()
    # timeout 
    # tmp_dest 
    # unredirected_headers 
    o += PWH.unsafe_writes()
    # url 
    # url_password 
    # url_username
    # use_gssapi 
    # use_netrc 
    # use_proxy 
    o += PWH.validate_certs()

    return o

def getent():
    #getent module
    o = ""
    o += PWH.playStart("getent")
    # database

    # fail_key 
    # key 
    # service 
    # split

    return o

def git():
    #git module
    o = ""
    o += PWH.playStart("git")

    #dest repo

    # accept_hostkey 
    # accept_newhostkey 
    # archive 
    # archive_prefix 
    # bare 
    # clone 
    # depth 
    # executable 
    # force 
    # gpg_whitelist 
    # key_file
    # recursive 
    # reference 
    # refspec 
    # remote 
    # separate_git_dir 
    # single_branch 
    # ssh_opts 
    # track_submodules 
    # umask 
    # update 
    # verify_commit
    # version

    return o

def group():
    o = ""
    o += PWH.playStart("group")
    o += "\t\tname: " + input("Enter the name of the group being managed: ") + "\n"

    if PWH.y_or_n_quest("Do you want to set a GID for the resulting group"):
        o += "\t\tgid: " + input("Enter the GID: ") + "\n"
    print("https://docs.ansible.com/ansible/latest/collections/ansible/builtin/group_module.html#parameter-local")
    if PWH.y_or_n_quest("Do you want to force the use of \"local\" command alternatives"):
        o += "\t\tlocal: true\n"
    if PWH.y_or_n_quest("Do you want to change the group ID to a non-unique value (the GID needed to be set earlier for this)"):
        o += "\t\tnon_unique: true\n"
    o += PWH.stateAbsentPresent("Do you want the created group to be absent on the remote host")
    if PWH.y_or_n_quest("Do you want for this group to be a \"system\" group"):
        o += "\t\tsystem: true\n"

    return o

def group_by():
    o = ""
    o += PWH.playStart("group_by")

    o += "\t\tkey: " + input("Enter the Ansible variables (Jinja Format) to be used for group creation") + "\n"
    if PWH.y_or_n_quest(""):        
        o += "\t\tparents: "
        i = PWH.multiAns(input("Enter the parent group, or groups separated by spaces: "))

    return o

def hostname():
    o = ""
    o += PWH.playStart("hostname")

    o += "\t\tname: " + input("What do you want to set the hostname as? ") + "\n"
    print("https://docs.ansible.com/ansible/latest/collections/ansible/builtin/hostname_module.html#parameter-use")
    ans = PWH.ans_from_list("NOTE: It is highly recommended to not use the autodetect option.\nWhich strategy do you want to use to update the hostname?", 
                            ["alpine", "debian", "freebsd", "generic", "macos", "macosx","darwin", "openbsd", "openrc", "redhat", "sles", "solaris", "systemd", "autodetect"])
    if ans == "autodetect":
        o += ""
    else:
        o += "\t\tuse: " + ans + "\n"

    return o

def import_playbook():
    o = ""
    o += "- name: " + input("What would you like to name this play: ") + "\n\tansible.builtin.import_playbook" + input("What is the filename of the playbook being imported? ") + "\n"
    return o

def import_role():
    #import_role module
    o = ""
    o += PWH.playStart("import_role")
    # name

    # allow_duplicates 
    # defaults_from 
    # handlers_from 
    # rolespec_validate 
    # tasks_from 
    # vars_from

    return o

def import_tasks():
    #import_tasks module
    o = ""
    o += PWH.playStart("import_tasks")

    # file 
    # free-form

    return o

def include():
    o = "\nSorry, this module has been deprecated due to conflicting behaviors. For more information, please visit: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/include_module.html#deprecated\n\nPossible replacements:\n- \"include_tasks\" (https://docs.ansible.com/ansible/latest/collections/ansible/builtin/include_tasks_module.html)\n- \"import_tasks\" (https://docs.ansible.com/ansible/latest/collections/ansible/builtin/import_tasks_module.html)\n- \"import_playbook\" (https://docs.ansible.com/ansible/latest/collections/ansible/builtin/import_playbook_module.html)\n"
    # o = ""
    # o += PWH.playStart("include")
    # free-form 
    return o

def include_role():
    #include_role module
    o = ""
    o += PWH.playStart("include_role")
    # name

    # allow_duplicates 
    # apply 
    # defaults_from 
    # handlers_from 
    # public 
    # rolespec_validate 
    # tasks_from 
    # vars_from

    return o

def include_tasks():
    #include_tasks module
    o = ""
    o += PWH.playStart("include_tasks")

    # apply 
    # file 
    # free-form

    return o

def include_vars():
    #include_vars module
    o = ""
    o += PWH.playStart("include_vars")

    # depth 
    # dir 
    # extensions 
    # file 
    # files_matching
    # free-form 
    # hash_behaviour 
    # ignore_files 
    # ignore_unknown_extensions 
    # name 

    return o

def iptables():
    #iptables module
    o = ""
    o += PWH.playStart("iptables")

    # action 
    # chain 
    # chain_management 
    # comment 
    # ctstate 
    # destination 
    # destination_port 
    # destination_ports 
    # dst_range 
    # flush
    # fragment 
    # gateway 
    # gid_owner 
    # goto 
    # icmp_type 
    # in_interface 
    # ip_version 
    # jump 
    # limit 
    # limit_burst 
    # log_level 
    # log_prefix
    # match 
    # match_set 
    # match_set_flags 
    # out_interface 
    # policy 
    # protocol 
    # reject_with 
    # rule_num 
    # set_counters 
    # set_dscp_mark
    # set_dscp_mark_class
    # source
    # source_port
    # src_range
    o += PWH.stateAbsentPresent("Do you want the rule to not be present")
    # syn
    # table
    # tcp_flags(flags flags_set)
    # to_destination to_ports
    # to_source
    # uid_owner
    # wait

    return o

def known_hosts():
    o = ""
    o += PWH.playStart("known_hosts")
    o += "\t\tname: " + input("Enter the host you want to be added/removed in the \"known_hosts\" file: ") + "\n"

    if PWH.y_or_n_quest("Do you want the hostname hashed in the \"known_hosts\" file"):
        o += "\t\thash_host: true\n"
    if PWH.y_or_n_quest("Do you want to provide a SSH public host key"):
        o += "\t\tkey: " + input("Enter the SSH public host key: ") + "\n"
    if PWH.y_or_n_quest("Do you want to specify a specific \"known_hosts\" file to be edited"):
        o += "\t\tpath: " + input("Enter the path to the file: ") + "\n"
    o += PWH.stateAbsentPresent("Do you want to remove the host key")

    return o

def lineinfile():
    #lineinfile module
    o = ""
    o += PWH.playStart("lineinfile")
    # path

    print("https://docs.ansible.com/ansible/latest/collections/ansible/builtin/lineinfile_module.html#parameter-attributes")
    o += PWH.attributes("Do you want to specify attributes for the file being worked on")
    # backrefs
    o += PWH.backup()
    # create
    # firstmatch
    o += PWH.group()
    # insertafter
    # insertbefore
    # line
    o += PWH.mode()
    # others
    o += PWH.owner()
    o += PWH.regexp("Do you you want to use a regular expression for this action")
    # search_string
    o += PWH.seThings()
    o += PWH.stateAbsentPresent("Do you want the line to not be present in the file")
    o += PWH.unsafe_writes()
    o += PWH.validate()

    return o

def meta():
    #meta module
    o = ""
    o += PWH.playStart("meta")

    # free_form

    return o

def package():
    o = ""
    o += PWH.playStart("package")

    o += PWH.packagesName()
    o += PWH.ans_from_list("state", ["present", "absent"], "package")

    print("NOTE: The default selection is usually very good, and is recommended to be used.\n Only specify a package manager if needed.")
    if PWH.y_or_n_quest("Do you want to specify a package manager to be used for this package installation"):
        print("https://docs.ansible.com/ansible/latest/collections/ansible/builtin/package_module.html#parameter-use")
        o += "\t\tuse: " + input("Enter the package manager that you want to use: ") + "\n"

    return o

def package_facts():
    o = ""
    o += PWH.playStart("package_facts")

    print("NOTE: The default selection is usually very good, and is recommended to be used.\n Only specify a package manager if needed.")
    if PWH.y_or_n_quest("Do you want to specify a package manager to use in querying for package information"):
        o += "\t\tmanager: " + PWH.ans_from_list("Which package manager do you want to use", ["auto", "rpm", "apt", "portage", "pkg", "pacman", "apk", "pkg_info"]) + "\n"
    if PWH.y_or_n_quest("Do you want to specify a querying strategy?"):
        o += "\t\tstrategy: " + PWH.ans_from_list("Which querying strategy do you want to use?", ["first", "all"]) + "\n"

    return o

def pause():
    o = ""
    o += PWH.playStart("pause")

    #print("https://docs.ansible.com/ansible/latest/collections/ansible/builtin/pause_module.html#parameter-echo")
    print("NOTE: If you specify a message to be echoed an amount of time, the echoed message will be ignored.")
    if PWH.y_or_n_quest("Do you want the ability for input to be shown during the pause"):
        o += "\t\techo: false"
    if PWH.y_or_n_quest("Do you want to specify a prompt to be shown during the pause"):
        o += "\t\tprompt: " + input("What should the prompt be: ") + "\n"
    if PWH.y_or_n_quest("Do you want to specify an amount of time to pause playbook execution for"):
        mins = input("How many minutes to pause for: ")
        secs = input("How many seconds to pause for: ")
        if mins > 0:
            o += "\t\tminutes: " + input("") + "\n"
        if secs > 0:
            o += "\t\tseconds: " + input("") + "\n"

    return o

def ping():
    o = ""
    o += PWH.playStart("ping")
    if PWH.y_or_n_quest("Do you want this function to force an exception"):
        o += "\t\tdata: crash\n"
    return o

def pip():
    o = ""
    o += PWH.playStart("pip")

    name = input("Enter the name of the library being modified (X to skip): ")
    if name.lower() != "x": o += "\t\tname: " + name + "\n"
    if PWH.y_or_n_quest("Do you want to specify a version of the library being installed"):
        o += "\t\tversion: " + input("Enter the version number (ex: 13.3.11): ") + "\n"

    if PWH.y_or_n_quest("Do you want to change the directory prior to running this command"):
        o += "\t\tchdir: " + input("Enter the path to the directory: ") + "\n"
    if PWH.y_or_n_quest("Do you want to make the installed files editable to the user"):
        o += "\t\teditable: true\n"
    if PWH.y_or_n_quest("Do you need to specify a different pip version for the desired installation"):
        o += "\t\texecutable: " + input("Enter the path to the different pip executable: ") + "\n"
    if PWH.y_or_n_quest("Do you want to provide extra command line arguments to pip"):
        o += "\t\textra_args: " + input("Enter your desired command line arguments: ") + "\n"
    if PWH.y_or_n_quest("Do you want to utilize a requirements file"):
        o += "\t\trequirements: " + input("Enter the path to the requirements file on the remote machine: ") + "\n"
    o += PWH.ans_from_list("state", ["absent", "forcereinstall", "latest", "present"], "pip")
    if PWH.y_or_n_quest("Do you want to specify a umask for the installed libraries"):
        o += "\t\tumask: " + input("Enter the desired umask mode as an octal: ") + "\n"
    if PWH.y_or_n_quest("Do you want to specify a version of the library being installed"):
        o += "\t\tversion: " + input("Enter the version number (ex: 13.3.11): ") + "\n"
    if PWH.y_or_n_quest("Do you want to create a virtual environment"):
        o += "\t\tvirtualenv: " + input("Enter the directory path for the desired location: ") + "\n"
        if PWH.y_or_n_quest("Do you want to specify a command/pathname to use in the creation of the virtual environment"):
            o += "\t\virtualenv_command: " + input("Enter the desired command/pathname: ") + "\n"
        if PWH.y_or_n_quest("Do you want to specify a Python version for this play"):
            o += "\t\tvirtualenv_python: python" + input("Enter just the version number (ex: 3.5 or 2.7): ") + "\n"
        if PWH.y_or_n_quest("Do you want the virtual environment to inherit packages from the global site-packages directory"):
            o += "\t\tvirtualenv_site_packages : true\n"

    return o

def raw():
    #raw module
    o = ""
    o += PWH.playStart("raw")

    # free_form
    # executable

    return o

def reboot():
    o = ""
    o += PWH.playStart("reboot")

    print("NOTE: This only provides the default behavior.")
    if PWH.y_or_n_quest("Do you want to run a command on startup that prints a message stating the last time the system was booted"):
        o += "\t\t: \"cat /proc/sys/kernel/random/boot_id\"\n"                         
    if PWH.y_or_n_quest("Do you want to specify a max amount of seconds between connection attempts"):
        o += "\t\t: " + input("Enter the max amount of seconds: ") + "\n"
    o += PWH.msg("Do you want to set a custom message to display before rebooting?")
    if PWH.y_or_n_quest("Do you want to specify an amount of time to wait AFTER rebooting"):
        o += "\t\tpost_reboot_delay: " + input("Enter the amount of seconds to wait AFTER rebooting: ") + "\n"
    if PWH.y_or_n_quest("Do you need to specify an amount of time to wait BEFORE rebooting"):
        o += "\t\pre_reboot_delay : " + input("Enter the amount of seconds to wait BEFORE rebooting: ") + "\n"
    if PWH.y_or_n_quest("Do you want to a custom reboot command for the target system"):
        o += "\t\treboot_command: " + input("Enter the custom reboot command: ") + "\n"
    if PWH.y_or_n_quest("Do you want to specify a max amount of seconds to wait for the machine to reboot"):
        o += "\t\treboot_timeout: " + input("Enter the desired amount of time in seconds: ") + "\n"
    if PWH.y_or_n_quest("Do you need to specify a nonstandard location for the reboot command"):
        i = input("Enter the path, or paths separated by spaces: ")
        if " " in i:
            i = str(i.split())
    
        o += "\t\tsearch_paths: " + i + "\n"
    if PWH.y_or_n_quest("Do you want to specify an nondefault test command, that determines if the machine has rebooted"):
        o += "\t\ttest_command: " + input("Enter the desired test command: ") + "\n"
 
    return o

def replace():
    print("WARNING: This will replace exactly what you tell it to do, be careful.")
    o = ""
    o += PWH.playStart("replace")
    o += "\t\tpath: " + input("Enter the path to the file being modified: ") + "\n"

    print("Python Regex: https://docs.python.org/3/library/re.html")
    print("Ansible Documentation: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/replace_module.html#parameter-regexp")
    o += "\t\tregexp: " + input("Enter the regular expression used for matching: ") + "\n"

    o += "\t\treplace: " + input("Enter the value to replace all matches with: ") + "\n"

    if PWH.y_or_n_quest("Do you want the content that occurs after the match to be replaced"):
        o += "\t\tafter: " + input("Enter the content: ") + "\n"
    if PWH.y_or_n_quest("Do you want the content that occurs before the match to be replaced"):
        o += "\t\tbefore: " + input("Enter the content: ") + "\n"

    print("https://docs.ansible.com/ansible/latest/collections/ansible/builtin/replace_module.html#parameter-attributes")
    o += PWH.attributes()
    o += PWH.backup()
    if PWH.y_or_n_quest("Do you want to specify a non-UTF-8 encoding for the file being edited"):
        o += "\t\tencoding: " + input("Enter the encoding type: ") + "\n"
    o += PWH.group()
    o += PWH.mode()
    print("https://docs.ansible.com/ansible/latest/collections/ansible/builtin/replace_module.html#parameter-others")
    if PWH.y_or_n_quest("Do you want to use extra arguments for this operation"):
        o += "\t\t:others " + input("Enter the extra arguments: ") + "\n"
    o += PWH.owner()
    o += PWH.seThings()
    o += PWH.unsafe_writes()
    o += PWH.validate()

    return o

def rpm_key():
    #rpm_key module
    o = ""
    o += PWH.playStart("rpm_key")

    # fingerprint
    # key
    o += PWH.stateAbsentPresent("Do you want the key to be removed from the rpm database")
    o += PWH.validate_certs()

    return o

def script():
    #script module
    o = ""
    o += PWH.playStart("script")

    # chdir
    # cmd
    # creates
    o += PWH.decrypt()
    # executable
    # free_form
    # removes

    return o

def service():
    #service module
    o = ""
    o += PWH.playStart("service")

    # arguments
    # enabled
    # name
    # pattern
    # runlevel
    # sleep
    o += PWH.ans_from_list("state", rrssList, "service")
    # use

    return o

def service_facts():
    #service_facts module
    o = ""
    o += PWH.playStart("service_facts")

    # 

    return o

def set_fact():
    #set_fact module
    o = ""
    o += PWH.playStart("set_fact")
    # key_value

    # cacheable 

    return o

def set_stats():
    #set_stats module
    o = ""
    o += PWH.playStart("set_stats")
    # data

    # aggregate per_host

    return o

def setup():
    #setup module
    o = ""
    o += PWH.playStart("setup")

    # fact_path 
    # filter 
    # gather_subset 
    # gather_timeout

    return o

def shell():
    #shell module
    o = ""
    o += PWH.playStart("shell")

    # chdir 
    # cmd 
    # creates 
    # executable 
    # free_form 
    # removes 
    # stdin 
    # stdin_add_newline
    
    return o

def slurp():
    o = ""
    o += PWH.playStart("slurp")

    print("NOTE: This module only works on files, not directories. It also only copies the file into memory, so it must be registered into a variable.")
    o += "\t\tslurp: " + input("Enter the file path to the file you want \"slurped\"/gotten:") + "\n"
    o += "\tregister: " + input("Enter a variable name to store the file:") + "\n"

    return o

def stat():
    #stat module
    o = ""
    o += PWH.playStart("stat")
    # path

    # checksum_algorithm 
    # follow 
    # get_attributes 
    # get_checksum 
    # get_mime

    return o

def subversion():
    #subversion module
    o = ""
    o += PWH.playStart("subversion")
    # repo

    # checkout 
    # dest 
    # executable 
    # export 
    # force 
    # in_place 
    # password
    # revision 
    # switch 
    # update 
    # username 
    o += PWH.validate_certs()

    return o

def systemd():
    #systemd module
    o = ""
    o += PWH.playStart("systemd")

    # daemon_reexec 
    # daemon_reload 
    # enabled 
    # force 
    # masked 
    # name 
    # no_block 
    # scope 
    o += PWH.ans_from_list("state", rrssList, "systemd")

    return o

def systemd_service():
    #systemd_service module
    o = ""
    o += PWH.playStart("systemd_service")

    # daemon_reexec 
    # daemon_reload 
    # enabled 
    # force 
    # masked 
    # name 
    # no_block 
    # scope 
    o += PWH.ans_from_list("state", rrssList, "systemd_service")

    return o

def sysvinit():
    #sysvinit module
    o = ""
    o += PWH.playStart("sysvinit")
    # name

    # arguments 
    # daemonize 
    # enabled 
    # pattern 
    # runlevels 
    # sleep 
    o += PWH.ans_from_list("state", rrssList, "sysvinit")

    return o

def tempfile():
    o = ""
    o += PWH.playStart("tempfile")

    o += "\t\tpath: " + input("Enter the path for where the temp file should be created: ") + "\n"
    if PWH.y_or_n_quest("Do you want to provide a prefix for the created file/directory"):
        o += "\t\tprefix: " + input("Enter the prefix: ") + "\n"
    o += PWH.ans_from_list("state", ["directory", "file"], "tempfile")
    if PWH.y_or_n_quest("Do you want to provide a suffix for the created file/directory"):
        o += "\t\tsuffix: " + input("Enter the suffix: ") + "\n"

    return o

def template():
    #template module
    o = ""
    o += PWH.playStart("template")
    # dest 
    # src

    print("https://docs.ansible.com/ansible/latest/collections/ansible/builtin/template_module.html#parameter-attributes")
    o += PWH.attributes("Do you want to specify attributes for the file created by this template")
    o += PWH.backup
    # block_end_string 
    # block_start_string 
    # comment_end_string 
    # comment_start_string 
    # follow 
    # force 
    o+= PWH.group()
    # lstrip_blocks
    o += PWH.mode() 
    # newline_sequence 
    # output_encoding 
    o += PWH.owner()
    o += PWH.seThings()
    # trim_blocks 
    o += PWH.unsafe_writes()
    o += PWH.validate()
    # variable_end_string
    # vari

    return o

def unarchive():
    #unarchive module
    o = ""
    o += PWH.playStart("unarchive")
    # dest src

    print("https://docs.ansible.com/ansible/latest/collections/ansible/builtin/unarchive_module.html#parameter-attributes")
    o += PWH.attributes("Do you want any specific attributes on the resulting files")
    # copy
    # creates
    o += PWH.decrypt()
    # exclude
    # extra_opts
    o += PWH.group()
    # include 
    # io_buffer_size
    # keep_newer
    # list_files
    o += PWH.mode()
    o += PWH.owner()
    # remote_src
    o += PWH.seThings()
    o += PWH.unsafe_writes()
    o += PWH.validate_certs()

    return o

def uri():
    #uri module
    o = ""
    o += PWH.playStart("uri")
    # url

    print("https://docs.ansible.com/ansible/latest/collections/ansible/builtin/uri_module.html#parameter-attributes")
    o += PWH.attributes("Do you want the result to have any specific attributes")
    # body 
    # body_format 
    # ca_path 
    # ciphers 
    # client_cert 
    # client_key 
    # creates 
    # decompress 
    # dest 
    # follow_redirects 
    # force
    # force_basic_auth 
    o += PWH.group()
    # headers 
    # http_agent 
    # method 
    o += PWH.mode()
    o += PWH.owner()
    # remote_src 
    # removes 
    # return_content 
    o += PWH.seThings() 
    # src
    # status_code 
    # timeout 
    # unix_socket 
    # unredirected_headers
    o += PWH.unsafe_writes()
    # url_password 
    # url_username 
    # use_gssapi 
    # use_netrc
    # use_proxy 
    o += PWH.validate_certs()

    return o

def user():
    #user module
    o = ""
    o += PWH.playStart("user")
    #

    # append 
    # authorization 
    # comment 
    # create_home 
    # expires 
    # force 
    # generate_ssh_key 
    o += PWH.group()
    # groups 
    # hidden 
    # home 
    # local 
    # login_class
    # move_home 
    # non_unique 
    # password 
    # password_expire_max 
    # password_expire_min 
    # password_lock 
    # profile 
    # remove 
    # role 
    o += PWH.seuser()
    # shell
    # skeleton 
    # ssh_key_bits 
    # ssh_key_comment 
    # ssh_key_file 
    # ssh_key_passphrase 
    # ssh_key_type 
    o += PWH.stateAbsentPresent("Do you want the user to be removed from the system")
    # system 
    # uid 
    # umask 
    # update_password

    return o

def validate_argument_spec():
    #validate_argument_spec module
    o = ""
    o += PWH.playStart("validate_argument_spec")
    # argument_spec 
    #o += "\t\targument_spec: " + input("") + "\n"

    # provided_arguments

    return o

def wait_for():
    #wait_for module
    o = ""
    o += PWH.playStart("wait_for")

    # active_connection_states 
    # connect_timeout 
    # delay 
    # exclude_hosts 
    # host 
    o += PWH.msg("Do you want to set a custom message for failing to meet the required conditions?")
    # path 
    # port 
    # search_regex 
    # sleep 
    o += PWH.ans_from_list("state", ["absent", "drained", "present", "started", "stopped"], "wait_for")
    # timeout

    return o

def wait_for_connection():
    #wait_for_connection module
    o = ""
    o += PWH.playStart("wait_for_connection")

    # connect_timeout
    # delay 
    # sleep 
    # timeout

    return o

def yum():
    #yum module
    o = ""
    o += PWH.playStart("yum")

    # allow_downgrade 
    # autoremove 
    # bugfix 
    # cacheonly 
    # conf_file 
    # disable_excludes 
    # disable_gpg_check 
    # disable_plugin 
    # disablerepo 
    # download_dir 
    # enable_plugin 
    # enablerepo 
    # exclude 
    # install_repository
    # install_weak_deps 
    # install_root 
    # list 
    # lock_timeout 
    # name releasever 
    # security 
    # skip_broken 
    # sslverify 
    o += PWH.ans_from_list("state", ["absent", "installed", "latest", "present", "removed"], "yum")
    o += PWH.update_cache()
    # update_only 
    # use_backend 
    o += PWH.validate_certs()

    return o

def yum_repository():
    #yum_repository module
    o = ""
    o += PWH.playStart("yum_repository")
    # name

    # async 
    print("https://docs.ansible.com/ansible/latest/collections/ansible/builtin/yum_repository_module.html#parameter-attributes")
    o += PWH.attributes("Do you want any specific attributes for the created yum repository")
    # bandwidth
    # baseurl
    # cost
    # deltarpm_metadata_percentage
    # deltarpm_percentage
    # description
    # enabled
    # enablegroups
    # excludes
    # failovermethod
    # file
    # gpgcakey
    # gpgcheck
    # gpgkey
    o += PWH.group()
    # http_caching
    # include
    # includepkgs
    # ip_resolve
    # keepalive
    # keepcache
    # metadata_expire
    # metadata_expire_filter
    # metalink
    # mirrorlist
    # mirrorlist_expire
    o += PWH.mode()
    # module_hotfixes
    o += PWH.owner()
    # password
    # priority
    # protect
    # proxy
    # proxy_password
    # proxy_username
    # repo_gpgcheck
    # reposdir
    # retries
    # s3_enabled
    o += PWH.seThings()
    # skip_if_unavailable
    # ssl_check_cert_permissions
    # sslcacert
    # sslclientcert
    # sslclientkey
    # sslverify
    o += PWH.stateAbsentPresent("Do you want the repo file to be absent")
    # throttle
    # timeout
    # ui_repoid_vars
    o += PWH.unsafe_writes()
    # username

    return o

funcs = {'add_host':add_host, 'apt':apt, 'apt_key':apt_key, 'apt_repository':apt_repository, 'assemble':assemble, 'assert':Assert, 'async_status':async_status, 'blockinfile':blockinfile, 'command':command, 'copy':copy, 'cron':cron, 'debconf':debconf, 'debug':debug, 'dnf':dnf, 'dpkg_selections':dpkg_selections, 'expect':expect, 'fail':fail, 'fetch':fetch, 'file':file, 'gather_facts':gather_facts, 'get_url':get_url, 'getent':getent, 'git':git, 'group':group, 'group_by':group_by, 'hostname':hostname, 'import_playbook':import_playbook, 'import_role':import_role, 'import_tasks':import_tasks, 'include':include, 'include_role':include_role, 'include_tasks':include_tasks, 'include_vars':include_vars, 'iptables':iptables, 'known_hosts':known_hosts, 'lineinfile':lineinfile, 'meta':meta, 'package':package, 'package_facts':package_facts, 'pause':pause, 'ping':ping, 'pip':pip, 'raw':raw, 'reboot':reboot, 'replace':replace, 'rpm_key':rpm_key, 'script':script, 'service':service, 'service_facts':service_facts, 'set_fact':set_fact, 'set_stats':set_stats, 'setup':setup, 'shell':shell, 'slurp':slurp, 'stat':stat, 'subversion':subversion, 'systemd':systemd, 'systemd_service':systemd_service, 'sysvinit':sysvinit, 'tempfile':tempfile, 'template':template, 'unarchive':unarchive, 'uri':uri, 'user':user, 'validate_argument_spec':validate_argument_spec, 'wait_for':wait_for, 'wait_for_connection':wait_for_connection, 'yum':yum, 'yum_repository':yum_repository}