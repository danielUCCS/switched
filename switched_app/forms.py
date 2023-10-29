from django.forms import ModelForm
from .models import Review

#create class for project form
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'description', 'rating')