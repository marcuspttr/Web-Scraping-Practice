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
    mars_df.set_index('Mars - Earth Comparison',inplace=True)

    # Saving the dataframe to html.
    mars_facts = mars_df.to_html()

    # Path to Mars website.
    url_4 = "https://marshemispheres.com/"
    browser.visit(url_4)
    
    # Pause to let the page load.
    time.sleep(1)


    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")
    
    # Creating empty lists to help store the data for the 4 hemispheres.
    title = []
    links = []
    img_url = []

    # Finding all the separate listings for each hemisphere.
    for div in soup.find_all('div', {"class" : "description"}):
        # Grabbing the title of each hemisphere.
        img_title = div.find('h3').get_text()
        title.append(img_title)
    
        # This is where things get tricky. The full-sized high, quality image was at another linked website.
        # This grabs those links.
        img_link = div.find('a')['href']
        links.append(img_link)

    # Unless I completely overlooked something I have to path to each site to grab the full-sized images.
    # This loops through the links to do just that.
    for link in links:
        # Path to each hemisphere's full sized-image, they are modifications of the original site.
        hemisphere_url = url_4 + link
        browser.visit(hemisphere_url)
        
        # Pause to let the page load
        time.sleep(1)

        # Scrape each page into Soup
        html = browser.html
        soup = bs(html, "html.parser")

        full_img_path = soup.find('img', {"class" : "wide-image"})["src"]

        # Wouldn't you believe it? Another link.
        # Pathing to each hemisphere's full sized-image. 
        hemisphere_img_url = url_4 + full_img_path
        browser.visit(hemisphere_img_url)
                
        # Pause to let the page load
        time.sleep(1)

        # Scrape this final page into Soup
        html = browser.html
        soup = bs(html, "html.parser")

        # The image is the only one featured here so this is easier.
        # Storing the picture into the list.
        current_img = soup.find('img')["src"]
        img_url.append(current_img)

    # Store data in a dictionary
    mars_info = {
        "mars_img": mars_img,
        "news_title": news_title,
        "news_p": news_p,
        "mars_facts" : mars_facts,
        "hemi_title1" : title[0],
        "hemi_image1" : img_url[0],
        "hemi_title2" : title[1],
        "hemi_image2" : img_url[1],
        "hemi_title3" : title[2],
        "hemi_image3" : img_url[2],
        "hemi_title4" : title[3],
        "hemi_image4" : img_url[3]
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_info