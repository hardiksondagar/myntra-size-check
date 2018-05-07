import sys
from pyquery import PyQuery
from selenium import webdriver

if __name__ == '__main__':
    default_url = 'https://www.myntra.com/jeans/jack--jones/jack--jones-men-blue-slim-fit-low-rise-stretchable-jeans/1801426/buy'
    url = sys.argv[1] if len(sys.argv) > 1 else default_url
    driver = webdriver.Firefox()
    driver.get(url)
    html = driver.page_source
    driver.quit()
    pq = PyQuery(html)
    available_sizes = pq('button.size-buttons-size-button')
    print available_sizes.text()
