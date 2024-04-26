from typing import Text
import requests
from django.shortcuts import render

def home(request):
  #Apply APIS
  response = requests.get('https://api.github.com/events')
  data = response.json()   
  result = data[10]["repo"]
  return render(request, 'templates/index.html', {'result': result})