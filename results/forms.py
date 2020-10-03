from django import forms
from .models import Result
from bootstrap_datepicker.widgets import DatePicker
from clubs.models import Club
from events.models import EventInstance

class ResultForm(forms.ModelForm):

    class Meta:
        model = Result
        fields = (
        'eventinstance',
        'athletefirstname',
        'athletesurname',
        'athlete',
        'gender',
        'dateofbirth',
        'club'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        clubs = Club.objects.all()
        events = EventInstance.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in clubs]
        
        self.fields['club'].choices = friendly_names
       
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
