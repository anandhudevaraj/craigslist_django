import requests

from django.shortcuts import render
from bs4 import BeautifulSoup
from requests.compat import quote_plus
from .models import Search

BASE_URL_CRAIGSLIST = "https://newyork.craigslist.org/search/bbb?query={}"
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'

# Create your views here.
def home(request):
    return render(request, 'base.html')


def new_search(request):
    search_item = request.POST.get('search')
    # Search.objects.create(search_field=search_item)
    required_search_url = BASE_URL_CRAIGSLIST.format(quote_plus(search_item))
    response = requests.get(required_search_url)
    soup = BeautifulSoup(response.text, features='html.parser')
    # post_titles = soup.find_all('a', {'class': 'result-title'})
    final_postings = []
    post_listings = soup.find_all('li', {'class': 'result-row'})
    for post in post_listings:
        post_title = post.find(class_='result-title').text
        post_id = post.find(class_='result-image').get('data-ids')
        if post_id is not None:
            image_url = BASE_IMAGE_URL.format(post_id.split(',')[0].split(':')[-1])
        else:
            image_url = 'https://craigslist.org/images/peace.jpg'
        post_url = post.find('a').get('href')
        post_price = 'N/A'
        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        final_postings.append((post_title,
                               post_url,
                               post_price,
                               image_url,
                               ))
    # some_list = [(item.text, item.get('href')) for item in post_titles]
    context = {
        'search_item': search_item,
        'final_postings': final_postings,
    }
    return render(request, 'my_app/new_search.html', context)
