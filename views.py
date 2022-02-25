
import requests
import pygal    
from django.shortcuts import render

def index(request):
    context = {

    }
    return render(request, 'base.html', context)

def chart(request):
    response = requests.get('https://api.github.com/users/kickstartcoding/repos')
    repos = response.json()

    chart = pygal.Pie()
    for repo_dict in repos:
        value = repo_dict["size"]
        label = repo_dict["name"]
        chart.add(label, value)
        chart_svg_as_datauri = chart.render_data_uri()
        context = {
            'github_repos': repos,
            "rendered_chart_svg_as_datauri": chart_svg_as_datauri,
        }
    return render(request, 'chart.html', context)


def all(request):
    response = requests.get('https://api.github.com/users/kickstartcoding/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'all.html', context)

