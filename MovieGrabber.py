import bs4, requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import pandas as pd
import tkinter as tk
from tkinter import filedialog



def Scrape_Tomatoes():
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

    while current_count < max_count:
        movies_soup = bs4.BeautifulSoup(driver.page_source, "lxml")
        show_count = movies_soup.select_one('#count-link>span').text
        current_count = int(show_count.split()[1])
        max_count = int(show_count.split()[3])

        try:
            # Finds the show more button and clicks it
            show_more_btn = driver.find_element_by_css_selector('#show-more-btn > button')
            show_more_btn.click()
            
        except TimeoutException:
            break
    
    # Creates a BeautifulSoup Requests lists of all movie Info div tags
    movie_divs = movies_soup.select('.movie_info')
    rtdf = pd.DataFrame(columns=['Title','Critic Tomato','Audience Tomato','Release Date','TomatoURL'])

    # Loops through Movie div list to extract all movie info into pandas df
    for movie in movie_divs:
        movie_title = movie.select_one('.movieTitle').text
        critic_tomato_score = int(movie.select_one('.tMeterScore').text[:-1])
        release_date = movie.select_one('.release-date').text.split()[1:]
        release_date = ' '.join(release_date)
        movie_url = 'https://www.rottentomatoes.com' + movie.select_one('a')['href'] 
        rtdf = rtdf.append({'Title': movie_title, 'Critic Tomato': critic_tomato_score, 'Release Date': release_date, 'TomatoURL': movie_url}, ignore_index=True)
        
    rtdf.sort_values(by=['Critic Tomato'], inplace=True)
    #display(rtdf)
    #print(show_count)
    
    #Opens a dialog window to save the data as a csv file and select location
    root= tk.Tk()

    canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief = 'raised')
    canvas1.pack()
    saveAsButton_CSV = tk.Button(text='Export CSV', command=exportCSV, bg='green', fg='white', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 150, window=saveAsButton_CSV)
    root.mainloop()

def exportCSV():
    global rtdf

    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    rtdf.to_csv (export_file_path, index = None, header=True)

if __name__ == "__main__":
    #Run Scraper
    Scrape_Tomatoes()
    print("done")