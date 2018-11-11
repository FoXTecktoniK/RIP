from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


def function_view(request):
    return HttpResponse('response from function view')


class ExampleClassBased(View):
    def get(self, request):
        return HttpResponse('response from class based view')


class ExampleStaticView(View):
    def get(self, request):
        return render(request, 'static_example.html')


def var_view(request):
    return render(request, 'first_example_var.html',{ 'my_variable': 'IU5-52'})

def var_tag(request):
    return render(request, 'view_tag.html', { 'list': [1, 2, 3, 1, 4, 5]})

class OrdersView(View):
    def get(self, request):
        data = {
            'orders':[
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