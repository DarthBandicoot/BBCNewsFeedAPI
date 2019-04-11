from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class NewsList(TemplateView):

    def requests(self):
        bbc = 'http://feeds.bbci.co.uk/news/world/rss.xml'
