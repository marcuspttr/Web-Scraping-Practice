from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    # Path to Mars website.
    url = "https://redplanetscience.com/"
    browser.visit(url)
    
    # Pause to let the page load.
    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the latest News Title
    # From inspect I found: <div class = "content_title">
    news_title = soup.find('div', class_= "content_title").text

    # Get the latest News Paragraph text
    # From inspect I found: <div class="article_teaser_body">
    news_p = soup.find('div', class_= "article_teaser_body").text

    # Path to Mars image page.
    url_2 = "https://spaceimages-mars.com/"
    browser.visit(url_2)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Slooooowwwwww down. What's the rush?
    time.sleep(1)  

    # Find the src for the featured Mars image.
    # The main image is the second one featured.
    img_source = soup.find('img', {"class" : "headerimage fade-in"})["src"]

    mars_img = url_2 + img_source

    # Pathing to Mars facts page.
    url_3 = "https://galaxyfacts-mars.com/"

    # Using Pandas to scrape the tables.
    tables = pd.read_html(url_3)

    # Grabbing the first table.
    mars_df = tables[0] 

    # Table has a formatted header. Removing it to make the first row the header instead.
    header = mars_df.iloc[0]
    mars_df = mars_df[1:]
    mars_df.columns = header

    # Saving the dataframe to html.
    mars_facts = mars_df.to_html()

    # Store data in a dictionary
    mars_info = {
        "mars_img": mars_img,
        "news_title": news_title,
        "news_p": news_p,
        "mars_facts" : mars_facts
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_info