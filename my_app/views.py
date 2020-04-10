from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'base.html')


def new_search(request):
    search_item = request.POST.get('search')
    print(search_item)
    return render(request, 'my_app/new_search.html')
