from django import forms
import models
from .models import PostAd


class PostAdForm(forms.ModelForm):
    error_css_class = 'error'

    school_name = forms.ChoiceField(choices=models.SCHOOLS, required=True)
    class_name = forms.ChoiceField(choices=models.CLASS, required=True)
    subject_name = forms.ChoiceField(choices=models.SUBJECTS, required=True)

    class Meta:
        model = PostAd
