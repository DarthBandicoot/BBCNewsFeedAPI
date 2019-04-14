import feedparser
import requests
from bs4 import BeautifulSoup
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from bbcnews.forms import NewArticleForm


class NewsList(TemplateView):
    template_name = 'news_list.html'
    results = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.news_results()
        context['articles'] = self.results
        context['title_header'] = 'Top 10 BBC News Articles'
        return context

    def news_results(self):
        bbcFeed = feedparser.parse('http://feeds.bbci.co.uk/news/world/rss.xml')
        news_articles = bbcFeed.entries[:10]

        for article in news_articles:
            if article not in self.results:
                self.results.append(article)
        return self.results


class AddNewArticle(NewsList, FormView):
    template_name = 'generic_form.html'
    form_class = NewArticleForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context[''] = ''
        return context

    def form_valid(self, form):
        bbc_url = form.cleaned_data.get('url_path')
        self.get_bbc_article(bbc_url)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'home'
        )

    def get_bbc_article(self, url):
        response = requests.get(url)
        html = response.text

        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('h1', {'class': 'story-body__h1'})
        description = soup.find('p', {'class': 'story-body__introduction'})
        date = soup.find('div', {"class": "date date--v2"})

        print('title :{}, description: {}, date {}, url: {}'.format(title, description, date, url))

        item = {'title': title.contents, 'summary': description.contents, 'published': date.contents, 'link': url}

        if item not in self.results:
            self.results.append(item)

        return self.results
