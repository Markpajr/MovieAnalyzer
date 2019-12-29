import bs4, requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
# import pandas as pd


def Scrape_Movies():
    #Scrapes the Rotten Tomatos DVD - Streaming URL
    rt_movies_url = "https://www.rottentomatoes.com/browse/dvd-streaming-all?minTomato=0&maxTomato=100&services=amazon;hbo_go;itunes;netflix_iw;vudu;amazon_prime;fandango_now&genres=1;2;4;5;6;8;9;10;11;13;18;14&sortBy=release"
    driver_path = r"C:\Python\chromedriver.exe" 
    driver = webdriver.Chrome(driver_path)
    driver.get(rt_movies_url)

    #Creates a beautifulsoup HTML object from the scraped URL
    movies_soup = bs4.BeautifulSoup(driver.page_source, "lxml")

 #   print(movies_soup.prettify()) # Prints the HTML object

    ''' Finds the current number of visible movies. Uses soup.select_one to
        return one object into text. Format: # = ID, >span represents
        span tag under #ID.
        Then splits the text to find current and total movies.
    '''
    show_count = movies_soup.select_one('#count-link>span').text
    current_count = int(show_count.split()[1])
    max_count = int(show_count.split()[3])

    # Loops through clicking the show more button until all movies are shown
    # (Loop until Showing X of X)

    # # while current_count < max_count:
    # #     movies_soup = bs4.BeautifulSoup(driver.page_source, "lxml")
    # #     show_count = movies_soup.select_one('#count-link>span').text
    # #     current_count = int(show_count.split()[1])
    # #     max_count = int(show_count.split()[3])

    # #     try:
                # Finds the show more button and clicks it
    # #         show_more_btn = driver.find_element_by_css_selector('#show-more-btn > button')
    # #         show_more_btn.click()
            
    # #     except TimeoutException:
    # #         break
    
    # Creates a BeautifulSoup Requests lists of all movie Info div tags
    movie_divs = movies_soup.select('.movie_info')

    # Loops through Movie div list to extract all movie info into pandas df
    for movie in movie_divs:
        movie_title = movie.select_one('.movieTitle').text
        tomato_score = movie.select_one('.tMeterScore').text
        tomato_score = int(tomato_score[:-1])
        print(movie_title)
        print(tomato_score)
    print(show_count)


if __name__ == "__main__":
    #Run Scraper
    Scrape_Movies()
    print("done")