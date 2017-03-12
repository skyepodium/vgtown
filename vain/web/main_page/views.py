from django.shortcuts import render
import requests

#key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIwODFkMDdkMC1lOTEzLTAxMzQtOWY1Yy0wMjQyYWMxMTAwMGIiLCJpc3MiOiJnYW1lbG9ja2VyIiwib3JnIjoic2t5ZXBvZGl1bS1nbWFpbC1jb20iLCJhcHAiOiIwODFiNTI4MC1lOTEzLTAxMzQtOWY1Yi0wMjQyYWMxMTAwMGIiLCJwdWIiOiJzZW1jIiwidGl0bGUiOiJ2YWluZ2xvcnkiLCJzY29wZSI6ImNvbW11bml0eSIsImxpbWl0IjoxMH0.jbBOxLbhaGaE4nB4YRNXm5ghpObWynuHNX2kIxx0ruA'

def main_page(request):
    return render(request, 'web/main_page/main_page.html')


'''
def main_page(request):
#    url = "https://api.dc01.gamelockerapp.com/shards/ea/matches?sort=-createdAt"
    url = "https://api.dc01.gamelockerapp.com/shards/ea/players?filter[playerNames]=haruholic"

    header = {
        "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIwODFkMDdkMC1lOTEzLTAxMzQtOWY1Yy0wMjQyYWMxMTAwMGIiLCJpc3MiOiJnYW1lbG9ja2VyIiwib3JnIjoic2t5ZXBvZGl1bS1nbWFpbC1jb20iLCJhcHAiOiIwODFiNTI4MC1lOTEzLTAxMzQtOWY1Yi0wMjQyYWMxMTAwMGIiLCJwdWIiOiJzZW1jIiwidGl0bGUiOiJ2YWluZ2xvcnkiLCJzY29wZSI6ImNvbW11bml0eSIsImxpbWl0IjoxMH0.jbBOxLbhaGaE4nB4YRNXm5ghpObWynuHNX2kIxx0ruA",
        "X-TITLE-ID": "semc-vainglory",
        "Accept": "application/vnd.api+json",
        "Accept-Encoding":"gzip"
    }

    r = requests.get(url, headers=header)

    return HttpResponse(r)
'''
