from django.contrib import admin

from .models import Result

# Register your models here.



class ResultsAdmin(admin.ModelAdmin):
    list_display = (
        'eventinstance',
        'athletefirstname',
        'athletesurname',
        'athlete',
        'gender',
        'bibnumber',
        'agecat',
        'club',
        'chiptime',
        'guntime',
        'distance',
        'discipline',
        'event_format',
    )

    ordering = ('eventinstance',)


admin.site.register(Result, ResultsAdmin)
