from django.contrib import admin
from .models import Game
from django.template.response import TemplateResponse
from django.urls import path
from django.shortcuts import render
from django.shortcuts import redirect 
from django import forms
from .scraper import ScrapeURL


from .models import Review

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
            data = ScrapeURL(URL)

            # Create new game 
            game = Game()

            game.title = data[0]
            game.price = data[1]
            game.heading = data[2]
            game.description = data[3]

            game.save()

            return redirect('admin:index')

        form = GameForm()
        context = {"form": form}
        return render(request, 'admin/game_form.html', context)

# Register your models here.
admin.site.register(Game, GameAdmin)
admin.site.register(Review)

