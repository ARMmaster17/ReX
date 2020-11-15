from proxmoxer import ProxmoxAPI
import yaml

stream = open('proxmox.yml', 'r')
px_vars = yaml.full_load(stream)
proxmox = ProxmoxAPI(px_vars['proxmox_host'], user=px_vars['proxmox_user'], password=px_vars['proxmox_password'], verify_ssl=px_vars['proxmox_verify_ssl'])


def proxmox_reboot(hostname):
    node_found = False
    for vm in proxmox.cluster.resources.get(type='vm'):
        if vm['name'] == hostname:
            proxmox.nodes(vm['node']).lxc(vm['vmid']).status.reboot.post()
            node_found = True
            break
    if not node_found:
        # TODO: Output some kind of error message to the logs.
        return
