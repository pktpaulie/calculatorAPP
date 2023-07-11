from django.shortcuts import render
from .models import Computation
from .forms import CalculatorForm

# Create your views here.


def index(request):
    return render(request, "index.html")


def calculate(request):
    answer = ''
    data = Computation.objects.all()

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
                try:
                    answer = int(first_number) / int(second_number)
                except ZeroDivisionError:
                    answer = "Error: Cannot divide by zero"
            elif operand == "*":
                answer = int(first_number) * int(second_number)
            elif operand == "^":
                answer = int(first_number) ** int(second_number)
            else:
                answer = "invalid operator"
            data = Computation(first_number=first_number, operation=operand, second_number=second_number, answer=answer)
            data.save()
            data = Computation.objects.last()
            computations = Computation.objects.order_by("-id")[:5]

    return render(request, "index.html", {'answer': answer, "computations": computations})


def read_history(request):
    my_computations = Computation.objects.order_by("-id")[:5]
    return render(request, "index.html", {"computations": my_computations})
