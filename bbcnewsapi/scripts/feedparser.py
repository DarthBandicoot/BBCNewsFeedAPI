import feedparser


def rssfeedparser():
    bbcFeed = feedparser.parse('http://feeds.bbci.co.uk/news/world/rss.xml')
    entry = bbcFeed.entries[1]
    entries = []
    entries.append(entry.values)

    return entries


rssfeedparser()
