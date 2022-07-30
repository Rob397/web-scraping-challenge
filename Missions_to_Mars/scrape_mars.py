from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser
import pandas as pd
import requests
from selenium import webdriver
import pandas as pd
import splinter



def Mars_news():
    # browser = init_browser()
    # splinter method
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    parent_class = soup.select_one('div', class_='list_text')
    news_title = parent_class.find('div', class_='content_title').get_text()
    news = parent_class.find('div', class_='article_teaser_body').get_text()
    news_data = {
        "content title": news_title,
        "page article": news,
    }

    # Quit the browser
    browser.quit()
    return news_data

def mars_image():

    # splinter method
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # ------constaint errors throught the notebook without the above method added each time scraping happends on a new page-----

    mars_url = 'https://spaceimages-mars.com/'
    browser.visit(mars_url)

    html_mars = browser.html

    soup = BeautifulSoup(html_mars, 'html.parser')

    featured_url = soup.find("img", class_="headerimage fade-in")["src"]
    featured_image_url = f'https://spaceimages-mars.com/{featured_url}'
    
    return featured_image_url

def Marsfacts():
    url ='https://galaxyfacts-mars.com/'
    tables = pd.read_html(url)
    df = tables[0]
    df.columns =["Comparison","Mars", "Earth"]
    cleaned_df = df.iloc[1:, :]
    html_table = cleaned_df.to_html()
    
    return html_table
def mars_hemispheres():
    
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url_hem = 'https://marshemispheres.com/'
    browser.visit(url_hem)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # list to hold the images and titles.
    hemisphere_image_urls = []

    # Code to retrieve the image urls and titles for each hemisphere.

    # First, we need to get a get a list of all of the hemispheres
    links = browser.find_by_css('a.product-item img')

    # Next, loop through those links, click the link, find the sample anchor, and return the href we want
    for i in range(len(links)):
        hemisphere = {}
        
        # We have to find the elements on each loop to avoid a stale element exception
        browser.find_by_css('a.product-item img')[i].click()
        
        #  Sample image anchor tag and extract the href
        sample_elem = browser.links.find_by_text('Sample').first
        hemisphere['img_url'] = sample_elem['href']
        
        # Get Hemisphere title
        hemisphere['title'] = browser.find_by_css('h2.title').text
        
        # Append hemisphere object to list
        hemisphere_image_urls.append(hemisphere)
        
        # Finally, we navigate backwards
        browser.back()
    return hemisphere_image_urls

