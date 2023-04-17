from . import playWriterHelpers as PWH

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

funcs = {'runas':runas, 'su':su, 'sudo':sudo, 'jsonfile':jsonfile, 'memory':memory, 'default':default, 'junit':junit, 'minimal':minimal, 'oneline':oneline, 'tree':tree, 'local':local, 'paramiko_ssh':paramiko_ssh, 'psrp':psrp, 'ssh':ssh, 'winrm':winrm, 'b64decode':b64decode, 'b64encode':b64encode, 'basename':basename, 'bool':bool, 'checksum':checksum, 'combinations':combinations, 'combine':combine, 'comment':comment, 'dict2items':dict2items, 'difference':difference, 'dirname':dirname, 'expanduser':expanduser, 'expandvars':expandvars, 'extract':extract, 'fileglob':fileglob, 'flatten':flatten, 'from_json':from_json, 'from_yaml':from_yaml, 'from_yaml_all':from_yaml_all, 'hash':hash, 'human_readable':human_readable, 'human_to_bytes':human_to_bytes, 'intersect':intersect, 'items2dict':items2dict, 'log':log, 'mandatory':mandatory, 'md5':md5, 'password_hash':password_hash, 'path_join':path_join, 'permutations':permutations, 'pow':pow, 'product':product, 'quote':quote, 'random':random, 'realpath':realpath, 'regex_escape':regex_escape, 'regex_findall':regex_findall, 'regex_replace':regex_replace, 'regex_search':regex_search, 'rekey_on_member':rekey_on_member, 'relpath':relpath, 'root':root, 'sha1':sha1, 'shuffle':shuffle, 'splittext':splittext, 'strftime':strftime, 'subelements':subelements, 'symmetric_difference':symmetric_difference, 'ternary':ternary, 'to_datetime':to_datetime, 'to_json':to_json, 'to_nice_json':to_nice_json, 'to_nice_yaml':to_nice_yaml, 'to_uuid':to_uuid, 'to_yaml':to_yaml, 'type_debug':type_debug, 'union':union, 'unique':unique, 'unvault':unvault, 'urlsplit':urlsplit, 'vault':vault, 'win_basename':win_basename, 'win_dirname':win_dirname, 'win_splitdrive':win_splitdrive, 'zip':zip, 'zip_longest':zip_longest, 'advanced_host_list':advanced_host_list, 'auto':auto, 'constructed':constructed, 'generator':generator, 'host_list':host_list, 'ini':ini, 'script':script, 'toml':toml, 'yaml':yaml, 'config':config, 'csvfile':csvfile, 'dict':dict, 'env':env, 'file':file, 'fileglob':fileglob, 'first_found':first_found, 'indexed_items':indexed_items, 'ini':ini, 'inventory_hostnames':inventory_hostnames, 'lines':lines, 'list':list, 'nested':nested, 'password':password, 'pipe':pipe, 'random_choice':random_choice, 'sequence':sequence, 'subelements':subelements, 'template':template, 'together':together, 'unvault':unvault, 'url':url, 'varnames':varnames, 'vars':vars, 'cmd':cmd, 'powershell':powershell, 'sh':sh, 'debug':debug, 'free':free, 'host_pinned':host_pinned, 'linear':linear, 'abs':abs, 'all':all, 'any':any, 'changed':changed, 'contains':contains, 'directory':directory, 'exists':exists, 'failed':failed, 'falsy':falsy, 'file':file, 'finished':finished, 'link':link, 'link_exists':link_exists, 'match':match, 'mount':mount, 'nan':nan, 'reachable':reachable, 'regex':regex, 'same_file':same_file, 'search':search, 'skipped':skipped, 'started':started, 'subset':subset, 'success':success, 'superset':superset, 'truthy':truthy, 'unreachable':unreachable, 'uri':uri, 'url':url, 'urn':urn, 'vault_encrypted':vault_encrypted, 'version':version, 'host_group_vars':host_group_vars}
