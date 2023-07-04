from django import forms
# from django.forms import ModelForm
# from .models import Computation

""" class CalculatorForm(ModelForm):
    class Meta:
        model = Computation

        fields = ["first_number", "operation", "second_number", "answer"]
        # fields = "__all__" """


class CalculatorForm(forms.Form):
    first_number = forms.CharField(label="first_number", max_length=100)
    operation = forms.CharField(label="operation", max_length=100)
    second_number = forms.CharField(label="second_number", max_length=100)
