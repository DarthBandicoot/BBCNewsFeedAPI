# BBCNewsFeedAPI
Small App to display news stories from the bbc





Task:

Create a (basic) Django application that shows up to 10 news stories from BBC News - title, text, date, URL. Using Bootstrap would be a bonus. 

Onto that, create a basic API that accepts a BBC URL (GET request is fine but token authenticated POST request is best :smile: ) and then adds that article to the list - so adds the title, text, date, URL.

If this can be queried from a frontend input, then amazing. 

Python packages to use include: Django, Django Rest Framework, Requests, a DB of some kind (SQLite / MySQL) 



Plan Of Action:

For First part -

1 ListView displaying 10 news using bbc rss feed and from "http://feeds.bbci.co.uk/news/world/rss.xml"
Use feedparser library to parse the xml and return the news stories in a table
1 bootstap table template displaying the stories with headers "title, text, date, URL. Clickable url 




