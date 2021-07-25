from django.forms import ModelForm
from home_app.models import *

class QueryForm(ModelForm):
    class Meta:
        model = Query
        fields = '__all__'
