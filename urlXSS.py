import sys
from selenium import webdriver
import requests
from time import sleep

target = sys.argv[1]
list = sys.argv[2]

browser = webdriver.Firefox()

with open(list, 'r') as wordlist:
    for line in wordlist.readlines():
        line = line.strip()
        url = target + line
        r = requests.get(url)
        if r.status_code == 200:
            browser.get(url)
            sleep(1)
        else:
            continue
