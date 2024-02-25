from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
import requests
from django.shortcuts import redirect


def edit(response):
    return render(response, "main/edit.html")


def fetch_posts(request):
    response = requests.get('https://danews.pl/api/')

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract only the 'results'
        posts = data.get('results', [])  # Use get() to handle cases where 'results' key might not exist
        canonical_url = request.build_absolute_uri()

        return render(request, 'main/home.html', {'posts': posts, 'canonical_url': canonical_url})
    else:
        # Handle error
        raise Exception('Error fetching posts from API')


def login_view(request):
    next_url = request.GET.get('next',
                               '/api/')  # Pobierz adres docelowy z parametru GET 'next', jeśli nie ma ustaw domyślną wartość na '/home/'

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(next_url)  # Przekierowanie do adresu docelowego po zalogowaniu
    else:
        form = AuthenticationForm(request)
    return render(request, 'main/login.html', {'form': form})  # Przekazanie adresu docelowego do szablonu logowania
