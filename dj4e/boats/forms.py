from django.forms import ModelForm
from boats.models import Type

# Create the form class.
class TypeForm(ModelForm):
    class Meta:
        model = Type
        fields = '__all__'