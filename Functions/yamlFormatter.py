import yaml

def format_playbook(path):
    """Loads, parses, and formats a YAML playbook file at the given path.

    Args:
        path (str): The path to the YAML playbook file.

    Returns:
        str: The formatted YAML playbook.

    Raises:
        IOError: If there was an error reading or writing the file.
    """
    with open(path, 'r') as f:
        playbook_contents = f.read()

    parsed_playbook = yaml.safe_load(playbook_contents)

    formatted_playbook = yaml.dump(parsed_playbook, indent=2)

    return formatted_playbook

def toFile(path):
    """Formats the YAML playbook file at the given path and writes the result back to the file.

    Args:
        path (str): The path to the YAML playbook file.

    Raises:
        IOError: If there was an error reading or writing the file.
    """
    formatted_playbook = format_playbook(path)

    with open(path, 'w') as f:
        f.write(formatted_playbook)
