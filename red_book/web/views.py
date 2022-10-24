from django.shortcuts import render
from .models import Red_book

def ab(request):
    context = {
        'sinichky': Red_book.objects.all()
    }
    return render(request, 'base.html', context)
