import bs4, requests
from selenium import webdriver


driver_path = r"C:\Python\chromedriver.exe" 
Chrome = webdriver.Chrome(driver_path)
g_movies_url = "https://play.google.com/store/movies/collection/cluster?clp=6gIkIiIKHHByb21vdGlvbl9tb3ZpZXNfbmV3X3JlbGVhc2UQBxgE:S:ANO1ljIZSCM&gsr=CifqAiQiIgoccHJvbW90aW9uX21vdmllc19uZXdfcmVsZWFzZRAHGAQ%3D:S:ANO1ljKPEAQ&hl=en_US"



# res = requests.get(g_movies_url)
# res.raise_for_status()


movies_soup = bs4.BeautifulSoup(res.text)
print(movies_soup.prettify())

print(type(movies_soup))
