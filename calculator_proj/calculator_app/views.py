from django.shortcuts import render
from .models import Computation
from .forms import *

# Create your views here.

def index(request):
    return render(request, "index.html")

def calculate(request):
    answer = ''
    if request.method == "POST":
        form = CalculatorForm(request.POST)
            
        if form.is_valid():
            first_number = request.GET.get("first_number")
            operand = request.GET.get("operation")
            second_number = request.GET.get("second_number")
            answer = request.GET.get("answer")
            if operand is "+":
                answer = int(first_number) + int(second_number)
            elif operand is "-":
                answer = int(first_number) - int(second_number)
            elif operand is "/":
                answer = int(first_number) / int(second_number)
            elif operand is "*":
                answer = int(first_number) * int(second_number)
            #return answer
            form.save()


    context = {
        'form': form,
        'answer': answer,
        }


    return render(request, "index.html", context)

def read_history(request):
    computations = Computation.objects.all().latest
    return render(request, "index.html", {"computations":computations})
