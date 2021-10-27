from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager

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
    news_title = soup.find('div', id = "content_title")

    # Get the latest News Paragraph text
    # From inspect I found: <div class="article_teaser_body">
    news_p = soup.find('div',id = "article_tear_body")
   
    # Path to Mars image page.
    url2 = "https://spaceimages-mars.com/"
    browser.visit(url2)
   
    # Slooooowwwwww down. What's the rush?
    time.sleep(1)

    # Find the src for the featured Mars image.
    # The main image is the second one featured.
    relative_image_path = soup.find_all('img')[1]["src"]
    mars_img = url2 + relative_image_path

    # Store data in a dictionary
    mars_data = {
        "mars_img": mars_img,
        "news_title": news_title,
        "news_p": news_p
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data