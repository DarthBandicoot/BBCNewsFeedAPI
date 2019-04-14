import feedparser
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, FormView


class NewsList(TemplateView):
    template_name = 'news_list.html'
    results = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.results.clear()
        self.news_results()
        context['articles'] = self.results
        context['title_header'] = 'Top 10 BBC News Articles'
        return context

    def news_results(self):
        bbcFeed = feedparser.parse('http://feeds.bbci.co.uk/news/world/rss.xml')
        news_articles = bbcFeed.entries[:10]

        for article in news_articles:
            self.results.append(article)
        return self.results


class AddNewArticle(FormView):
    pass

