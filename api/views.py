# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.decorators import api_view
from proxmoxer import ProxmoxAPI
import yaml
import os

stream = open('proxmox.yml', 'r')
px_vars = yaml.full_load(stream)
proxmox = ProxmoxAPI(px_vars['proxmox_host'], user=px_vars['proxmox_user'], password=px_vars['proxmox_password'], verify_ssl=px_vars['proxmox_verify_ssl'])


@api_view(["GET"])
def trigger(request):
    hostname = request.GET['host']
    actions = []
    if os.path.isfile('./hosts/' + hostname + '.yml'):
        actions = yaml.full_load(open('./hosts/' + hostname + '.yml'))
    else:
        actions = yaml.full_load(open('./hosts/default.yml'))
    for action in actions:
        # Perform action.
        if action['fix'] == 'proxmox.reboot':
            node_found = False
            for vm in proxmox.cluster.resources.get(type='vm'):
                if vm['name'] == hostname:
                    proxmox.nodes(vm['node']).lxc(vm['vmid']).status.reboot.post()
                    node_found = True
                    break
            if not node_found:
                return JsonResponse("An error occurred", safe=False)
        else:
            # No action is selected, Return with error.
            return JsonResponse("An error occurred", safe=False)
        # Check if issue is resolved.
        if action['check'] == 'none':
            # User doesn't want to check. Just return success.
            break
        else:
            # No checks were requested. Return OK.
            break
    return JsonResponse("200 OK", safe=False)
