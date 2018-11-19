from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
import random


def function_view(request):
    return HttpResponse('response from function view')


class ExampleClassBased(View):
    def get(self, request):
        return HttpResponse('response from class based view')


class ExampleStaticView(View):
    def get(self, request):
        return render(request, 'static_example.html')


def var_view(request):
    return render(request, 'first_example_var.html', {'my_variable': 'RIP'})


def var_tag(request):
    list = [random.randint(0, 10) for _ in range(10)]
    return render(request, 'view_tag.html', {'list': list})


class OrdersView(View):
    def get(self, request):
        data = {
            'orders': [
                {'title': 'First order', 'id': 1},
                {'title': 'Second order', 'id': 2},
                {'title': 'Third order', 'id': 3},
                {'title': 'Fourth order', 'id': 4}
            ]
        }
        return render(request, 'orders.html', data)


class OrderView(View):
    def get(self, request, id):
        data = {
            'order':{
                'id': id
            }
        }
        return render(request, 'order.html', data)
