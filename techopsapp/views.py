from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import test, rehber

class Another(View):

    tests = rehber.objects.all()
    output = ''
    for test in tests:
        output += f"DB'de {test.isim} kayıt mevcut.<br>"
    def get(self, request):
        return HttpResponse(self.output)



def first(request):
    return HttpResponse('First Message from views')
