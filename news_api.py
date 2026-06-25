import requests
query = input("What type of news do you want today?")
api = "a52ea400f9e8419db677e2a66517175a"

url = f"https://newsapi.org/v2/everything?q={query} &sortBy=publishedAt&apiKey={api}"
# print(url)
r = requests.get(url)
data = r.json()
articles = data["articles"]
for index, article in enumerate(articles):
    print(index+1, article["title"], article["url"])
    print("\n***********************************\n")



