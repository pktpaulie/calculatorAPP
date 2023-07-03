from django.forms import ModelForm
from .models import Computation

class CalculatorForm(ModelForm):
    class Meta:
        model = Computation
        fields = ["first_number", "operation", "second_number", "answer"]
        #fields = "__all__"