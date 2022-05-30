from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Category, Actor, RatingStar, Rating, Genre, Movie, MovieShots, Reviews


class MoviesView(ListView):
    """Список фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    """Полное описание фильма"""
    model = Movie
    slug_field = "url"


class AddReview(View):
    """ Добавление отзыва"""
    def post(self, request, pk):
        print(request.POST)
        return redirect("/")
