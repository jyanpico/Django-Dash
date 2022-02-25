
import requests
from django.shortcuts import render

def index(request):
    context = {

    }
    return render(request, 'base.html', context)

def all(request):
    context = {

    }
    return render(request, 'all.html', context)


def chart(request):
    response = requests.get('https://api.github.com/users/janeqhacker/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'chart.html', context)

