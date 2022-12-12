# food/views.py
from django.shortcuts import render, redirect
from flask import jsonify
from django.http import HttpResponse

def index(request):
    response = HttpResponse()
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    return response
#    return render(request, 'food/index.html', context=None)
