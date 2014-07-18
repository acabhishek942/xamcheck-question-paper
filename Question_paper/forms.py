from django import forms
from .models import PostAd

SCHOOLS = (
    ('CPS', 'Chirec Public School'),
    ('OPS', 'Oakridge Public School'),
    ('KPS', 'Kenndy Public School'),
    ('SPS', 'Silverstone Public School'),
)
CLASS = (
    ('C1', 'Class 1'),
    ('C2', 'Class 3'),
    ('C3', 'Class 4'),
    ('C4', 'Class 5'),
    ('C5', 'Class 6'),
)
SUBJECTS = (
    ('ENG', 'English'),
    ('MATHS', 'Mathematics'),
    ('SS', 'Social Science'),
    ('SCI', 'Science'),
    ('TEL', 'Telugu'),
    ('HIN', 'Hindi'),
)


class PostAdForm(forms.ModelForm):
    error_css_class = 'error'

    category = forms.ChoiceField(choices=SCHOOLS, required=True)
    location = forms.ChoiceField(choices=CLASS, required=True)

    class Meta:
        model = PostAd
