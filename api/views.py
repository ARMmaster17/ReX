# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.decorators import api_view
from proxmoxer import ProxmoxAPI
import yaml

stream = open('proxmox.yml', 'r')
px_vars = yaml.full_load(stream)
proxmox = ProxmoxAPI(px_vars['proxmox_host'], user=px_vars['proxmox_user'], password=px_vars['proxmox_password'], verify_ssl=px_vars['proxmox_verify_ssl'])


@api_view(["GET"])
def trigger(request):
    hostname = request.GET['host']
    for vm in proxmox.cluster.resources.get(type='vm'):
        if vm['name'] == hostname:
            return JsonResponse(proxmox.nodes(vm['node']).lxc(vm['vmid']).status.reboot.post(), safe=False)
    return JsonResponse("An error occurred", safe=False)
