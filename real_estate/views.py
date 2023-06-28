from django.shortcuts import render
from real_estate.models import HomeView, ContactInfo
import feedparser
from django.http import JsonResponse

# Create your views here.
def home_view(request):
    home_view = HomeView.objects.first()  
    return render(request, 'base.html', {'home_view': home_view})

def news_view(request):
    feed = feedparser.parse('https://www.zillow.com/blog/feed/')
    news_items = []

    for entry in feed.entries[:5]:
        news_item = {
            'title': entry.title,
            'description': entry.description,
            'url': entry.link
        }
        news_items.append(news_item)

    return JsonResponse(news_items, safe=False)

def contact_view(request):
    contact_info = ContactInfo.objects.all()  
    return render(request, 'base.html', {'contact_info': contact_info})


