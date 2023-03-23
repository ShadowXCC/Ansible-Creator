import yaml

def dowork(path):
    # Load the contents of the improperly formatted playbook
    with open(path, 'r') as f:
        playbook_contents = f.read()

    # Parse the playbook using PyYAML
    parsed_playbook = yaml.safe_load(playbook_contents)

    # Dump the parsed playbook back to YAML format with proper indentation
    formatted_playbook = yaml.dump(parsed_playbook, default_flow_style=False, indent=2)

    # Write the formatted playbook back to file
    with open(path, 'w') as f:
        f.write(formatted_playbook)  