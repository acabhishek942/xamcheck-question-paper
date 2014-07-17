from django.db import models


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


class PostAd(models.Model):

    school_name = models.CharField(max_length=3, choices=SCHOOLS)
    class_name = models.CharField(max_length=3, choices=CLASS)
    subject_name = models.CharField(max_length=3, choices=SUBJECTS)
