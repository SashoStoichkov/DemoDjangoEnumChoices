from django.db import models
from django.utils.translation import gettext_lazy as _

class Student(models.Model):

    class YearInSchool(models.TextChoices):
        FRESHMAN = 'FR', _('Freshman')
        SOPHOMORE = 'SO', _('Sophomore')
        JUNIOR = 'JR', _('Junior')
        SENIOR = 'SR', _('Senior')
        GRADUATE = 'GR', _('Graduate')

    name = models.CharField(default="", max_length=150)
    year_in_school = models.CharField(
        max_length=2,
        choices=YearInSchool.choices,
        default=YearInSchool.FRESHMAN,
    )

    def __str__(self):
        return self.name + " (" + self.year_in_school + ")"
