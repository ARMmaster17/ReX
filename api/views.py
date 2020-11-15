# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from urllib.parse import urlparse

from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.utils import json

from api.actions import perform_actions


@api_view(["GET"])
def trigger(request):
    hostname = request.GET['host']
    # TODO: Verify that hostname is not empty/invalid.
    perform_actions(hostname)
    return JsonResponse("OK", safe=False)


@api_view(["POST"])
def vigil(request):
    json_payload = json.loads(request.body)
    for replica in json_payload['replicas']:
        if not json_payload['status'] == "dead":
            continue
        domain = urlparse(replica).netloc
        perform_actions(domain)
    return JsonResponse("OK", safe=False)
