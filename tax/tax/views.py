from django.shortcuts import render
from django.http import HttpResponse
def home(req):
    return HttpResponse("<h1>This is a site to calculate tax</h1>")
def calculate_tax(req, num):
    t_rate = 0.15
    sum = num * (1 + t_rate)
    return HttpResponse(f"<h1>The total price after tax is {sum}</h1>")
def tax_rate(req):
    t_rate = 0.15
    return render(req, 'tax_rate.html', {'tax_rate': t_rate})