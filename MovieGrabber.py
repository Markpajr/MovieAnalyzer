import bs4, requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

def Scrape_Movies():
    rt_movies_url = "https://www.rottentomatoes.com/browse/dvd-streaming-all?minTomato=0&maxTomato=100&services=amazon;hbo_go;itunes;netflix_iw;vudu;amazon_prime;fandango_now&genres=1;2;4;5;6;8;9;10;11;13;18;14&sortBy=release"
    driver_path = r"C:\Python\chromedriver.exe" 
    driver = webdriver.Chrome(driver_path)
    driver.get(rt_movies_url)

    # sleep(timeout)
    # try:
    #     element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[2]/c-wiz/div/div/div[2]/div/div/div[1]/div/div/div[1]/a/div'))
    #     WebDriverWait(driver, timeout).until(element_present)
    # except TimeoutException:
    #     print ("Timed out waiting for page to load")


    movies_soup = bs4.BeautifulSoup(driver.page_source, "lxml")

    print(movies_soup.prettify())



if __name__ == "__main__":
    #Run Scraper
    Scrape_Movies()
    print("done")