import feedparser


def rssfeedparser():
    bbcFeed = feedparser.parse('http://feeds.bbci.co.uk/news/world/rss.xml')
    entries = []
    news_articles = bbcFeed.entries[:10]

    for article in news_articles:
        print(article)
        entries.append(article)

    return entries


rssfeedparser()
