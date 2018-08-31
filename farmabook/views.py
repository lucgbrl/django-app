from django.shortcuts import render
from django.utils import timezone
from .models import Card
# Create your views here.

def post_list(request):
    #posts = Card.objects.filter(published_date__lte=timezone.now()).order_by('id') 
    cards = Card.objects.all()
    return render(request, 'farmabook/post_list.html', {'cards': cards})