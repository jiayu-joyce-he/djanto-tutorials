from django.shortcuts import render
from django.http import HttpResponse

# Each view must return a http object;
# In order for this view to be seen, we need to map this view to the urls,py file
def index(request):
    # use my_dic as a context that provides variable name and values
    my_dic = {'insert_me': "Helle, I'm from views.py from first_app/index.html!!"}
    return render(request, 'first_app/index.html', context= my_dic)
