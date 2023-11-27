from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path
from django.shortcuts import render
from django import forms
from .models import Game
from .models import Review

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

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.split(",")
                print(fields[0])
                #print(fields[1])
                #print(fields[2])
                #print(fields[3])
                #print(fields[4])

        form = CSVImportForm()
        context = {"form": form}
        return render(request, "admin/csv_upload.html", context)

# Register your models here.
admin.site.register(Review)
admin.site.register(Game, GameModelManager)