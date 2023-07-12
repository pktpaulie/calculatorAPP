import logging
from django.shortcuts import render
from .models import Computation
from .forms import CalculatorForm

# Configure logging basic info to use
logging.basicConfig(filename='logs.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


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
                logging.info("Using the addition logic of calculator Gp-3")
            elif operand == "-":
                answer = int(first_number) - int(second_number)
                logging.info("Using the subtraction logic of calculator Gp-3")
            elif operand == "/":
                try:
                    answer = int(first_number) / int(second_number)
                    logging.info("Using the division logic of calculator Gp-3")
                except ZeroDivisionError:
                    logging.info(
                        f"Error: Cannot divide {first_number} by zero")
            elif operand == "*":
                answer = int(first_number) * int(second_number)
                logging.info("Using the multiply logic of calculator Gp-3")
            elif operand == "^":
                answer = int(first_number) ** int(second_number)
                logging.info("using the modulus logic of calculator Gp-3")
            else:
                answer = "invalid operator"
            data = Computation(first_number=first_number, operation=operand,
                               second_number=second_number, answer=answer)
            data.save()
            data = Computation.objects.last()
            computations = Computation.objects.order_by("-id")[:5]

        # context = {
        #     'form': form,
        #     'data': data,
        #     'answer': answer,
        #     }

    return render(request, "index.html", {'answer': answer, "computations": computations})


def read_history(request):
    my_computations = Computation.objects.order_by("-id")[:5]
    return render(request, "index.html", {"computations": my_computations})
