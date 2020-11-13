# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(["GET"])
def welcome(request):
    content = {"message": "Welcome to the BookStore!"}
    return JsonResponse(content)
