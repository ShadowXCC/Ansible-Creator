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
    o += "\t\tname: " + input("\nExample: \"ip:portnumber\"\n" + "Enter the hostname/IP address you are adding a host to: ") + "\n"
    
    if input("Would you like to add the \"groups\" parameter to this play? (Y/N): ").lower() == "y":
        o += "\t\tgroups:"
        groups = input("Enter the group name(s), with spaces separating multiple group names: ")
        if " " in groups:
            o += "\n"
            gList = groups.split()
            for item in gList:
                o += "\t\t- " + item + "\n"
        else:
            o += groups

    if input("Does the host you need to reach exist through a tunnel (Y/N): ").lower() == "y":
        o += "\t\tansible_host: " + input("What is the hostname of the tunnel? ") + "\n"
        o += "\t\tansible_port: " + input("What is the port number of the tunnel? ") + "\n"

    if input("Do you want this play to loop (Y/N): ").lower() == "y":
        o += "\tloop: " + input("How many times do you want this play to loop: ")

    return o

def apt():
    o = ""
    o += PWH.playStart("apt")
    o += "\t\tname:"
    packages = input("Enter the name(s) of the package(s), with spaces separating multiple package names: ")
    if " " in packages:
        o += "\n"
        pList = packages.split()
        for item in pList:
            o += "\t\t- " + item + "\n"
    else:
        o += packages

    
    if input("Do you need more specialized options for the \"apt\" task, 25 questions (Y/N)? ").lower() == "y":
        if input("Do you want to specify a required state for these packages (Y/N)? ").lower() == "y":
            o += "\t\tstate: "

            a = True
            while a:
                print(menus.aptStatesMenu())
                choice = input("Choice: ")
                if choice == "1":
                    o += "present"
                    a = False
                elif choice == "2":
                    o += "absent"
                    a = False
                elif choice == "3":
                    o += "latest"
                    a = False
                elif choice == "4":
                    o += "build-dep"
                    a = False
                elif choice == "5":
                    o += "fixed"
                    a = False
                else:
                    print("Incorrect Input, please try again.")
            o += "\n"

        if input("Do you need to change the version of a held package (Y/N)? ").lower() == "y":
            o += "\t\tallow_change_held_packages: true\n"
        if input("Do you want to allow the specified packages to downgrade if specified (Y/N)? ").lower() == "y":
            o += "\t\tallow_downgrade: true\n"
        if input("Do you want packages that aren't/cannot be authenticated to still be installed (Y/N)? ").lower() == "y":
            o += "\t\tallow_unauthenticated: true\n"
        if input("Do you want to autoclean the local repository (Y/N)? ").lower() == "y":
            o += "\t\tautoclean: true\n"
        if input("Do you want to autoremove unnused packages (Y/N)? ").lower() == "y":
            o += "\t\tautoremove: true\n"
        if input("Do you want to update the apt cache if older than a set number of seconds (Y/N)? ").lower() == "y":
            o += "\t\tcache_valid_time: " + input("How many seconds is too old for the apt cache (Seconds): ") + "\n"
        if input("Do you want to clear out the local repository of package files (Y/N)? ").lower() == "y":
            o += "\t\tclean: true\n"
        if input("Do you want to provide a path to a \".deb\" file on the remote machine (Y/N)? ").lower() == "y":
            o += "\t\tdeb: " + input("What is the path: ") + "\n" # This option controls the default input to the policy engine. It creates a default pin at priority 990 using the specified release string. The preferences file may further override this setting. In short, this option lets you have simple control over which distribution packages will be retrieved from. Some common examples might be -t '2.1*' or -t unstable.
        if input("-t option for \"apt\"(Y/N)? ").lower() == "y":
            o += "\t\tdefault_release: " + input("How high of a priority is this? ") + "\n"
        if input("Do you need dpkg options (Y/N)? ").lower() == "y":
            o += "\t\tdpkg_options: " + input("dpkg options: ") + "\n"
        if input("Do you want to guarantee no packages will be auto removed (Y/N)? ").lower() == "y":
            o += "\t\tfail_on_autoremove: true\n"
        if input("Do you want to force the install to install no matter what (Y/N)? ").lower() == "y":
            o += "\t\tforce: true\n"
        if input("Do you want to use \"apt-get\" instead of \"apt\" (Y/N)? ").lower() == "y":
            o += "\t\tforce_apt_get: true\n"
        if input("Do you want to install recommended packages (Y/N)? ").lower() == "y":
            o += "\t\tinstall_recommends: y\n"
        if input("Do you want to set how long to wait to aquire a lock on the apt db (Y/N)? ").lower() == "y":
            o += "\t\tlock_timeout: " + input("Enter a time in seconds: ") + "\n"
        if input("Do you only want to upgrade packages if they are already installed (Y/N)? ").lower() == "y":
            o += "\t\tonly_upgrade: true\n"
        if input("Do you want to force the exit code of \"/usr/sbin/policy-rc.d\" (Y/N)? ").lower() == "y":
            o += "\t\tpolicy_rc_d: " + input("What exit code do you want forced: ") + "\n"
        if input("If the state is set to absent, do you want to force a purge of configuration files (Y/N)? ").lower() == "y":
            o += "\t\tpurge: true\n"
        if input("Do you want to update the apt cache (Y/N)? ").lower() == "y":
            o += "\t\tupdate_cache: true\n"
        o += PWH.update_cache_retries()
        o += PWH.update_cache_retry_max_delay()
        if input("Do you want to upgrade (Y/N)? ").lower() == "y":
            o += "\t\tupgrade: "

            a = True
            while a:
                print(menus.aptUpgradeMenu())
                choice = input("Choice: ")
                if choice == "1":
                    o += "no"
                    a = False
                elif choice == "2":
                    o += "yes"
                    a = False
                elif choice == "3":
                    o += "safe"
                    a = False
                elif choice == "4":
                    o += "full"
                    a = False
                elif choice == "5":
                    o += "dist"
                    a = False
                else:
                    print("Incorrect Input, please try again.")
            o += "\n"

    return o

def apt_key():
    o = ""
    o += PWH.playStart("apt_key")
    if input("Do you want to specify raw keyfile contents to add to the keyring (Y/N)? ").lower() == "y":
        o += "\t\tdata: " + input("Enter the raw keyfile data: ") + "\n"
    if input("Do you want to specify the path to a keyfile on the remote machine (Y/N)? ").lower() == "y":
        o += "\t\tfile: " + input("Enter the keyfile's path on the remote machine: ") + "\n"
    if input("Do you want to specify the path to the keyring file on the remote machine, should be in \"/etc/apt/trusted.gpg.d/\" (Y/N)? ").lower() == "y":
        o += "\t\tkeyring: " + input("Enter the full path to the keyring file: ") + "\n"
    if input("Do you want to specify a keyserver (Y/N)? ").lower() == "y":
        o += "\t\tkeyserver: " + input("Enter the URL of the keyserver: ") + "\n"
    h = PWH.stateAbsentPresent()
    if h != "":
        o += h
        o += "\t\tid: " + input("Enter the key's identifier: ") + "\n"
    elif input("Do you want to specify a key identifier (Y/N)? ").lower() == "y":
        o += "\t\tid: " + input("Enter the key's identifier: ") + "\n"
    if input("Do you want to specify a URL to retrieve the key from (Y/N)? ").lower() == "y":
        o += "\t\turl: " + input("What is the URL to retrieve the key from? ") + "\n"
    o += PWH.validate_certs()

    return o

def apt_repository():
    o = ""
    o += PWH.playStart("apt_repository")

    if input("(Y/N)? ").lower() == "y":
        o += "\t\t: \n"

    print("\nHelp: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_repository_module.html#parameters")
    o += "\t\trepo: " + input("From the above link, what is the source string for the repository: ") + "\n"
    if input("Do you want to override the distribution codename used for PPA repositories (Y/N)? ").lower() == "y":
        o += "\t\tcodename: " + input("Enter the distribution codename: ") + "\n"
    if input("Do you want to specify the filename of the added repository (Y/N)? ").lower() == "y":
        o += "\t\tfilename: " + input("Enter the filename (without any file extension): ") + "\n"
    if input("Do you want to automatically try to install the Python apt library (Y/N)? ").lower() == "y":
        o += "\t\tinstall_python_apt: false\n"
    if input("Do you want to set a mode/permission octal for this repo (Y/N)? ").lower() == "y":
        o += "\t\tmode: " + input("Enter the mode/permission octal for this repo (ex: 0644): ") + "\n"
    
    o += PWH.stateAbsentPresent()
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

    if input("Do you need more specialized options for the \"assemble\" task, 13 questions (Y/N)? ").lower() == "y":

        print("https://docs.ansible.com/ansible/latest/collections/ansible/builtin/assemble_module.html#parameter-attributes")
        o += PWH.attributes("Do you want to set any attributes for the resulting file")
        o += PWH.backup()
        o += PWH.decrypt()
        if input("Do you want to specify a delimiter to separate file contents (Y/N)? ").lower() == "y":
            o += "\t\tdeliminiter: " + input("What delimiter do you want to use: ") + "\n"
        o += PWH.group()
        if input("Do you want this operation to include hidden files in the assembling (Y/N)? ").lower() == "y":
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
    if input("Do you want to specify a fail message (Y/N)? ").lower() == "y":
        o += "\t\tfail_msg: " + input("Enter the fail message: ") + "\n"
    if input("Do you want to specify a success message (Y/N)? ").lower() == "y":
        o += "\t\tsuccess_msg: " + input("Enter the success message: ") + "\n"
    if input("(Y/N)? ").lower() == "y":
        o += "\t\t: \n"

    return o

def async_status():
    o = ""
    o += PWH.playStart("async_status")

    o += "\t\tjid: " + input("What is the job or task identifier for the asynchronous task: ") + "\n"
    if input("Do you want to also clean up the async job cache for the specified ID (Y/N)? ").lower() == "y":
        o += "\t\tmode: cleanup\n"
    return o

def blockinfile():
    #blockinfile module
    o = ""
    o += PWH.playStart("blockinfile")

    # path

    if input("(Y/N)? ").lower() == "y":
        o += "\t\t: \n"

    print("https://docs.ansible.com/ansible/latest/collections/ansible/builtin/blockinfile_module.html#parameter-attributes")
    o += PWH.attributes("Do you want to set any attributes for the file being worked on")
    o += PWH.backup()
    # block
    # create
    o += PWH.group()
    # insertafter
    # insertbefore
    # marker
    # marker_begin
    # marker_end
    o += PWH.mode()
    o += PWH.owner()
    o += PWH.seThings()
    o += PWH.stateAbsentPresent()
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
    o += PWH.stateAbsentPresent()
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
    #debug module
    o = ""
    o += PWH.playStart("debug")

    # msg var verbosity

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
    #dpkg_selections module
    o = ""
    o += PWH.playStart("dpkg_selections")

    # name
    # selection

    return o

def expect():
    #expect module
    o = ""
    o += PWH.playStart("expect")
    # command responses

    # chdir
    # creates
    # echo
    # removes
    # timeout

    return o

def fail():
    #fail module
    o = ""
    o += PWH.playStart("fail")

    # msg

    return o

def fetch():
    #fetch module
    o = ""
    o += PWH.playStart("fetch")

    # dest src

    # fail_on_missing flat validate_checksum

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
    #gather_facts module
    o = ""
    o += PWH.playStart("gather_facts")

    #parallel

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

    # fail_key key service split

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
    #group module
    o = ""
    o += PWH.playStart("group")
    # name

    # gid 
    # local 
    # non_unique 
    o += PWH.stateAbsentPresent()
    # system

    return o

def group_by():
    #group_by module
    o = ""
    o += PWH.playStart("group_by")

    # key
    # parents

    return o

def hostname():
    #hostname module
    o = ""
    o += PWH.playStart("hostname")

    # name
    # use

    return o

def import_playbook():
    #import_playbook module
    o = ""
    o += PWH.playStart("import_playbook")

    #free-form

    return o

def import_role():
    #import_role module
    o = ""
    o += PWH.playStart("import_role")
    # name

    # allow_duplicates defaults_from handlers_from rolespec_validate tasks_from vars_from

    return o

def import_tasks():
    #import_tasks module
    o = ""
    o += PWH.playStart("import_tasks")

    # file free-form

    return o

def include():
    #include module
    o = ""
    o += PWH.playStart("include")

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

    # apply file free-form

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
    o += PWH.stateAbsentPresent()
    # syn
    # table
    # tcp_flags(flags flags_set)
    # to_destination to_ports
    # to_source
    # uid_owner
    # wait

    return o

def known_hosts():
    #known_hosts module
    o = ""
    o += PWH.playStart("known_hosts")

    # hash_host 
    # key 
    # name 
    # path 
    o += PWH.stateAbsentPresent()

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
    o += PWH.stateAbsentPresent()
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
    #package module
    o = ""
    o += PWH.playStart("package")

    # name
    o += PWH.state(["present", "absent"])

    # use

    return o

def package_facts():
    #package_facts module
    o = ""
    o += PWH.playStart("package_facts")

    # manager 
    # strategy

    return o

def pause():
    #pause module
    o = ""
    o += PWH.playStart("pause")

    # echo 
    # prompt 
    # minutes 
    # seconds

    return o

def ping():
    #ping module
    o = ""
    o += PWH.playStart("ping")

    # data

    return o

def pip():
    #pip module
    o = ""
    o += PWH.playStart("pip")

    # chdir 
    # editable
    # executable 
    # extra_args 
    # name 
    # requirements 
    o += PWH.state(["absent", "forcereinstall", "latest", "present"])
    # umask 
    # version 
    # virtualenv 
    # virtualenv_command
    # virtualenv_python 
    # virtualenv_site_packages

    return o

def raw():
    #raw module
    o = ""
    o += PWH.playStart("raw")

    # free_form
    # executable

    return o

def reboot():
    #reboot module
    o = ""
    o += PWH.playStart("reboot")

    # boot_time_command 
    # connect_timeout 
    # msg 
    # post_reboot_delay 
    # reboot_command 
    # reboot_timeout 
    # search_paths 
    # test_command
 
    return o

def replace():
    #replace module
    o = ""
    o += PWH.playStart("replace")
    # path regexp

    # after 
    print("https://docs.ansible.com/ansible/latest/collections/ansible/builtin/replace_module.html#parameter-attributes")
    o += PWH.attributes()
    o += PWH.backup()
    # before 
    # encoding 
    o += PWH.group()
    o += PWH.mode()
    # others 
    o += PWH.owner() 
    # replace 
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
    o += PWH.stateAbsentPresent()
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
    o += PWH.state(rrssList)
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
    #slurp module
    o = ""
    o += PWH.playStart("slurp")

    # src

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
    o += PWH.state(rrssList)

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
    o += PWH.state(rrssList)

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
    o += PWH.state(rrssList)

    return o

def tempfile():
    #tempfile module
    o = ""
    o += PWH.playStart("tempfile")

    # path 
    # prefix 
    o += PWH.state(["directory", "file"])
    # suffix

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
    o += PWH.stateAbsentPresent()
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
    # msg 
    # path 
    # port 
    # search_regex 
    # sleep 
    o += PWH.state(["absent", "drained", "present", "started", "stopped"])
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
    o += PWH.state(["absent", "installed", "latest", "present", "removed"])
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
    o += PWH.stateAbsentPresent()
    # throttle
    # timeout
    # ui_repoid_vars
    o += PWH.unsafe_writes()
    # username

    return o

























def runas():
    #runas become
    o = ""
    o += PWH.playStart("runas")
    # become_user 

    # become_flags become_pass 
    
    return o

def su():
    #su become
    o = ""
    o += PWH.playStart("su")

    # become_exe 
    # become_flags 
    # become_pass 
    # become_user 
    # prompt_l10n

    return o

def sudo():
    #sudo become
    o = ""
    o += PWH.playStart("sudo")

    # become_exe 
    # become_flags 
    # become_pass 
    # become_user

    return o

def jsonfile():
    #jsonfile cache
    o = ""
    o += PWH.playStart("jsonfile")
    # _uri

    # _prefix 
    # _timeout

    return o

def memory():
    #memory cache
    o = ""
    o += PWH.playStart("memory")

    # no things

    return o

def default():
    #default callback
    o = ""
    o += PWH.playStart("default")

    # check_mode_markers 
    # display_failed_stderr 
    # display_ok_hosts 
    # display_skipped_hosts 
    # pretty_results result_format 
    # show_custom_stats 
    # show_per_host_start 
    # show_task_path_on_failure 

    return o

def junit():
    #junit callback
    o = ""
    o += PWH.playStart("junit")

    # fail_on_change 
    # fail_on_ignore 
    # hide_task_arguments 
    # include_setup_tasks_in_report 
    # output_dir 
    # replace_out_of_tree_path
    # task_class 
    # task_relative_path 
    # test_case_prefix

    return o

def minimal():
    #minimal callback
    o = ""
    o += PWH.playStart("minimal")

    # pretty_results
    # result_format

    return o

def oneline():
    #oneline callback
    o = ""
    o += PWH.playStart("oneline")

    # no things

    return o

def tree():
    #tree callback
    o = ""
    o += PWH.playStart("tree")

    # directory 

    return o

def local():
    #local connection
    o = ""
    o += PWH.playStart("local")

    # 

    return o

def paramiko_ssh():
    #paramiko_ssh connection
    o = ""
    o += PWH.playStart("paramiko_ssh")



    return o

def psrp():
    #psrp connection
    o = ""
    o += PWH.playStart("psrp")



    return o

def ssh():
    #ssh connection
    o = ""
    o += PWH.playStart("ssh")



    return o

def winrm():
    #winrm connection
    o = ""
    o += PWH.playStart("winrm")



    return o

def b64decode():
    #b64decode filter
    o = ""
    o += PWH.playStart("b64decode")



    return o

def b64encode():
    #b64encode filter
    o = ""
    o += PWH.playStart("b64encode")



    return o

def basename():
    #basename filter
    o = ""
    o += PWH.playStart("basename")



    return o

def bool():
    #bool filter
    o = ""
    o += PWH.playStart("bool")
    return o

def checksum():
    #checksum filter
    o = ""
    o += PWH.playStart("checksum")
    return o

def combinations():
    #combinations filter
    o = ""
    o += PWH.playStart("combinations")
    return o

def combine():
    #combine filter
    o = ""
    o += PWH.playStart("combine")
    return o

def comment():
    #comment filter
    o = ""
    o += PWH.playStart("comment")
    return o

def dict2items():
    #dict2items filter
    o = ""
    o += PWH.playStart("dict2items")
    return o

def difference():
    #difference filter
    o = ""
    o += PWH.playStart("difference")
    return o

def dirname():
    #dirname filter
    o = ""
    o += PWH.playStart("dirname")
    return o

def expanduser():
    #expanduser filter
    o = ""
    o += PWH.playStart("expanduser")
    return o

def expandvars():
    #expandvars filter
    o = ""
    o += PWH.playStart("expandvars")
    return o

def extract():
    #extract filter
    o = ""
    o += PWH.playStart("extract")
    return o

def fileglob():
    #fileglob filter
    o = ""
    o += PWH.playStart("fileglob")
    return o

def flatten():
    #flatten filter
    o = ""
    o += PWH.playStart("flatten")
    return o

def from_json():
    #from_json filter
    o = ""
    o += PWH.playStart("from_json")
    return o

def from_yaml():
    #from_yaml filter
    o = ""
    o += PWH.playStart("from_yaml")
    return o

def from_yaml_all():
    #from_yaml_all filter
    o = ""
    o += PWH.playStart("from_yaml_all")
    return o

def hash():
    #hash filter
    o = ""
    o += PWH.playStart("hash")
    return o

def human_readable():
    #human_readable filter
    o = ""
    o += PWH.playStart("human_readable")
    return o

def human_to_bytes():
    #human_to_bytes filter
    o = ""
    o += PWH.playStart("human_to_bytes")
    return o

def intersect():
    #intersect filter
    o = ""
    o += PWH.playStart("intersect")
    return o

def items2dict():
    #items2dict filter
    o = ""
    o += PWH.playStart("items2dict")
    return o

def log():
    #log filter
    o = ""
    o += PWH.playStart("log")
    return o

def mandatory():
    #mandatory filter
    o = ""
    o += PWH.playStart("mandatory")
    return o

def md5():
    #md5 filter
    o = ""
    o += PWH.playStart("md5")
    return o

def password_hash():
    #password_hash filter
    o = ""
    o += PWH.playStart("password_hash")
    return o

def path_join():
    #path_join filter
    o = ""
    o += PWH.playStart("path_join")
    return o

def permutations():
    #permutations filter
    o = ""
    o += PWH.playStart("permutations")
    return o

def pow():
    #pow filter
    o = ""
    o += PWH.playStart("pow")
    return o

def product():
    #product filter
    o = ""
    o += PWH.playStart("product")
    return o

def quote():
    #quote filter
    o = ""
    o += PWH.playStart("quote")
    return o

def random():
    #random filter
    o = ""
    o += PWH.playStart("random")
    return o

def realpath():
    #realpath filter
    o = ""
    o += PWH.playStart("realpath")
    return o

def regex_escape():
    #regex_escape filter
    o = ""
    o += PWH.playStart("regex_escape")
    return o

def regex_findall():
    #regex_findall filter
    o = ""
    o += PWH.playStart("regex_findall")
    return o

def regex_replace():
    #regex_replace filter
    o = ""
    o += PWH.playStart("regex_replace")
    return o

def regex_search():
    #regex_search filter
    o = ""
    o += PWH.playStart("regex_search")
    return o

def rekey_on_member():
    #rekey_on_member filter
    o = ""
    o += PWH.playStart("rekey_on_member")
    return o

def relpath():
    #relpath filter
    o = ""
    o += PWH.playStart("relpath")
    return o

def root():
    #root filter
    o = ""
    o += PWH.playStart("root")
    return o

def sha1():
    #sha1 filter
    o = ""
    o += PWH.playStart("sha1")
    return o

def shuffle():
    #shuffle filter
    o = ""
    o += PWH.playStart("shuffle")
    return o

def splittext():
    #splittext filter
    o = ""
    o += PWH.playStart("splittext")
    return o

def strftime():
    #strftime filter
    o = ""
    o += PWH.playStart("strftime")
    return o

def subelements():
    #subelements filter
    o = ""
    o += PWH.playStart("subelements")
    return o

def symmetric_difference():
    #symmetric_difference filter
    o = ""
    o += PWH.playStart("symmetric_difference")
    return o

def ternary():
    #ternary filter
    o = ""
    o += PWH.playStart("ternary")
    return o

def to_datetime():
    #to_datetime filter
    o = ""
    o += PWH.playStart("to_datetime")
    return o

def to_json():
    #to_json filter
    o = ""
    o += PWH.playStart("to_json")
    return o

def to_nice_json():
    #to_nice_json filter
    o = ""
    o += PWH.playStart("to_nice_json")
    return o

def to_nice_yaml():
    #to_nice_yaml filter
    o = ""
    o += PWH.playStart("to_nice_yaml")
    return o

def to_uuid():
    #to_uuid filter
    o = ""
    o += PWH.playStart("to_uuid")
    return o

def to_yaml():
    #to_yaml filter
    o = ""
    o += PWH.playStart("to_yaml")
    return o

def type_debug():
    #type_debug filter
    o = ""
    o += PWH.playStart("type_debug")
    return o

def union():
    #union filter
    o = ""
    o += PWH.playStart("union")
    return o

def unique():
    #unique filter
    o = ""
    o += PWH.playStart("unique")
    return o

def unvault():
    #unvault filter
    o = ""
    o += PWH.playStart("unvault")
    return o

def urlsplit():
    #urlsplit filter
    o = ""
    o += PWH.playStart("urlsplit")
    return o

def vault():
    #vault filter
    o = ""
    o += PWH.playStart("vault")
    return o

def win_basename():
    #win_basename filter
    o = ""
    o += PWH.playStart("win_basename")
    return o

def win_dirname():
    #win_dirname filter
    o = ""
    o += PWH.playStart("win_dirname")
    return o

def win_splitdrive():
    #win_splitdrive filter
    o = ""
    o += PWH.playStart("win_splitdrive")
    return o

def zip():
    #zip filter
    o = ""
    o += PWH.playStart("zip")
    return o

def zip_longest():
    #zip_longest filter
    o = ""
    o += PWH.playStart("zip_longest")
    return o

def advanced_host_list():
    #advanced_host_list inventory
    o = ""
    o += PWH.playStart("advanced_host_list")
    return o

def auto():
    #auto inventory
    o = ""
    o += PWH.playStart("auto")
    return o

def constructed():
    #constructed inventory
    o = ""
    o += PWH.playStart("constructed")
    return o

def generator():
    #generator inventory
    o = ""
    o += PWH.playStart("generator")
    return o

def host_list():
    #host_list inventory
    o = ""
    o += PWH.playStart("host_list")
    return o

def ini():
    #ini inventory
    o = ""
    o += PWH.playStart("ini")
    return o

def script():
    #script inventory
    o = ""
    o += PWH.playStart("script")
    return o

def toml():
    #toml inventory
    o = ""
    o += PWH.playStart("toml")
    return o

def yaml():
    #yaml inventory
    o = ""
    o += PWH.playStart("yaml")
    return o


def config():
    #config lookup
    o = ""
    o += PWH.playStart("config")
    return o

def csvfile():
    #csvfile lookup
    o = ""
    o += PWH.playStart("csvfile")
    return o

def dict():
    #dict lookup
    o = ""
    o += PWH.playStart("dict")
    return o

def env():
    #env lookup
    o = ""
    o += PWH.playStart("env")
    return o

def file():
    #file lookup
    o = ""
    o += PWH.playStart("file")
    return o

def fileglob():
    #fileglob lookup
    o = ""
    o += PWH.playStart("fileglob")
    return o

def first_found():
    #first_found lookup
    o = ""
    o += PWH.playStart("first_found")
    return o

def indexed_items():
    #indexed_items lookup
    o = ""
    o += PWH.playStart("indexed_items")
    return o

def ini():
    #ini lookup
    o = ""
    o += PWH.playStart("ini")
    return o

def inventory_hostnames():
    #inventory_hostnames
    o = ""
    o += PWH.playStart("inventory_hostnames")
    return o

def lines():
    #lines lookup
    o = ""
    o += PWH.playStart("lines")
    return o

def list():
    #list lookup
    o = ""
    o += PWH.playStart("list")
    return o

def nested():
    #nested lookup
    o = ""
    o += PWH.playStart("nested")
    return o

def password():
    #password lookup
    o = ""
    o += PWH.playStart("password")
    return o

def pipe():
    #pipe lookup
    o = ""
    o += PWH.playStart("pipe")
    return o

def random_choice():
    #random_choice lookup
    o = ""
    o += PWH.playStart("random_choice")
    return o

def sequence():
    #sequence lookup
    o = ""
    o += PWH.playStart("sequence")
    return o

def subelements():
    #subelements lookup
    o = ""
    o += PWH.playStart("subelements")
    return o

def template():
    #template lookup
    o = ""
    o += PWH.playStart("template")
    return o

def together():
    #together lookup
    o = ""
    o += PWH.playStart("together")
    return o

def unvault():
    #unvault lookup
    o = ""
    o += PWH.playStart("unvault")
    return o

def url():
    #url lookup
    o = ""
    o += PWH.playStart("url")
    return o

def varnames():
    #varnames lookup
    o = ""
    o += PWH.playStart("varnames")
    return o

def vars():
    #vars lookup 
    o = ""
    o += PWH.playStart("vars")
    return o


def cmd():
    #cmd shell
    o = ""
    o += PWH.playStart("cmd")
    return o

def powershell():
    #powershell shell
    o = ""
    o += PWH.playStart("powershell")
    return o

def sh():
    #sh shell
    o = ""
    o += PWH.playStart("sh")
    return o


def debug():
    #debug strategy
    o = ""
    o += PWH.playStart("debug")
    return o

def free():
    #free strategy
    o = ""
    o += PWH.playStart("free")
    return o

def host_pinned():
    #host_pinned strategy
    o = ""
    o += PWH.playStart("host_pinned")
    return o

def linear():
    #linear strategy
    o = ""
    o += PWH.playStart("linear")
    return o


def abs():
    #abs all test
    o = ""
    o += PWH.playStart("abs")
    return o

def any():
    #any test
    o = ""
    o += PWH.playStart("any")
    return o

def changed():
    #changed test
    o = ""
    o += PWH.playStart("changed")
    return o

def contains():
    #contains test
    o = ""
    o += PWH.playStart("contains")
    return o

def directory():
    #directory test
    o = ""
    o += PWH.playStart("directory")
    return o

def exists():
    #exists test
    o = ""
    o += PWH.playStart("exists")
    return o

def failed():
    #failed test
    o = ""
    o += PWH.playStart("failed")
    return o

def falsy():
    #falsy test
    o = ""
    o += PWH.playStart("falsy")
    return o

def file():
    #file test
    o = ""
    o += PWH.playStart("file")
    return o

def finished():
    #finished test
    o = ""
    o += PWH.playStart("finished")
    return o

def link():
    #link test
    o = ""
    o += PWH.playStart("link")
    return o

def link_exists():
    #link_exists test
    o = ""
    o += PWH.playStart("link_exists")
    return o

def match():
    #match test
    o = ""
    o += PWH.playStart("match")
    return o

def mount():
    #mount test
    o = ""
    o += PWH.playStart("mount")
    return o

def nan():
    #nan test
    o = ""
    o += PWH.playStart("nan")
    return o

def reachable():
    #reachable test
    o = ""
    o += PWH.playStart("reachable")
    return o

def regex():
    #regex test
    o = ""
    o += PWH.playStart("regex")
    return o

def same_file():
    #same_file test
    o = ""
    o += PWH.playStart("same_file")
    return o

def search():
    #search test
    o = ""
    o += PWH.playStart("search")
    return o

def skipped():
    #skipped test
    o = ""
    o += PWH.playStart("skipped")
    return o

def started():
    #started test
    o = ""
    o += PWH.playStart("started")
    return o

def subset():
    #subset test
    o = ""
    o += PWH.playStart("subset")
    return o

def success():
    #success test
    o = ""
    o += PWH.playStart("success")
    return o

def superset():
    #superset test
    o = ""
    o += PWH.playStart("superset")
    return o

def truthy():
    #truthy test
    o = ""
    o += PWH.playStart("truthy")
    return o

def unreachable():
    #unreachable test
    o = ""
    o += PWH.playStart("unreachable")
    return o

def uri():
    #uri test
    o = ""
    o += PWH.playStart("uri")
    return o

def url():
    #url test
    o = ""
    o += PWH.playStart("url")
    return o

def urn():
    #urn test
    o = ""
    o += PWH.playStart("urn")
    return o

def vault_encrypted():
    #vault_encrypted test
    o = ""
    o += PWH.playStart("vault_encrypted")
    return o

def version():
    #version test
    o = ""
    o += PWH.playStart("version")
    return o

def host_group_vars():
    #host_group_vars test
    o = ""
    o += PWH.playStart("host_group_vars")
    return o

funcs = {'add_host':add_host, 'apt':apt, 'apt_key':apt_key, 'apt_repository':apt_repository, 'assemble':assemble, 'assert':Assert, 'async_status':async_status, 'blockinfile':blockinfile, 'command':command, 'copy':copy, 'cron':cron, 'debconf':debconf, 'debug':debug, 'dnf':dnf, 'dpkg_selections':dpkg_selections, 'expect':expect, 'fail':fail, 'fetch':fetch, 'file':file, 'gather_facts':gather_facts, 'get_url':get_url, 'getent':getent, 'git':git, 'group':group, 'group_by':group_by, 'hostname':hostname, 'import_playbook':import_playbook, 'import_role':import_role, 'import_tasks':import_tasks, 'include':include, 'include_role':include_role, 'include_tasks':include_tasks, 'include_vars':include_vars, 'iptables':iptables, 'known_hosts':known_hosts, 'lineinfile':lineinfile, 'meta':meta, 'package':package, 'package_facts':package_facts, 'pause':pause, 'ping':ping, 'pip':pip, 'raw':raw, 'reboot':reboot, 'replace':replace, 'rpm_key':rpm_key, 'script':script, 'service':service, 'service_facts':service_facts, 'set_fact':set_fact, 'set_stats':set_stats, 'setup':setup, 'shell':shell, 'slurp':slurp, 'stat':stat, 'subversion':subversion, 'systemd':systemd, 'systemd_service':systemd_service, 'sysvinit':sysvinit, 'tempfile':tempfile, 'template':template, 'unarchive':unarchive, 'uri':uri, 'user':user, 'validate_argument_spec':validate_argument_spec, 'wait_for':wait_for, 'wait_for_connection':wait_for_connection, 'yum':yum, 'yum_repository':yum_repository, 'runas':runas, 'su':su, 'sudo':sudo, 'jsonfile':jsonfile, 'memory':memory, 'default':default, 'junit':junit, 'minimal':minimal, 'oneline':oneline, 'tree':tree, 'local':local, 'paramiko_ssh':paramiko_ssh, 'psrp':psrp, 'ssh':ssh, 'winrm':winrm, 'b64decode':b64decode, 'b64encode':b64encode, 'basename':basename, 'bool':bool, 'checksum':checksum, 'combinations':combinations, 'combine':combine, 'comment':comment, 'dict2items':dict2items, 'difference':difference, 'dirname':dirname, 'expanduser':expanduser, 'expandvars':expandvars, 'extract':extract, 'fileglob':fileglob, 'flatten':flatten, 'from_json':from_json, 'from_yaml':from_yaml, 'from_yaml_all':from_yaml_all, 'hash':hash, 'human_readable':human_readable, 'human_to_bytes':human_to_bytes, 'intersect':intersect, 'items2dict':items2dict, 'log':log, 'mandatory':mandatory, 'md5':md5, 'password_hash':password_hash, 'path_join':path_join, 'permutations':permutations, 'pow':pow, 'product':product, 'quote':quote, 'random':random, 'realpath':realpath, 'regex_escape':regex_escape, 'regex_findall':regex_findall, 'regex_replace':regex_replace, 'regex_search':regex_search, 'rekey_on_member':rekey_on_member, 'relpath':relpath, 'root':root, 'sha1':sha1, 'shuffle':shuffle, 'splittext':splittext, 'strftime':strftime, 'subelements':subelements, 'symmetric_difference':symmetric_difference, 'ternary':ternary, 'to_datetime':to_datetime, 'to_json':to_json, 'to_nice_json':to_nice_json, 'to_nice_yaml':to_nice_yaml, 'to_uuid':to_uuid, 'to_yaml':to_yaml, 'type_debug':type_debug, 'union':union, 'unique':unique, 'unvault':unvault, 'urlsplit':urlsplit, 'vault':vault, 'win_basename':win_basename, 'win_dirname':win_dirname, 'win_splitdrive':win_splitdrive, 'zip':zip, 'zip_longest':zip_longest, 'advanced_host_list':advanced_host_list, 'auto':auto, 'constructed':constructed, 'generator':generator, 'host_list':host_list, 'ini':ini, 'script':script, 'toml':toml, 'yaml':yaml, 'config':config, 'csvfile':csvfile, 'dict':dict, 'env':env, 'file':file, 'fileglob':fileglob, 'first_found':first_found, 'indexed_items':indexed_items, 'ini':ini, 'inventory_hostnames':inventory_hostnames, 'lines':lines, 'list':list, 'nested':nested, 'password':password, 'pipe':pipe, 'random_choice':random_choice, 'sequence':sequence, 'subelements':subelements, 'template':template, 'together':together, 'unvault':unvault, 'url':url, 'varnames':varnames, 'vars':vars, 'cmd':cmd, 'powershell':powershell, 'sh':sh, 'debug':debug, 'free':free, 'host_pinned':host_pinned, 'linear':linear, 'abs':abs, 'all':all, 'any':any, 'changed':changed, 'contains':contains, 'directory':directory, 'exists':exists, 'failed':failed, 'falsy':falsy, 'file':file, 'finished':finished, 'link':link, 'link_exists':link_exists, 'match':match, 'mount':mount, 'nan':nan, 'reachable':reachable, 'regex':regex, 'same_file':same_file, 'search':search, 'skipped':skipped, 'started':started, 'subset':subset, 'success':success, 'superset':superset, 'truthy':truthy, 'unreachable':unreachable, 'uri':uri, 'url':url, 'urn':urn, 'vault_encrypted':vault_encrypted, 'version':version, 'host_group_vars':host_group_vars}
