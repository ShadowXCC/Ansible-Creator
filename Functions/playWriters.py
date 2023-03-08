#import playWriterHelpers as PWH
import menus as menus

#---------------------------------------------------------
# Variables

baseModuleName = "\tansible.builtin."

#---------------------------------------------------------

def add_host():
    o = ""
    #o += PWH.playName()
    o += "- name: " + input("What would you like to name this play: ") + "\n"
    o += baseModuleName + "add_host:\n"
    o += "\t\tname: " + input("\nExample: \"ip:portnumber\"\n" + "Enter the hostname/IP address you are adding a host to: ") + "\n"
    # groups
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

    # ansible_host and ansible_port
    if input("Does the host you need to reach exist through a tunnel (Y/N): ").lower() == "y":
        o += "\t\tansible_host: " + input("What is the hostname of the tunnel? ") + "\n"
        o += "\t\tansible_port: " + input("What is the port number of the tunnel? ") + "\n"

    #Loop    
    if input("Do you want this play to loop (Y/N): ").lower() == "y":
        o += "\tloop: " + input("How many times do you want this play to loop: ")

    # # action
    # o += "\t\t" + "\n"
    # # async
    # o += "\t\t" + "\n"
    # # become
    # o += "\t\t" + "\n"
    # # bypasss_host_loop
    # o += "\t\t" + "\n"
    # # bypass_task_loop
    # o += "\t\t" + "\n"
    # # check_mode
    # o += "\t\t" + "\n"
    # # connection
    # o += "\t\t"  + "\n"
    # # core
    # o += "\t\t" + "\n"
    # # delegation
    # o += "\t\t" + "\n"
    # # diff_mode
    # o += "\t\t" + "\n"
    # # ignore_conditional
    # o += "\t\t" + "\n"
    # # platform
    # o += "\t\t" + "\n"
    # # tags
    # o += "\t\t" + "\n"
    # # until
    # o += "\t\t" + "\n"
    return o

def apt():
    o = ""
    o += "- name: " + input("What would you like to name this play: ") + "\n"
    o += "\t\tname:"
    packages = input("Enter the name(s) of the package(s), with spaces separating multiple package names: ")
    if " " in packages:
        o += "\n"
        pList = packages.split()
        for item in pList:
            o += "\t\t- " + item + "\n"
    else:
        o += packages

    #state
    if input("Do you want to specify a required state for these packages? (Y/N)").lower == "y":
        o += "\t\tstate: "
        while True:
            print(menus.aptStatesMenu())
            choice = input("pick")
            if choice == "1":
                o += "present"
                break
            elif choice == "2":
                o += "absent"
                break
            elif choice == "3":
                o += "latest"
                break
            elif choice == "4":
                o += "build-dep"
                break
            elif choice == "5":
                o += "fixed"
                break
            else:
                print("Incorrect Input, please try again.")
        o += "\n"
    
    



    # allow_change_held_packages allow_downgrade allow_unauthenticated autoclean autoremove cache_valid_time clean deb default release
    # dpkg_options fail_on_autoremove force force_apt_get install_recommends lock_timeout name only_upgrade policy_rc_d purge update_cache
    # update_cache_retries update_cache_retry_max_delay upgrade 

    return o

def apt_key():
    #apt_key module
    return

def apt_repository():
    #apt_repository module
    return

def assemble():
    #assemble module
    return

def assert1():
    #assert module
    return

def async_status():
    #async_status module
    return

def blockinfile():
    #blockinfile module
    return

def command():
    #command module
    return

def copy():
    #copy module
    return

def cron():
    #cron module
    return

def debconf():
    #debconf module
    return

def debug():
    #debug module
    return

def dnf():
    #dnf module
    return

def dpkg_selections():
    #dpkg_selections module
    return

def expect():
    #expect module
    return

def fail():
    #fail module
    return

def fetch():
    #fetch module
    return

def file():
    #file module
    return

def find():
    #find module
    return

def gather_facts():
    #gather_facts module
    return

def get_url():
    #get_url module
    return

def getent():
    #getent module
    return

def git():
    #git module
    return

def group():
    #group module
    return

def group_by():
    #group_by module
    return

def hostname():
    #hostname module
    return

def import_playbook():
    #import_playbook module
    return

def import_role():
    #import_role module
    return

def import_tasks():
    #import_tasks module
    return

def include():
    #include module
    return

def include_role():
    #include_role module
    return

def include_tasks():
    #include_tasks module
    return

def include_vars():
    #include_vars module
    return

def iptables():
    #iptables module
    return

def known_hosts():
    #known_hosts module
    return

def lineinfile():
    #lineinfile module
    return

def meta():
    #meta module
    return

def package():
    #package module
    return

def package_facts():
    #package_facts module
    return

def pause():
    #pause module
    return

def ping():
    #ping module
    return

def pip():
    #pip module
    return

def raw():
    #raw module
    return

def reboot():
    #reboot module
    return

def replace():
    #replace module
    return

def rpm_key():
    #rpm_key module
    return

def script():
    #script module
    return

def service():
    #service module
    return

def service_facts():
    #service_facts module
    return

def set_fact():
    #set_fact module
    return

def set_stats():
    #set_stats module
    return

def setup():
    #setup module
    return

def shell():
    #shell module
    return

def slurp():
    #slurp module
    return

def stat():
    #stat module
    return

def subversion():
    #subversion module
    return

def systemd():
    #systemd module
    return

def systemd_service():
    #systemd_service module
    return

def sysvinit():
    #sysvinit module
    return

def tempfile():
    #tempfile module
    return

def template():
    #template module
    return

def unarchive():
    #unarchive module
    return

def uri():
    #uri module
    return

def user():
    #user module
    return

def validate_argument_spec():
    #validate_argument_spec module
    return

def wait_for():
    #wait_for module
    return

def wait_for_connection():
    #wait_for_connection module
    return

def yum():
    #yum module
    return

def yum_repository():
    #yum_repository module
    return


def runas():
    #runas become
    return

def su():
    #su become
    return

def sudo():
    #sudo become
    return


def jsonfile():
    #jsonfile cache
    return

def memory():
    #memory cache
    return


def default():
    #default callback
    return

def junit():
    #junit callback
    return

def minimal():
    #minimal callback
    return

def oneline():
    #oneline callback
    return

def tree():
    #tree callback
    return


def local():
    #local connection
    return

def paramiko_ssh():
    #paramiko_ssh connection
    return

def psrp():
    #psrp connection
    return

def ssh():
    #ssh connection
    return

def winrm():
    #winrm connection
    return


def b64decode():
    #b64decode filter
    return

def b64encode():
    #b64encode filter
    return

def basename():
    #basename filter
    return

def bool():
    #bool filter
    return

def checksum():
    #checksum filter
    return

def combinations():
    #combinations filter
    return

def combine():
    #combine filter
    return

def comment():
    #comment filter
    return

def dict2items():
    #dict2items filter
    return

def difference():
    #difference filter
    return

def dirname():
    #dirname filter
    return

def expanduser():
    #expanduser filter
    return

def expandvars():
    #expandvars filter
    return

def extract():
    #extract filter
    return

def fileglob():
    #fileglob filter
    return

def flatten():
    #flatten filter
    return

def from_json():
    #from_json filter
    return

def from_yaml():
    #from_yaml filter
    return

def from_yaml_all():
    #from_yaml_all filter
    return

def hash():
    #hash filter
    return

def human_readable():
    #human_readable filter
    return

def human_to_bytes():
    #human_to_bytes filter
    return

def intersect():
    #intersect filter
    return

def items2dict():
    #items2dict filter
    return

def log():
    #log filter
    return

def mandatory():
    #mandatory filter
    return

def md5():
    #md5 filter
    return

def password_hash():
    #password_hash filter
    return

def path_join():
    #path_join filter
    return

def permutations():
    #permutations filter
    return

def pow():
    #pow filter
    return

def product():
    #product filter
    return

def quote():
    #quote filter
    return

def random():
    #random filter
    return

def realpath():
    #realpath filter
    return

def regex_escape():
    #regex_escape filter
    return

def regex_findall():
    #regex_findall filter
    return

def regex_replace():
    #regex_replace filter
    return

def regex_search():
    #regex_search filter
    return

def rekey_on_member():
    #rekey_on_member filter
    return

def relpath():
    #relpath filter
    return

def root():
    #root filter
    return

def sha1():
    #sha1 filter
    return

def shuffle():
    #shuffle filter
    return

def splitext():
    #splitext filter
    return

def strftime():
    #strftime filter
    return

def subelements():
    #subelements filter
    return

def symmetric_difference():
    #symmetric_difference filter
    return

def ternary():
    #ternary filter
    return

def to_datetime():
    #to_datetime filter
    return

def to_json():
    #to_json filter
    return

def to_nice_json():
    #to_nice_json filter
    return

def to_nice_yaml():
    #to_nice_yaml filter
    return

def to_uuid():
    #to_uuid filter
    return

def to_yaml():
    #to_yaml filter
    return

def type_debug():
    #type_debug filter
    return

def union():
    #union filter
    return

def unique():
    #unique filter
    return

def unvault():
    #unvault filter
    return

def urlsplit():
    #urlsplit filter
    return

def vault():
    #vault filter
    return

def win_basename():
    #win_basename filter
    return

def win_dirname():
    #win_dirname filter
    return

def win_splitdrive():
    #win_splitdrive filter
    return

def zip():
    #zip filter
    return

def zip_longest():
    #zip_longest filter
    return


def advanced_host_list():
    #advanced_host_list inventory
    return

def auto():
    #auto inventory
    return

def constructed():
    #constructed inventory
    return

def generator():
    #generator inventory
    return

def host_list():
    #host_list inventory
    return

def ini():
    #ini inventory
    return

def script():
    #script inventory
    return

def toml():
    #toml inventory
    return

def yaml():
    #yaml inventory
    return


def config():
    #config lookup
    return

def csvfile():
    #csvfile lookup
    return

def dict():
    #dict lookup
    return

def env():
    #env lookup
    return

def file():
    #file lookup
    return

def fileglob():
    #fileglob lookup
    return

def first_found():
    #first_found lookup
    return

def indexed_items():
    #indexed_items lookup
    return

def ini():
    #ini lookup
    return

def inventory_hostnames():
    #inventory_hostnames
    return

def lines():
    #lines lookup
    return

def list():
    #list lookup
    return

def nested():
    #nested lookup
    return

def password():
    #password lookup
    return

def pipe():
    #pipe lookup
    return

def random_choice():
    #random_choice lookup
    return

def sequence():
    #sequence lookup
    return

def subelements():
    #subelements lookup
    return

def template():
    #template lookup
    return

def together():
    #together lookup
    return

def unvault():
    #unvault lookup
    return

def url():
    #url lookup
    return

def varnames():
    #varnames lookup
    return

def vars():
    #vars lookup 
    return


def cmd():
    #cmd shell
    return

def powershell():
    #powershell shell
    return

def sh():
    #sh shell
    return


def debug():
    #debug strategy
    return

def free():
    #free strategy
    return

def host_pinned():
    #host_pinned strategy
    return

def linear():
    #linear strategy
    return


def abs():
    #abs all test
    return

def any():
    #any test
    return

def changed():
    #changed test
    return

def contains():
    #contains test
    return

def directory():
    #directory test
    return

def exists():
    #exists test
    return

def failed():
    #failed test
    return

def falsy():
    #falsy test
    return

def file():
    #file test
    return

def finished():
    #finished test
    return

def link():
    #link test
    return

def link_exists():
    #link_exists test
    return

def match():
    #match test
    return

def mount():
    #mount test
    return

def nan():
    #nan test
    return

def reachable():
    #reachable test
    return

def regex():
    #regex test
    return

def same_file():
    #same_file test
    return

def search():
    #search test
    return

def skipped():
    #skipped test
    return

def started():
    #started test
    return

def subset():
    #subset test
    return

def success():
    #success test
    return

def superset():
    #superset test
    return

def truthy():
    #truthy test
    return

def unreachable():
    #unreachable test
    return

def uri():
    #uri test
    return

def url():
    #url test
    return

def urn():
    #urn test
    return

def vault_encrypted():
    #vault_encrypted test
    return

def version():
    #version test
    return

def host_group_vars():
    #host_group_vars test
    return