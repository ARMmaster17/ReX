import yaml
import os
from api.proxmox import proxmox_reboot
from pythonping import ping


def load_actions(hostname):
    if os.path.isfile('./hosts/' + hostname + '.yml'):
        return yaml.full_load(open('./hosts/' + hostname + '.yml'))
    else:
        return yaml.full_load(open('./hosts/default.yml'))


def perform_actions(hostname):
    actions = load_actions(hostname)
    for action in actions:
        # Perform action.
        if action['fix'] == 'proxmox.reboot':
            proxmox_reboot(hostname)
        else:
            # No action is selected, Return with error.
            # TODO: Output some kind of error message to the logs.
            return
        # Check if issue is resolved.
        if action['check'] == 'none':
            # User doesn't want to check. Move on to next item (if it exists).
            continue
        elif action['check'] == 'ping':
            # Ping the hostname and check if it is up.
            result = ping(hostname)
            if result.packet_loss == 0:
                # Host is back up. Exit action list.
                return
            else:
                # Host is not up, or the connection is faulty. Move on to next item.
                continue
        else:
            # No checks were requested. Move on to next item (if it exists).
            continue
