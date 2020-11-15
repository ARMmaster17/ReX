# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.decorators import api_view
from api.actions import perform_actions


@api_view(["GET"])
def trigger(request):
    hostname = request.GET['host']
    # TODO: Verify that hostname is not empty/invalid.
    perform_actions(hostname)
    return JsonResponse("OK", safe=False)
