from django.shortcuts import render
import requests

# Create your views here.

# def homepage(response):
#     return render(response,"main/home.html")

def edit(response):
    return render(response, "main/edit.html")
def fetch_posts(request):
    response = requests.get('https://danews.pl/api/')

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        posts = response.json()

        # Return the posts data
        return render(request, 'main/home.html', {'posts': posts})
    else:
        # Handle error
        raise Exception('Error fetching posts from API')


