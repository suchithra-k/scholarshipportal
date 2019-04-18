from django.shortcuts import render
from django.http import HttpResponse

from .tasks import crawl_data
from .models import Scholarship

def crawl(request):
    crawl_data.delay()
    return HttpResponse("Crawling started. ") 
