from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.title)

article = soup.find(name="a", class_="titlelink")
article_title = article.getText()
article_link_junk = soup.find(name="a", class_="titlelink")
print(article_link_junk)
article_link = article_link_junk.get("href")
upvote_junk = soup.find(name="span", class_="score")
upvote = upvote_junk.getText()
print(upvote)

articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)


upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]


print(f"article texts = {article_texts}")
print(f"article links = {article_links}")
print(f"upvotes = {upvotes}")

largest_number = max(upvotes)
vote_index = upvotes.index(largest_number)
print(vote_index)
upvote_article = article_texts[vote_index]
print(upvote_article)

# article_link_junks = soup.findall(name="a", class_="titlelink")


# with open("website.html") as data:
#     contents = data.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# #print(soup.prettify())
# #print(soup.title)
# #print(soup.title.string)
#
# all_anchor_tags = soup.find_all(name='a')
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     #print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
#     #class_
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
#
# company_url = soup.select(selector="p a")
# print(company_url)
#
# name = soup.select_one("#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)
#
# h3_heading = soup.find_all("h3", class_="heading")
# print(h3_heading)
#
#
