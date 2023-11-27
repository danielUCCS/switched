from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path
from django.shortcuts import render
from django import forms
from .models import Game
from .models import Review

import pandas as pd

class CSVImportForm(forms.Form):
    csv_upload = forms.FileField()

class GameModelManager(admin.ModelAdmin):

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path("upload-csv/", self.admin_site.admin_view(self.upload_csv))]
        return new_urls + urls

    def upload_csv(self, request):

        # If request is POST
        if request.method == 'POST':

            csv_file = request.FILES["csv_upload"]
            df = pd.read_csv(csv_file)
            data = df.values.tolist()

            print(data[0][0])
            print(data[1][0])
            print(data[2][0])
            print(data[3][0])
            print(data[4][0])

            newGame = Game(title = data[0][0], price = data[1][0], heading = data[2][0], description = data[3][0], img_src = data[4][0])
            newGame.save()
            
            """
            data = df.to_dict('list')

            print(data["title"])
            print(data["price"])
            print(data["heading"])
            print(data["description"])
            print(data["img src"])

            newGame = Game(title = data["title"], price = data["price"], heading = data["heading"], description = data["description"], img_src = data["img src"])
            newGame.save()

            title = data["title"]
            price = data["price"]
            heading = data["heading"]
            description = data["description"]
            img_src = data["img src"] """

        form = CSVImportForm()
        context = {"form": form}
        return render(request, "admin/csv_upload.html", context)

# Register your models here.
admin.site.register(Review)
admin.site.register(Game, GameModelManager)