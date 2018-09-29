import config
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
import time

url = "http://google.com"
# Start New Session
driver = webdriver.Firefox()
driver.get(url)

# Close driver
driver.close()