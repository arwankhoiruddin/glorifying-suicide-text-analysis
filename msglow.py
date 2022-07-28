import pandas as pd
from helium import *
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def getData(url):
    options = Options()
    options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    # options.add_argument("--headless")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")

    # driver = webdriver.Chrome(ChromeDriverManager().install())

    # browser = start_chrome(url, headless=True, options=options)
    browser = start_chrome(url, options=options)

    soup = BeautifulSoup(browser.page_source, 'html.parser')
    
    time.sleep(5)

    browser.close()

    return soup

def scrollPages(url):
    options = Options()
    options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    # options.add_argument("--headless")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")

    # driver = webdriver.Chrome(ChromeDriverManager().install())

    # browser = start_chrome(url, headless=True, options=options)
    browser = start_chrome(url, options=options)

    soup = BeautifulSoup(browser.page_source, 'html.parser')

    html = browser.find_elements(By.TAG_NAME, "html")
    html[0].send_keys(Keys.END)

    foundLinks = []
    pages = soup.find('li', class_='b_pag')
    for page in pages:
        links = page.find_all('a', class_='b_widePag')
        for link in links:
            l = link.get('href')
            if l is not None:
                foundLinks.append(l)

    for link in foundLinks:
        print(link)
        url = "https://www.bing.com" + link
        print(url)
        browser = start_chrome(url, options = options)

    browser.close()

    return soup

def getURLNDateFromBing(query, page):
    # https://www.bing.com/search?q=kompas+msglow&first=11&FORM=PERE

    result_date = []
    result_url = []

    url = 'https://www.bing.com/search?q=' + query + '&first=' + str(page) + '1&FORM=PERE'
    print(url)

    soup = getData(url)

    # get all results
    results = soup.find_all('li', class_='b_algo')
    for result in results:
        date = result.find(class_="news_dt")
        if date is not None:
            url = result.find('a').get('href')
            print(date)
            print(url)
            result_date.append(date.text)
            result_url.append(url)

    return [result_date, result_url]

def openBingPages(query):
    # https://www.bing.com/search?q=kompas+msglow&first=11&FORM=PERE

    result_date = []
    result_url = []

    url = 'https://www.bing.com/search?q=' + query
    print(url)

    soup = getData(url)

    # get all results
    results = soup.find_all('li', class_='b_algo')
    for result in results:
        date = result.find(class_="news_dt")
        if date is not None:
            url = result.find('a').get('href')
            print(date)
            print(url)
            result_date.append(date.text)
            result_url.append(url)

    return [result_date, result_url]

def mixQuery(query):
    finalQuery = ""
    for q in query:
        finalQuery = finalQuery + q + '+'
    return finalQuery


def writingToFile(tanggal, url, judul, berita):
    print("Writing data to file ...")    
    f = open('msglow_kompas.txt', 'a')
    for i in range(len(tanggal)):
        print("Writing " + judul[i] + " to file")

        f.write(tanggal[i] + '\n')
        f.write(url[i] + '\n')
        f.write(judul[i] + '\n')
        f.write(berita[i].replace("\n", "") + '\n')
        f.write('\n')

    f.close()
    print("Data has been written into text file")


def crawlOnePage(query, page):

    [result_dates, result_urls] = getURLNDateFromBing(query, page)
    print("Number of URLs found: " + str(len(result_urls)))
    print("length result_dates: " + str(len(result_dates)))

    print('Scrapping data for each URL...')

    data = []
    for i in range(len(result_urls)):
        data.append(getData(result_urls[i]))

    tanggal = []
    url = []
    judul = []
    berita = []

    for i in range(len(data)):
        j = data[i].find(class_="read__title")
        if j is not None:
            print("Judul: " + j.text)
            tanggal.append(result_dates[i])
            url.append(result_urls[i])
            judul.append(j.text)
            berita.append(data[i].find(class_="read__content").text)

    writingToFile(tanggal, url, judul, berita)

    print("Scrapping completed")


def crawlSomePages(query, numPages):
    for page in range(numPages):
        print("Crawling page " + str(page+1))
        [result_dates, result_urls] = getURLNDateFromBing(query, page+1)

        print("Number of URLs found: " + str(len(result_urls)))
        print("length result_dates: " + str(len(result_dates)))

        print('Scrapping data for each URL...')

        data = []
        for i in range(len(result_urls)):
            data.append(getData(result_urls[i]))

        tanggal = []
        url = []
        judul = []
        berita = []

        for i in range(len(data)):
            j = data[i].find(class_="read__title")
            if j is not None:
                print("Judul: " + j.text)
                tanggal.append(result_dates[i])
                url.append(result_urls[i])
                judul.append(j.text)
                berita.append(data[i].find(class_="read__content").text)

        writingToFile(tanggal, url, judul, berita)

    print("Scrapping completed")


if __name__ == "__main__":
    # Define variables here
    site = "kompas.com"
    numPage = 20

    print('Building query for ' + site)
    query = mixQuery(["site:" + site, "ms", "glow", "ps"])

    # crawlSomePages(query, 20)
    scrollPages("https://www.bing.com/search?q=site%3Akompas.com+ms+glow+ps")
    
