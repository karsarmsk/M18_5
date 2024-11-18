from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

# class platform(TemplateView):
#     template_name ='platform.html'
# class games(TemplateView):
#     template_name = 'games.html'
# class cart(TemplateView):
#     template_name = 'cart.html'

def platform(request):
    return render(request, 'platform.html')
def games(request):
    return render(request, 'games.html')
def cart(request):
    return render(request, 'cart.html')