from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path
from django.shortcuts import render
from django import forms
from .models import Game
from .models import Review
from .scraper import ScrapeURL

import pandas as pd

# Custom game form, only requests a URL
class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['game_url']

class GameAdmin(admin.ModelAdmin):
    form = GameForm

    def save_model(self, request, obj, form, change):
        
        data = ScrapeURL(obj.game_url)

        obj.title = data[0]
        obj.price = data[1]
        obj.heading = data[2]
        obj.description = data[3]

        obj.get_image_from_url(data[4])
        
        super().save_model(request, obj, form, change)

# Register your models here.
admin.site.register(Review)
admin.site.register(Game, GameAdmin)