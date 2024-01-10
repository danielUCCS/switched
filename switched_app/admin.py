from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path
from django.shortcuts import render
from django.shortcuts import redirect # DONT FORGET THIS
from django import forms
from .models import Game
from .models import Review
from .scraper import ScrapeURL

import pandas as pd

# Custom game form, only requests a URL
class GameForm(forms.Form):
    game_url = forms.URLField()

class GameAdmin(admin.ModelAdmin):

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path("create-game/", self.admin_site.admin_view(self.create_game))]
        return new_urls + urls

    def create_game(self, request):

        if request.method == 'POST':

            URL = request.POST.get('game_url')

            print("-----HERES THE URL-----")
            print(URL)

            data = ScrapeURL(URL)

            game = Game()

            game.game_url = URL
            game.title = data[0]
            game.price = data[1]
            game.heading = data[2]
            game.description = data[3]

            game.get_image_from_url(data[4])

            game.save()

            return redirect('admin:index')

        form = GameForm()
        context = {"form": form}
        return render(request, 'admin/game_form.html', context)

    '''
    def save_model(self, request, obj, form, change):
        
        # Call the scraper function to get game data, then save to object
        data = ScrapeURL(obj.game_url)

        obj.title = data[0]
        obj.price = data[1]
        obj.heading = data[2]
        obj.description = data[3]

        obj.get_image_from_url(data[4])
        
        super().save_model(request, obj, form, change)
    '''

# Register your models here.
admin.site.register(Review)
admin.site.register(Game, GameAdmin)