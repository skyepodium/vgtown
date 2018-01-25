from django.shortcuts import render
import requests
from vain.banner.models import BannerModel
from django.http import HttpResponse
import json
from django.template import RequestContext
import http.client, urllib.request, urllib.parse, urllib.error, base64
#key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIwODFkMDdkMC1lOTEzLTAxMzQtOWY1Yy0wMjQyYWMxMTAwMGIiLCJpc3MiOiJnYW1lbG9ja2VyIiwib3JnIjoic2t5ZXBvZGl1bS1nbWFpbC1jb20iLCJhcHAiOiIwODFiNTI4MC1lOTEzLTAxMzQtOWY1Yi0wMjQyYWMxMTAwMGIiLCJwdWIiOiJzZW1jIiwidGl0bGUiOiJ2YWluZ2xvcnkiLCJzY29wZSI6ImNvbW11bml0eSIsImxpbWl0IjoxMH0.jbBOxLbhaGaE4nB4YRNXm5ghpObWynuHNX2kIxx0ruA'

def main_page(request):
    banners = BannerModel.objects.all().order_by('-id')

    return render(request, 'web/main_page/main_page.html',{
        'banners':banners
    })

def api(request):
#    url = "https://api.dc01.gamelockerapp.com/shards/ea/matches?sort=-createdAt"
#    url = "https://api.dc01.gamelockerapp.com/shards/ea/players?filter[playerNames]=haruholic"
#    url = "https://api.dc01.gamelockerapp.com/shards/ea/matches"
#    url = "https://api.dc01.gamelockerapp.com/shards/ea/players/f2043322-3799-11e6-b12a-062cb73cdbb1"
    url = "https://api.dc01.gamelockerapp.com/shards/ea/players"
#    url = "https://api.dc01.gamelockerapp.com/shards/ea/matches"

    header = {
        "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIwODFkMDdkMC1lOTEzLTAxMzQtOWY1Yy0wMjQyYWMxMTAwMGIiLCJpc3MiOiJnYW1lbG9ja2VyIiwib3JnIjoic2t5ZXBvZGl1bS1nbWFpbC1jb20iLCJhcHAiOiIwODFiNTI4MC1lOTEzLTAxMzQtOWY1Yi0wMjQyYWMxMTAwMGIiLCJwdWIiOiJzZW1jIiwidGl0bGUiOiJ2YWluZ2xvcnkiLCJzY29wZSI6ImNvbW11bml0eSIsImxpbWl0IjoxMH0.jbBOxLbhaGaE4nB4YRNXm5ghpObWynuHNX2kIxx0ruA",
        "X-TITLE-ID": "semc-vainglory",
        "Accept": "application/vnd.api+json",
        "Accept-Encoding":"gzip"
        #GZIP은 응답을 압축한다.
    }

    query = {
#        "sort": "-createdAt",
#        "filter[playerNames]": "haruholic",
#        "filter[createdAt-start]": "2017-10-22T13:25:30Z",
#        "page[limit]": "3"
#        "sort": "-createdAt",
#        "filter[playerNames]": "ProsAreSoBad",
        "filter[playerNames]": "haruholic",
#        "filter[playerIds]":"f2043322-3799-11e6-b12a-062cb73cdbb1",
#        "filter[playerIds]":"6a7479d6-5c83-11e5-8755-0628b69bf6d1",

#        "filter[createdAt-start]": "2017-02-28T13:25:30Z",
#        "filter[createdAt-start]": "2017-01-06T20:30:08Z",
#        "filter[createdAt-end]": "2017-06-28T13:25:30Z",
#        "filter[createdAt-end]": "",
#        "page[offset]":"2",
#        "page[limit]": "50"
    }

    r = requests.get(url, headers=header, params=query)
#    a = data["type"]
#    r = json.load(r)

#    r = r.json()
#    r = r["data"][0]["type"]
#    r = r["data"][0]["attributes"]["name"]
    return HttpResponse(r)




def apims(request):
    url = 'https://southcentralus.api.cognitive.microsoft.com/customvision/v1.0/Prediction/a6935af8-f509-4e24-87b0-ab2b681cb482/url?iterationId=dd3054f7-b975-4943-abf3-7aeef817204c'

    header = {
        'Prediction-Key': '58a0ad9c77734a45a6a992932e20b7bd',
        'Content-Type': 'application/json',
    }

    data = {
        'Url': 'http://blogfiles13.naver.net/20120409_242/viadelcorea_1333928398149DUpP7_JPEG/simonskreddernes2.jpg',
    }

    response = requests.post(url, headers=header, data=json.dumps(data))
    result = json.loads(response.content.decode("utf-8"))
    print(json.dumps(result))
    return HttpResponse(json.dumps(result))


def api2(request):
    url = "https://southcentralus.api.cognitive.microsoft.com/customvision/v1.0/Prediction/a6935af8-f509-4e24-87b0-ab2b681cb482/url?iterationId=dd3054f7-b975-4943-abf3-7aeef817204c"

    headers = {
    # Request headers
        "Prediction-Key": "58a0ad9c77734a45a6a992932e20b7bd",
        "Content-Type": "application/json",
    }

    params = urllib.parse.urlencode({
        # Request parameters
        "Url": "http://blogfiles13.naver.net/20120409_242/viadelcorea_1333928398149DUpP7_JPEG/simonskreddernes2.jpg",
    })

    conn = http.client.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')
    conn.request("POST", url, params, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
    return HttpResponse(1)
