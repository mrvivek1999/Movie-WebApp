


from turtle import title
from django.shortcuts import render, redirect, get_object_or_404
from .models import  Movies 
import os
from .forms import  MoviesForm

# Create your views here.
def index(request):
    # 1.load the data from data#get all the categories
    movies = Movies.objects.all() # get all the images
    #2. pass the data into context
    ctx = {
       
        'movies': movies,
        'title': ' Movies Gallery',
    }
    #3. return the rendered template
    return render(request, 'index.html', ctx)
    

def add_Movies(request):
    form = MoviesForm()

    if request.method == 'POST':
        form = MoviesForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            descriptions= form.cleaned_data['descriptions']
            image = form.cleaned_data['image']
            img = Movies(title=title, image=image,descriptions=descriptions)
            img.save()
            return redirect('index')

    ctx ={
        'form': form,
        'title': 'Add/Upload Movies',
    }
    return render(request, 'add_Movies.html', ctx)

def view_movie(request, movie_id):
    try:
        item = Movies.objects.get(id=movie_id)
        ctx = {
            'mov': item,
            'title': item.title,
            'image': item.image,
            'descriptions': item.descriptions,
        }
        return render(request,'movie_view.html', ctx)
    except:
        return redirect('index')



def search_movies(request):

    ctx = {}
    query = request.GET.get('q')
    # print(query)
    ctx['movies'] = Movies.objects.filter(title__icontains=query)
    ctx['q'] = query
    return render(request, 'search.html',ctx)


    