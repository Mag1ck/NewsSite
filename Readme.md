# NewsSite

Overwiew

This project is a site that resembles TikTok in its design and functionality. Users can add news using the API endpoints 'http://127.0.0.1:8000/edit' or 'http://127.0.0.1:8000/api' (the latter option is less preferable as it doesn't support including images and videos). However, before adding news, users need to be logged in. They can create an account using the link 'http://127.0.0.1:8000/login'. Once logged in, they can access the admin interface via 'http://127.0.0.1:8000/admin' (ensure you've created a superuser before).

The site features smooth scrolling using either the up and down arrow keys or the mouse wheel. Additionally, infinite scrolling has been implemented to enhance the browsing experience. Posts are sorted by date, with the newest posts displayed first.

# Instalation

Effortless setup with just one command:

pip install -r requirements.txt


# Usage

Navigate to the directory containing the manage.py file and run the following command to start the server:
python manage.py runserver

# Live version

You can explore the online version of the site at danews.pl.
