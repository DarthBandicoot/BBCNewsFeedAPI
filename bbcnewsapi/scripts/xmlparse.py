import feedparser


def rssfeedparser():
    results = {'title': '',
               'text': '',
               'date': '',
               'url': ''}

    bbcFeed = feedparser.parse('http://feeds.bbci.co.uk/news/world/rss.xml')
    news_articles = bbcFeed.entries[:10]

    for article in news_articles:
        results['title'] = article.get('title')
        results['text'] = article.get('summary')
        results['date'] = article.get('published')
        results['url'] = article.get('link')

    return results


rssfeedparser()
