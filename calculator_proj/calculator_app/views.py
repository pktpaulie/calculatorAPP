from django.shortcuts import render
from .models import Computation
from .forms import *

# Create your views here.

def index(request):
    return render(request, "index.html")

def calculate(request):
    answer = ''
    computations = Computation.objects.all()
    form = CalculatorForm(request.POST)   
    if request.method == "POST":
           
        if form.is_valid():
            first_number = request.POST.get("first_number")
            operand = request.POST.get("operation")
            second_number = request.POST.get("second_number")
            if operand == "+":
                answer = int(first_number) + int(second_number)
            elif operand == "-":
                answer = int(first_number) - int(second_number)
            elif operand == "/":
                answer = int(first_number) / int(second_number)
            elif operand == "*":
                answer = int(first_number) * int(second_number)
            #return answer
            
            computations = Computation(first_number=first_number, operation=operand, second_number=second_number, answer=answer)
            computations.save()
            #form.save()


    context = {
        'form': form,
        
        }


    return render(request, "index.html", context)

def read_history(request):
    computations = Computation.objects.all().latest
    return render(request, "index.html", {"computations":computations})
