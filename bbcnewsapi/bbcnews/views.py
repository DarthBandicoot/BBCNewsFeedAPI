import feedparser
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView


class NewsList(ListView):
    template_name = 'news_list.html'
    context_object_name = ''
    results = []

    def get_context_data(self, request, *args, **kwargs):
        context = super(request, *args, **kwargs)
        context['articles'] = self.results
        return context

    def news_results(self):
        bbcFeed = feedparser.parse('http://feeds.bbci.co.uk/news/world/rss.xml')
        news_articles = bbcFeed.entries[:10]

        for article in news_articles:
            self.results.append(article)
        return self.results

    def get_context_object_name(self, object_list):
        self.context_object_name = self.news_results()

        return self.context_object_name
