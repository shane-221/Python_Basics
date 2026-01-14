import requests
from bs4 import BeautifulSoup


response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_website = response.text

soup = BeautifulSoup(yc_website, "html.parser")


#Todo: Finding one of the headings, link and the upvotes
headings= soup.find(name ="a",class_ ="storylink")

upvote_function =soup.find(name="span", class_="score")
upvotes = upvote_function.getText()


article_upvotes = upvotes
article_text = headings.getText()
article_link =headings.get("href")

#Todo: Finding all of the headings, link and the upvotes
    # Same thing but just the find all function
headings= soup.find_all(name ="a",class_ ="storylink")
article_list_text=[]
articles_list_links=[]

for article_tag in headings:

    article_text = article_tag.getText()
    article_list_text.append(article_text)

    article_link = article_tag.get("href")
    articles_list_links.append(article_link)

article_upvotes = [score.getText()for score in soup.find_all(name="span", class_= "score")]
        # All the lists are now ordered. Need to get the article numbers to be in number format. Remove Points.
article_upvotes = [int(i.split()[0]) for i in article_upvotes]
print(article_upvotes)

print(article_list_text)


# Todo: Find the title, link of the item with the highest number of upvotes.
index = article_upvotes.index(max(article_upvotes))
popular_article = article_list_text[index]
popular_link = articles_list_links[index]


