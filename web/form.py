from django import forms
from .models import sampleweb


class crufdform(forms.ModelForm):
    class Meta:
        model=sampleweb
        fields = '__all__'