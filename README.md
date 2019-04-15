# BBCNewsFeedAPI
Small App to display news stories from the bbc


Task: ""

################################

NOTE COULDN'T FIND ANY BBC NEWS API FOR SECOND PART SO I IMPROVISED.

#################################

Plan Of Action:

For First part -

1) 1 TemplateView displaying 10 news using bbc rss feed and from "http://feeds.bbci.co.uk/news/world/rss.xml"

2) Use feedparser library to parse the xml and return the news stories in a table

3) 1 table template displaying the stories with headers "title, text, date, URL. Clickable url 


For Second Part -

1) Added button on to the template to go to new form

2) 1 Field on the new form taking a url

3) Parse the url given and using beautiful soup identify div tags and add the the article to the List

