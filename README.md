# BBCNewsFeedAPI
Small App to display news stories from the bbc





Task:

Create a (basic) Django application that shows up to 10 news stories from BBC News - title, text, date, URL. Using Bootstrap would be a bonus. 

Onto that, create a basic API that accepts a BBC URL (GET request is fine but token authenticated POST request is best :smile: ) and then adds that article to the list - so adds the title, text, date, URL.

If this can be queried from a frontend input, then amazing. 

Python packages to use include: Django, Django Rest Framework, Requests, a DB of some kind (SQLite / MySQL) 

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

