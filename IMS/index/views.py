from django.shortcuts import render
from django.http import HttpResponse


#TODO сделать вывод общей таблицы
def index(request):
    return HttpResponse('<h1>Hello World!</h1>')


def test(request):
    return HttpResponse('<h2>Test page...</h2>')


#TODO Реализовать механизм поиска
def search(request):
    return HttpResponse('<h2>Поиск</h2>')


#TODO Реализовать механизм прихода расхода
def change(request):
    return HttpResponse('<h2>Изменение остатков</h2>')
