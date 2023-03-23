from . import playWriterHelpers as PWH
from . import menus

#---------------------------------------------------------
# Variables

baseModuleName = "\tansible.builtin."
funcs = {} # Located at very bottom of file

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
        o += PWH.selevel()
        o += PWH.serole()
        o += PWH.setype()
        o += PWH.seuser()
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
    o += PWH.selevel()
    o += PWH.serole()
    o += PWH.setype()
    o += PWH.seuser()
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

    # attributes
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
    o += PWH.selevel()
    o += PWH.serole()
    o += PWH.setype()
    o += PWH.seuser()
    # src 
    o += PWH.unsafe_writes()
    o += PWH.validate()

    return o

def cron():
    #cron module
    o = ""
    o += PWH.playStart("cron")

    #name


    # backup 
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
    # state 
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
    # state 
    # update_cache 
    o += PWH.update_cache()
    # update_only 
    # validate_certs
    o += PWH.validate_certs()


    return o

def dpkg_selections():
    #dpkg_selections module
    o = ""
    o += PWH.playStart("dpkg_selections")
    return o

def expect():
    #expect module
    o = ""
    o += PWH.playStart("expect")
    return o

def fail():
    #fail module
    o = ""
    o += PWH.playStart("fail")
    return o

def fetch():
    #fetch module
    o = ""
    o += PWH.playStart("fetch")
    return o

def file():
    #file module
    o = ""
    o += PWH.playStart("file")
    return o

def find():
    #find module
    o = ""
    o += PWH.playStart("find")
    return

def gather_facts():
    #gather_facts module
    o = ""
    o += PWH.playStart("gather_facts")
    return o

def get_url():
    #get_url module
    o = ""
    o += PWH.playStart("get_url")
    return o

def getent():
    #getent module
    o = ""
    o += PWH.playStart("getent")
    return o

def git():
    #git module
    o = ""
    o += PWH.playStart("git")
    return o

def group():
    #group module
    o = ""
    o += PWH.playStart("group")
    return o

def group_by():
    #group_by module
    o = ""
    o += PWH.playStart("group_by")
    return o

def hostname():
    #hostname module
    o = ""
    o += PWH.playStart("hostname")
    return o

def import_playbook():
    #import_playbook module
    o = ""
    o += PWH.playStart("import_playbook")
    return o

def import_role():
    #import_role module
    o = ""
    o += PWH.playStart("import_role")
    return o

def import_tasks():
    #import_tasks module
    o = ""
    o += PWH.playStart("import_tasks")
    return o

def include():
    #include module
    o = ""
    o += PWH.playStart("include")
    return o

def include_role():
    #include_role module
    o = ""
    o += PWH.playStart("include_role")
    return o

def include_tasks():
    #include_tasks module
    o = ""
    o += PWH.playStart("include_tasks")
    return o

def include_vars():
    #include_vars module
    o = ""
    o += PWH.playStart("include_vars")
    return o

def iptables():
    #iptables module
    o = ""
    o += PWH.playStart("iptables")
    return o

def known_hosts():
    #known_hosts module
    o = ""
    o += PWH.playStart("known_hosts")
    return o

def lineinfile():
    #lineinfile module
    o = ""
    o += PWH.playStart("lineinfile")
    return o

def meta():
    #meta module
    o = ""
    o += PWH.playStart("meta")
    return o

def package():
    #package module
    o = ""
    o += PWH.playStart("package")
    return o

def package_facts():
    #package_facts module
    o = ""
    o += PWH.playStart("apt")
    return o

def pause():
    #pause module
    o = ""
    o += PWH.playStart("apt")
    return o

def ping():
    #ping module
    o = ""
    o += PWH.playStart("apt")
    return o

def pip():
    #pip module
    o = ""
    o += PWH.playStart("apt")
    return o

def raw():
    #raw module
    o = ""
    o += PWH.playStart("apt")
    return o

def reboot():
    #reboot module
    o = ""
    o += PWH.playStart("apt")
    return o

def replace():
    #replace module
    o = ""
    o += PWH.playStart("apt")
    return o

def rpm_key():
    #rpm_key module
    o = ""
    o += PWH.playStart("apt")
    return o

def script():
    #script module
    o = ""
    o += PWH.playStart("apt")
    return o

def service():
    #service module
    o = ""
    o += PWH.playStart("apt")
    return o

def service_facts():
    #service_facts module
    o = ""
    o += PWH.playStart("apt")
    return o

def set_fact():
    #set_fact module
    o = ""
    o += PWH.playStart("apt")
    return o

def set_stats():
    #set_stats module
    o = ""
    o += PWH.playStart("apt")
    return o

def setup():
    #setup module
    o = ""
    o += PWH.playStart("apt")
    return o

def shell():
    #shell module
    o = ""
    o += PWH.playStart("apt")
    return o

def slurp():
    #slurp module
    o = ""
    o += PWH.playStart("apt")
    return o

def stat():
    #stat module
    o = ""
    o += PWH.playStart("apt")
    return o

def subversion():
    #subversion module
    o = ""
    o += PWH.playStart("apt")
    return o

def systemd():
    #systemd module
    o = ""
    o += PWH.playStart("apt")
    return o

def systemd_service():
    #systemd_service module
    o = ""
    o += PWH.playStart("apt")
    return o

def sysvinit():
    #sysvinit module
    o = ""
    o += PWH.playStart("apt")
    return o

def tempfile():
    #tempfile module
    o = ""
    o += PWH.playStart("apt")
    return o

def template():
    #template module
    o = ""
    o += PWH.playStart("apt")
    return o

def unarchive():
    #unarchive module
    o = ""
    o += PWH.playStart("apt")
    return o

def uri():
    #uri module
    o = ""
    o += PWH.playStart("apt")
    return o

def user():
    #user module
    o = ""
    o += PWH.playStart("apt")
    return o

def validate_argument_spec():
    #validate_argument_spec module
    o = ""
    o += PWH.playStart("apt")
    return o

def wait_for():
    #wait_for module
    o = ""
    o += PWH.playStart("apt")
    return o

def wait_for_connection():
    #wait_for_connection module
    o = ""
    o += PWH.playStart("apt")
    return o

def yum():
    #yum module
    o = ""
    o += PWH.playStart("apt")
    return o

def yum_repository():
    #yum_repository module
    o = ""
    o += PWH.playStart("apt")
    return o

def runas():
    #runas become
    o = ""
    o += PWH.playStart("apt")
    return o

def su():
    #su become
    o = ""
    o += PWH.playStart("apt")
    return o

def sudo():
    #sudo become
    o = ""
    o += PWH.playStart("apt")
    return o

def jsonfile():
    #jsonfile cache
    o = ""
    o += PWH.playStart("apt")
    return o

def memory():
    #memory cache
    o = ""
    o += PWH.playStart("apt")
    return o

def default():
    #default callback
    o = ""
    o += PWH.playStart("apt")
    return o

def junit():
    #junit callback
    o = ""
    o += PWH.playStart("apt")
    return o

def minimal():
    #minimal callback
    o = ""
    o += PWH.playStart("apt")
    return o

def oneline():
    #oneline callback
    o = ""
    o += PWH.playStart("apt")
    return o

def tree():
    #tree callback
    o = ""
    o += PWH.playStart("apt")
    return o


def local():
    #local connection
    o = ""
    o += PWH.playStart("apt")
    return o

def paramiko_ssh():
    #paramiko_ssh connection
    o = ""
    o += PWH.playStart("apt")
    return o

def psrp():
    #psrp connection
    o = ""
    o += PWH.playStart("apt")
    return o

def ssh():
    #ssh connection
    o = ""
    o += PWH.playStart("apt")
    return o

def winrm():
    #winrm connection
    o = ""
    o += PWH.playStart("apt")
    return o

def b64decode():
    #b64decode filter
    o = ""
    o += PWH.playStart("apt")
    return o

def b64encode():
    #b64encode filter
    o = ""
    o += PWH.playStart("apt")
    return o

def basename():
    #basename filter
    o = ""
    o += PWH.playStart("apt")
    return o

def bool():
    #bool filter
    o = ""
    o += PWH.playStart("apt")
    return o

def checksum():
    #checksum filter
    o = ""
    o += PWH.playStart("apt")
    return o

def combinations():
    #combinations filter
    o = ""
    o += PWH.playStart("apt")
    return o

def combine():
    #combine filter
    o = ""
    o += PWH.playStart("apt")
    return o

def comment():
    #comment filter
    o = ""
    o += PWH.playStart("apt")
    return o

def dict2items():
    #dict2items filter
    o = ""
    o += PWH.playStart("apt")
    return o

def difference():
    #difference filter
    o = ""
    o += PWH.playStart("apt")
    return o

def dirname():
    #dirname filter
    o = ""
    o += PWH.playStart("apt")
    return o

def expanduser():
    #expanduser filter
    o = ""
    o += PWH.playStart("apt")
    return o

def expandvars():
    #expandvars filter
    o = ""
    o += PWH.playStart("apt")
    return o

def extract():
    #extract filter
    o = ""
    o += PWH.playStart("apt")
    return o

def fileglob():
    #fileglob filter
    o = ""
    o += PWH.playStart("apt")
    return o

def flatten():
    #flatten filter
    o = ""
    o += PWH.playStart("apt")
    return o

def from_json():
    #from_json filter
    o = ""
    o += PWH.playStart("apt")
    return o

def from_yaml():
    #from_yaml filter
    o = ""
    o += PWH.playStart("apt")
    return o

def from_yaml_all():
    #from_yaml_all filter
    o = ""
    o += PWH.playStart("apt")
    return o

def hash():
    #hash filter
    o = ""
    o += PWH.playStart("apt")
    return o

def human_readable():
    #human_readable filter
    o = ""
    o += PWH.playStart("apt")
    return o

def human_to_bytes():
    #human_to_bytes filter
    o = ""
    o += PWH.playStart("apt")
    return o

def intersect():
    #intersect filter
    o = ""
    o += PWH.playStart("apt")
    return o

def items2dict():
    #items2dict filter
    o = ""
    o += PWH.playStart("apt")
    return o

def log():
    #log filter
    o = ""
    o += PWH.playStart("apt")
    return o

def mandatory():
    #mandatory filter
    o = ""
    o += PWH.playStart("apt")
    return o

def md5():
    #md5 filter
    o = ""
    o += PWH.playStart("apt")
    return o

def password_hash():
    #password_hash filter
    o = ""
    o += PWH.playStart("apt")
    return o

def path_join():
    #path_join filter
    o = ""
    o += PWH.playStart("apt")
    return o

def permutations():
    #permutations filter
    o = ""
    o += PWH.playStart("apt")
    return o

def pow():
    #pow filter
    o = ""
    o += PWH.playStart("apt")
    return o

def product():
    #product filter
    o = ""
    o += PWH.playStart("apt")
    return o

def quote():
    #quote filter
    o = ""
    o += PWH.playStart("apt")
    return o

def random():
    #random filter
    o = ""
    o += PWH.playStart("apt")
    return o

def realpath():
    #realpath filter
    o = ""
    o += PWH.playStart("apt")
    return o

def regex_escape():
    #regex_escape filter
    o = ""
    o += PWH.playStart("apt")
    return o

def regex_findall():
    #regex_findall filter
    o = ""
    o += PWH.playStart("apt")
    return o

def regex_replace():
    #regex_replace filter
    o = ""
    o += PWH.playStart("apt")
    return o

def regex_search():
    #regex_search filter
    o = ""
    o += PWH.playStart("apt")
    return o

def rekey_on_member():
    #rekey_on_member filter
    o = ""
    o += PWH.playStart("apt")
    return o

def relpath():
    #relpath filter
    o = ""
    o += PWH.playStart("apt")
    return o

def root():
    #root filter
    return

def sha1():
    #sha1 filter
    o = ""
    o += PWH.playStart("apt")
    return o

def shuffle():
    #shuffle filter
    o = ""
    o += PWH.playStart("apt")
    return o

def splitext():
    #splitext filter
    o = ""
    o += PWH.playStart("apt")
    return o

def strftime():
    #strftime filter
    o = ""
    o += PWH.playStart("apt")
    return o

def subelements():
    #subelements filter
    o = ""
    o += PWH.playStart("apt")
    return o

def symmetric_difference():
    #symmetric_difference filter
    o = ""
    o += PWH.playStart("apt")
    return o

def ternary():
    #ternary filter
    o = ""
    o += PWH.playStart("apt")
    return o

def to_datetime():
    #to_datetime filter
    o = ""
    o += PWH.playStart("apt")
    return o

def to_json():
    #to_json filter
    o = ""
    o += PWH.playStart("apt")
    return o

def to_nice_json():
    #to_nice_json filter
    o = ""
    o += PWH.playStart("apt")
    return o

def to_nice_yaml():
    #to_nice_yaml filter
    o = ""
    o += PWH.playStart("apt")
    return o

def to_uuid():
    #to_uuid filter
    o = ""
    o += PWH.playStart("apt")
    return o

def to_yaml():
    #to_yaml filter
    o = ""
    o += PWH.playStart("apt")
    return o

def type_debug():
    #type_debug filter
    o = ""
    o += PWH.playStart("apt")
    return o

def union():
    #union filter
    o = ""
    o += PWH.playStart("apt")
    return o

def unique():
    #unique filter
    o = ""
    o += PWH.playStart("apt")
    return o

def unvault():
    #unvault filter
    o = ""
    o += PWH.playStart("apt")
    return o

def urlsplit():
    #urlsplit filter
    o = ""
    o += PWH.playStart("apt")
    return o

def vault():
    #vault filter
    o = ""
    o += PWH.playStart("apt")
    return o

def win_basename():
    #win_basename filter
    o = ""
    o += PWH.playStart("apt")
    return o

def win_dirname():
    #win_dirname filter
    o = ""
    o += PWH.playStart("apt")
    return o

def win_splitdrive():
    #win_splitdrive filter
    o = ""
    o += PWH.playStart("apt")
    return o

def zip():
    #zip filter
    o = ""
    o += PWH.playStart("apt")
    return o

def zip_longest():
    #zip_longest filter
    o = ""
    o += PWH.playStart("apt")
    return o

def advanced_host_list():
    #advanced_host_list inventory
    o = ""
    o += PWH.playStart("apt")
    return o

def auto():
    #auto inventory
    o = ""
    o += PWH.playStart("apt")
    return o

def constructed():
    #constructed inventory
    o = ""
    o += PWH.playStart("apt")
    return o

def generator():
    #generator inventory
    o = ""
    o += PWH.playStart("apt")
    return o

def host_list():
    #host_list inventory
    o = ""
    o += PWH.playStart("apt")
    return o

def ini():
    #ini inventory
    o = ""
    o += PWH.playStart("apt")
    return o

def script():
    #script inventory
    o = ""
    o += PWH.playStart("apt")
    return o

def toml():
    #toml inventory
    o = ""
    o += PWH.playStart("apt")
    return o

def yaml():
    #yaml inventory
    o = ""
    o += PWH.playStart("apt")
    return o


def config():
    #config lookup
    o = ""
    o += PWH.playStart("apt")
    return o

def csvfile():
    #csvfile lookup
    o = ""
    o += PWH.playStart("apt")
    return o

def dict():
    #dict lookup
    o = ""
    o += PWH.playStart("apt")
    return o

def env():
    #env lookup
    o = ""
    o += PWH.playStart("apt")
    return o

def file():
    #file lookup
    o = ""
    o += PWH.playStart("apt")
    return o

def fileglob():
    #fileglob lookup
    o = ""
    o += PWH.playStart("apt")
    return o

def first_found():
    #first_found lookup
    o = ""
    o += PWH.playStart("apt")
    return o

def indexed_items():
    #indexed_items lookup
    o = ""
    o += PWH.playStart("apt")
    return o

def ini():
    #ini lookup
    o = ""
    o += PWH.playStart("apt")
    return o

def inventory_hostnames():
    #inventory_hostnames
    o = ""
    o += PWH.playStart("apt")
    return o

def lines():
    #lines lookup
    o = ""
    o += PWH.playStart("apt")
    return o

def list():
    #list lookup
    o = ""
    o += PWH.playStart("apt")
    return o

def nested():
    #nested lookup
    o = ""
    o += PWH.playStart("apt")
    return o

def password():
    #password lookup
    o = ""
    o += PWH.playStart("apt")
    return o

def pipe():
    #pipe lookup
    o = ""
    o += PWH.playStart("apt")
    return o

def random_choice():
    #random_choice lookup
    o = ""
    o += PWH.playStart("apt")
    return o

def sequence():
    #sequence lookup
    o = ""
    o += PWH.playStart("apt")
    return o

def subelements():
    #subelements lookup
    o = ""
    o += PWH.playStart("apt")
    return o

def template():
    #template lookup
    o = ""
    o += PWH.playStart("apt")
    return o

def together():
    #together lookup
    o = ""
    o += PWH.playStart("apt")
    return o

def unvault():
    #unvault lookup
    o = ""
    o += PWH.playStart("apt")
    return o

def url():
    #url lookup
    o = ""
    o += PWH.playStart("apt")
    return o

def varnames():
    #varnames lookup
    o = ""
    o += PWH.playStart("apt")
    return o

def vars():
    #vars lookup 
    o = ""
    o += PWH.playStart("apt")
    return o


def cmd():
    #cmd shell
    o = ""
    o += PWH.playStart("apt")
    return o

def powershell():
    #powershell shell
    o = ""
    o += PWH.playStart("apt")
    return o

def sh():
    #sh shell
    o = ""
    o += PWH.playStart("apt")
    return o


def debug():
    #debug strategy
    o = ""
    o += PWH.playStart("apt")
    return o

def free():
    #free strategy
    o = ""
    o += PWH.playStart("apt")
    return o

def host_pinned():
    #host_pinned strategy
    o = ""
    o += PWH.playStart("apt")
    return o

def linear():
    #linear strategy
    o = ""
    o += PWH.playStart("apt")
    return o


def abs():
    #abs all test
    o = ""
    o += PWH.playStart("apt")
    return o

def any():
    #any test
    o = ""
    o += PWH.playStart("apt")
    return o

def changed():
    #changed test
    o = ""
    o += PWH.playStart("apt")
    return o

def contains():
    #contains test
    o = ""
    o += PWH.playStart("apt")
    return o

def directory():
    #directory test
    o = ""
    o += PWH.playStart("apt")
    return o

def exists():
    #exists test
    o = ""
    o += PWH.playStart("apt")
    return o

def failed():
    #failed test
    o = ""
    o += PWH.playStart("apt")
    return o

def falsy():
    #falsy test
    o = ""
    o += PWH.playStart("apt")
    return o

def file():
    #file test
    o = ""
    o += PWH.playStart("apt")
    return o

def finished():
    #finished test
    o = ""
    o += PWH.playStart("apt")
    return o

def link():
    #link test
    o = ""
    o += PWH.playStart("apt")
    return o

def link_exists():
    #link_exists test
    o = ""
    o += PWH.playStart("apt")
    return o

def match():
    #match test
    o = ""
    o += PWH.playStart("apt")
    return o

def mount():
    #mount test
    o = ""
    o += PWH.playStart("apt")
    return o

def nan():
    #nan test
    o = ""
    o += PWH.playStart("apt")
    return o

def reachable():
    #reachable test
    o = ""
    o += PWH.playStart("apt")
    return o

def regex():
    #regex test
    o = ""
    o += PWH.playStart("apt")
    return o

def same_file():
    #same_file test
    o = ""
    o += PWH.playStart("apt")
    return o

def search():
    #search test
    o = ""
    o += PWH.playStart("apt")
    return o

def skipped():
    #skipped test
    o = ""
    o += PWH.playStart("apt")
    return o

def started():
    #started test
    o = ""
    o += PWH.playStart("apt")
    return o

def subset():
    #subset test
    o = ""
    o += PWH.playStart("apt")
    return o

def success():
    #success test
    o = ""
    o += PWH.playStart("apt")
    return o

def superset():
    #superset test
    o = ""
    o += PWH.playStart("apt")
    return o

def truthy():
    #truthy test
    o = ""
    o += PWH.playStart("apt")
    return o

def unreachable():
    #unreachable test
    o = ""
    o += PWH.playStart("apt")
    return o

def uri():
    #uri test
    o = ""
    o += PWH.playStart("apt")
    return o

def url():
    #url test
    o = ""
    o += PWH.playStart("apt")
    return o

def urn():
    #urn test
    o = ""
    o += PWH.playStart("apt")
    return o

def vault_encrypted():
    #vault_encrypted test
    o = ""
    o += PWH.playStart("apt")
    return o

def version():
    #version test
    o = ""
    o += PWH.playStart("apt")
    return o

def host_group_vars():
    #host_group_vars test
    o = ""
    o += PWH.playStart("apt")
    return o

funcs = {'add_host':add_host, 'apt':apt, 'apt_key':apt_key, 'apt_repository':apt_repository, 'assemble':assemble, 'assert':Assert, 'async_status':async_status, 'blockinfile':blockinfile, 'command':command, 'copy':copy, 'cron':cron, 'debconf':debconf, 'debug':debug, 'dnf':dnf, 'dpkg_selections':dpkg_selections, 'expect':expect, 'fail':fail, 'fetch':fetch, 'file':file, 'gather_facts':gather_facts, 'get_url':get_url, 'getent':getent, 'git':git, 'group':group, 'group_by':group_by, 'hostname':hostname, 'import_playbook':import_playbook, 'import_role':import_role, 'import_tasks':import_tasks, 'include':include, 'include_role':include_role, 'include_tasks':include_tasks, 'include_vars':include_vars, 'iptables':iptables, 'known_hosts':known_hosts, 'lineinfile':lineinfile, 'meta':meta, 'package':package, 'package_facts':package_facts, 'pause':pause, 'ping':ping, 'pip':pip, 'raw':raw, 'reboot':reboot, 'replace':replace, 'rpm_key':rpm_key, 'script':script, 'service':service, 'service_facts':service_facts, 'set_fact':set_fact, 'set_stats':set_stats, 'setup':setup, 'shell':shell, 'slurp':slurp, 'stat':stat, 'subversion':subversion, 'systemd':systemd, 'systemd_service':systemd_service, 'sysvinit':sysvinit, 'tempfile':tempfile, 'template':template, 'unarchive':unarchive, 'uri':uri, 'user':user, 'validate_argument_spec':validate_argument_spec, 'wait_for':wait_for, 'wait_for_connection':wait_for_connection, 'yum':yum, 'yum_repository':yum_repository, 'runas':runas, 'su':su, 'sudo':sudo, 'jsonfile':jsonfile, 'memory':memory, 'default':default, 'junit':junit, 'minimal':minimal, 'oneline':oneline, 'tree':tree, 'local':local, 'paramiko_ssh':paramiko_ssh, 'psrp':psrp, 'ssh':ssh, 'winrm':winrm, 'b64decode':b64decode, 'b64encode':b64encode, 'basename':basename, 'bool':bool, 'checksum':checksum, 'combinations':combinations, 'combine':combine, 'comment':comment, 'dict2items':dict2items, 'difference':difference, 'dirname':dirname, 'expanduser':expanduser, 'expandvars':expandvars, 'extract':extract, 'fileglob':fileglob, 'flatten':flatten, 'from_json':from_json, 'from_yaml':from_yaml, 'from_yaml_all':from_yaml_all, 'hash':hash, 'human_readable':human_readable, 'human_to_bytes':human_to_bytes, 'intersect':intersect, 'items2dict':items2dict, 'log':log, 'mandatory':mandatory, 'md5':md5, 'password_hash':password_hash, 'path_join':path_join, 'permutations':permutations, 'pow':pow, 'product':product, 'quote':quote, 'random':random, 'realpath':realpath, 'regex_escape':regex_escape, 'regex_findall':regex_findall, 'regex_replace':regex_replace, 'regex_search':regex_search, 'rekey_on_member':rekey_on_member, 'relpath':relpath, 'root':root, 'sha1':sha1, 'shuffle':shuffle, 'splitext':splitext, 'strftime':strftime, 'subelements':subelements, 'symmetric_difference':symmetric_difference, 'ternary':ternary, 'to_datetime':to_datetime, 'to_json':to_json, 'to_nice_json':to_nice_json, 'to_nice_yaml':to_nice_yaml, 'to_uuid':to_uuid, 'to_yaml':to_yaml, 'type_debug':type_debug, 'union':union, 'unique':unique, 'unvault':unvault, 'urlsplit':urlsplit, 'vault':vault, 'win_basename':win_basename, 'win_dirname':win_dirname, 'win_splitdrive':win_splitdrive, 'zip':zip, 'zip_longest':zip_longest, 'advanced_host_list':advanced_host_list, 'auto':auto, 'constructed':constructed, 'generator':generator, 'host_list':host_list, 'ini':ini, 'script':script, 'toml':toml, 'yaml':yaml, 'config':config, 'csvfile':csvfile, 'dict':dict, 'env':env, 'file':file, 'fileglob':fileglob, 'first_found':first_found, 'indexed_items':indexed_items, 'ini':ini, 'inventory_hostnames':inventory_hostnames, 'lines':lines, 'list':list, 'nested':nested, 'password':password, 'pipe':pipe, 'random_choice':random_choice, 'sequence':sequence, 'subelements':subelements, 'template':template, 'together':together, 'unvault':unvault, 'url':url, 'varnames':varnames, 'vars':vars, 'cmd':cmd, 'powershell':powershell, 'sh':sh, 'debug':debug, 'free':free, 'host_pinned':host_pinned, 'linear':linear, 'abs':abs, 'all':all, 'any':any, 'changed':changed, 'contains':contains, 'directory':directory, 'exists':exists, 'failed':failed, 'falsy':falsy, 'file':file, 'finished':finished, 'link':link, 'link_exists':link_exists, 'match':match, 'mount':mount, 'nan':nan, 'reachable':reachable, 'regex':regex, 'same_file':same_file, 'search':search, 'skipped':skipped, 'started':started, 'subset':subset, 'success':success, 'superset':superset, 'truthy':truthy, 'unreachable':unreachable, 'uri':uri, 'url':url, 'urn':urn, 'vault_encrypted':vault_encrypted, 'version':version, 'host_group_vars':host_group_vars}
