from django.http import JsonResponse 
from rest_framework.decorators import api_view
from django.shortcuts import render

# Create your views here.
response = {
    'slackUsername': 'Jacob Peter',
    'backend': True,
    'age': 24,
    'bio': 'I am from ogun state,I am a backend developer'
}

@api_view(['Get'])
def Home(request):
    return JsonResponse(response)