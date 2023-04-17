import multiprocessing
import re
from collections import Counter

# MODULES = ["add_host", "apt", "apt_key", "apt_repository", "assemble", "assert", "async_status", "blockinfile", "command", "copy", "cron", "debconf", "debug", "dnf", "dpkg_selections", "expect", "fail", "fetch", "file", "gather_facts", "get_url", "getent", "git", "group", "group_by", "hostname", "import_playbook", "import_role", "import_tasks", "include", "include_role", "include_tasks", "include_vars", "iptables", "known_hosts", "lineinfile", "meta", "package", "package_facts", "pause", "ping", "pip", "raw", "reboot", "replace", "rpm_key", "script", "service", "service_facts", "set_fact", "set_stats", "setup", "shell", "slurp", "stat", "subversion", "systemd", "systemd_service", "sysvinit", "tempfile", "template", "unarchive", "uri", "user", "validate_argument_spec", "wait_for", "wait_for_connection", "yum", "yum_repository"]
# BECOMES = ["runas", "su", "sudo"]
# CACHES = ["jsonfile", "memory"]
# CALLBACKS = ["default", "junit", "minimal", "oneline", "tree"]
# CONNECTIONS = ["local", "paramiko_ssh", "psrp", "ssh", "winrm"]
# FILTER = ["b64decode", "b64encode", "basename", "bool", "checksum", "combinations", "combine", "comment", "dict2items", "difference", "dirname", "expanduser", "expandvars", "extract", "fileglob", "flatten", "from_json", "from_yaml", "from_yaml_all", "hash", "human_readable", "human_to_bytes", "intersect", "items2dict", "log", "mandatory", "md5", "password_hash", "path_join", "permutations", "pow", "product", "quote", "random", "realpath", "regex_escape", "regex_findall", "regex_replace", "regex_search", "rekey_on_member", "relpath", "root", "sha1", "shuffle", "splitext", "strftime", "subelements", "symmetric_difference", "ternary", "to_datetime", "to_json", "to_nice_json", "to_nice_yaml", "to_uuid", "to_yaml", "type_debug", "union", "unique", "unvault", "urlsplit", "vault", "win_basename", "win_dirname", "win_splitdrive", "zip", "zip_longest"]
# INVENTORY = ["advanced_host_list", "auto", "constructed", "generator", "host_list", "ini", "script", "toml", "yaml"]
# LOOKUPS = ["config", "csvfile", "dict", "env", "file", "fileglob", "first_found", "indexed_items", "ini", "inventory_hostnames", "lines", "list", "nested", "password", "pipe", "random_choice", "sequence", "subelements", "template", "together", "unvault", "url", "varnames", "vars"]
# SHELLS = ["cmd", "powershell", "sh"]
# STRATEGIES = ["debug", "free", "host_pinned", "linear"]
# TESTS = ["abs", "all", "any", "changed", "contains", "directory", "exists", "failed", "falsy", "file", "finished", "link", "link_exists", "match", "mount", "nan", "reachable", "regex", "same_file", "search", "skipped", "started", "subset", "success", "superset", "truthy", "unreachable", "uri", "url", "urn", "vault_encrypted", "version", "host_group_vars"]
# bigDaddy = MODULES + BECOMES + CACHES + CALLBACKS + CONNECTIONS + FILTER + INVENTORY + LOOKUPS + SHELLS + STRATEGIES + TESTS


bigDaddy = ['add_host', 'apt', 'apt_key', 'apt_repository', 'assemble', 'assert', 'async_status', 'blockinfile', 'command', 'copy', 'cron', 'debconf', 'debug', 'dnf', 'dpkg_selections', 'expect', 'fail', 'fetch', 'file', 'gather_facts', 'get_url', 'getent', 'git', 'group', 'group_by', 'hostname', 'import_playbook', 'import_role', 'import_tasks', 'include', 'include_role', 'include_tasks', 'include_vars', 'iptables', 'known_hosts', 'lineinfile', 'meta', 'package', 'package_facts', 'pause', 'ping', 'pip', 'raw', 'reboot', 'replace', 'rpm_key', 'script', 'service', 'service_facts', 'set_fact', 'set_stats', 'setup', 'shell', 'slurp', 'stat', 'subversion', 'systemd', 'systemd_service', 'sysvinit', 'tempfile', 'template', 'unarchive', 'uri', 'user', 'validate_argument_spec', 'wait_for', 'wait_for_connection', 'yum', 'yum_repository', 'runas', 'su', 'sudo', 'jsonfile', 'memory', 'default', 'junit', 'minimal', 'oneline', 'tree', 'local', 'paramiko_ssh', 'psrp', 'ssh', 'winrm', 'b64decode', 'b64encode', 'basename', 'bool', 'checksum', 'combinations', 'combine', 'comment', 'dict2items', 'difference', 'dirname', 'expanduser', 'expandvars', 'extract', 'fileglob', 'flatten', 'from_json', 'from_yaml', 'from_yaml_all', 'hash', 'human_readable', 'human_to_bytes', 'intersect', 'items2dict', 'log', 'mandatory', 'md5', 'password_hash', 'path_join', 'permutations', 'pow', 'product', 'quote', 'random', 'realpath', 'regex_escape', 'regex_findall', 'regex_replace', 'regex_search', 'rekey_on_member', 'relpath', 'root', 'sha1', 'shuffle', 'splitext', 'strftime', 'subelements', 'symmetric_difference', 'ternary', 'to_datetime', 'to_json', 'to_nice_json', 'to_nice_yaml', 'to_uuid', 'to_yaml', 'type_debug', 'union', 'unique', 'unvault', 'urlsplit', 'vault', 'win_basename', 'win_dirname', 'win_splitdrive', 'zip', 'zip_longest', 'advanced_host_list', 'auto', 'constructed', 'generator', 'host_list', 'ini', 'script', 'toml', 'yaml', 'config', 'csvfile', 'dict', 'env', 'file', 'fileglob', 'first_found', 'indexed_items', 'ini', 'inventory_hostnames', 'lines', 'list', 'nested', 'password', 'pipe', 'random_choice', 'sequence', 'subelements', 'template', 'together', 'unvault', 'url', 'varnames', 'vars', 'cmd', 'powershell', 'sh', 'debug', 'free', 'host_pinned', 'linear', 'abs', 'all', 'any', 'changed', 'contains', 'directory', 'exists', 'failed', 'falsy', 'file', 'finished', 'link', 'link_exists', 'match', 'mount', 'nan', 'reachable', 'regex', 'same_file', 'search', 'skipped', 'started', 'subset', 'success', 'superset', 'truthy', 'unreachable', 'uri', 'url', 'urn', 'vault_encrypted', 'version', 'host_group_vars']

def searchModules(searchTerm):
    """
    Searches for items in a list 'bigDaddy' that match a given search term using regular expressions, fuzzy matching, and spelling correction.

    Args:
    searchTerm (str): The term to search for in the list 'bigDaddy'.

    Returns:
    results (list): A list of items from 'bigDaddy' that match the search term. If no matches are found using regular expressions, fuzzy matching, or spelling correction, an empty list is returned.
    """
    results = []

    for item in bigDaddy:
        if re.search(searchTerm, item):
            results.append(item)
        # else:
        #     match = fuzzIt(searchTerm, bigDaddy, threshold=60)
        #     print(match)
        #     if match == item:
        #         print(match)
        #         results.append(match)
        # elif fuzz(searchTerm, bigDaddy, threshold=60) == item:
        #     print(fuzz(searchTerm, bigDaddy, threshold=60))
        #     results.append(fuzz(searchTerm, bigDaddy, threshold=60))
        #fuzz(input_str, search_list, threshold=60)
        elif searchTerm in item:
            results.append(item)
        elif correction(searchTerm) == item:
            print(correction(searchTerm))
            results.append(correction(searchTerm))

    return results

# PETER NORVIG'S (Google Exec) VERY SIMPLIFIED "DID YOU MEAN?"
# ------------------------------------------------------------

"""
Tokenizes a given text string into words using regular expressions.

Args:
text (str): The string of text to tokenize.

Returns:
A list of lowercase words found in the text string.
"""
def words(text): return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open('dictionary.txt').read()))

def P(word, N=sum(WORDS.values())): 
    """
    Calculates the probability of a given word in the dictionary.

    Args:
    word (str): The word to calculate the probability of.
    N (int): The sum of all word counts in the dictionary. Default is the total count of all words in the dictionary.

    Returns:
    The probability of the given word in the dictionary, calculated as the count of the word divided by the total count of all words in the dictionary.
    """
    return WORDS[word] / N

def correction(word): 
    """
    Returns the most probable spelling correction for a given word.

    Args:
    word (str): The word to correct.

    Returns:
    The most probable spelling correction for the given word, based on the dictionary of WORDS.
    """
    return max(candidates(word), key=P)

def candidates(word): 
    """
    Generates a list of possible spelling corrections for a given word.

    Args:
    word (str): The word to generate corrections for.

    Returns:
    A set of possible spelling corrections for the given word, based on the dictionary of WORDS. The set includes the original word, words with one edit distance away from the original word, words with two edit distances away from the original word, and words with three edit distances away from the original word.
    """
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or known(edits3(word)) or [word])

def known(words): 
    """
    Returns a set of words that are present in the dictionary of WORDS.

    Args:
    words (list): A list of words to check for presence in the dictionary.

    Returns:
    A set of words that are present in the dictionary of WORDS.
    """
    return set(w for w in words if w in WORDS)

def edits1(word):
    """
    Generates a set of all possible spelling corrections that are one edit distance away from a given word.

    Args:
    word (str): The word to generate corrections for.

    Returns:
    A set of all possible spelling corrections that are one edit distance away from the given word. Edits include deletions, transpositions, replacements, and insertions of letters.
    """
    letters    = 'abcdefghijklmnopqrstuvwxyz_'
    # letters    = 'abcdefghijklmnopqrstuvwxyz_12456'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    """
    Generate a set of all possible edits that can be made to the given `word`
    such that each edit is at most two edits away from the original word.
    This is done by generating all possible edits with one edit, and then
    generating all possible edits with one edit on those one-edit words.

    Parameters:
    word (str): The word for which the edits are to be generated.

    Returns:
    set: A set of strings, each string being a possible edit that is at most
    two edits away from the original word.
    """

    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

#Has not been tested
def edits3(word): 
    """
    Generate a set of all possible edits that can be made to the given `word`
    such that each edit is at most three edits away from the original word.
    This is done by generating all possible edits with one edit, then all
    possible edits with one edit on those one-edit words, and finally all
    possible edits with one edit on those two-edit words.

    Parameters:
    word (str): The word for which the edits are to be generated.

    Returns:
    set: A set of strings, each string being a possible edit that is at most
    three edits away from the original word.
    """
    return (e3 for e1 in edits1(word) for e2 in edits1(e1) for e3 in edits1(e2))

# https://stackoverflow.com/questions/307291/how-does-the-google-did-you-mean-algorithm-work
# https://stackoverflow.com/questions/41424/how-do-you-implement-a-did-you-mean
# http://www.norvig.com/spell-correct.html
# https://googlesystem.blogspot.com/2007/04/simplified-version-of-googles-spell.html'
# https://www.geeksforgeeks.org/how-does-the-googles-did-you-mean-algorithm-work/
# https://blog.apilayer.com/how-to-easily-implement-did-you-mean-this-in-your-app/
# https://github.com/SylvainDe/DidYouMean-Python
# Actual google search for it: https://www.google.com/search?q=did+you+mean+search+python&rlz=1C1GCEA_enUS1007US1007&oq=did+you+mean+search+python&aqs=chrome..69i57j33i160j33i22i29i30l7.3975j0j7&sourceid=chrome&ie=UTF-8

# ChatGPT code #1
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def fuzzIt(input_str, search_list, threshold=70):
    """Search for input string in search list and return a list of near matches"""
    matches = []
    for item in search_list:
        ratio = fuzz.token_set_ratio(input_str, item)
        if ratio >= threshold:
            #matches.append((item, ratio)) #This line shows % of matching
            matches.append(item)
    matches.sort(key=lambda x: x[1], reverse=True)
    return matches

# Example usage
#search_list = ['apple', 'banana', 'orange', 'pear', 'kiwi']
#input_str = 'appl'
#matches = fuzz(input_str, search_list, threshold=60)
#print(matches)

# ChatGPT code #2
# import re
# from fuzzywuzzy import fuzz
# from fuzzywuzzy import process

# def search_string(input_str, search_list, threshold=70):
#     """Search for input string in search list and return a list of near matches"""
#     # Remove non-alphanumeric characters and convert to lowercase
#     input_str = re.sub(r'\W+', '', input_str).lower()
#     matches = []
#     for item in search_list:
#         # Remove non-alphanumeric characters and convert to lowercase
#         item = re.sub(r'\W+', '', item).lower()
#         ratio = fuzz.token_set_ratio(input_str, item)
#         if ratio >= threshold:
#             matches.append((item, ratio))
#     matches.sort(key=lambda x: x[1], reverse=True)
#     return matches

# # Example usage
# search_list = ['apple', 'banana', 'orange', 'pear', 'kiwi']
# input_str = 'ApplE'
# matches = search_string(input_str, search_list, threshold=60)
# print(matches)