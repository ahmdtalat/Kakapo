from django.forms import ModelForm, TextInput
from weather.models import City


class CityForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(CityForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = False  # hiding the name field label

    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'City Name'})
        }
