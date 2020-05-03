from django.shortcuts import render
import requests
import json
# Create your views here.
def home(request):
    url = "https://api.covid19api.com/summary"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = [{'Country': i['Country'],
             'TotalConfirmed':i['TotalConfirmed'] ,
             'NewConf': i['NewConfirmed'],
             'NewDeaths': i['NewDeaths'],
             'NewRecovered': i['NewRecovered'],
             'TotalRecovered':i['TotalRecovered']}
            for i in response.json()['Countries']]
    return render(request, 'covid19/home.html',{'response': data})