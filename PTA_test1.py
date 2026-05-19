import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class TestTest1():
  def setup_method(self, method):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36")
    self.driver = webdriver.Chrome(
      service=Service(ChromeDriverManager().install()),
      options=options
    )
    self.vars = {}

  def teardown_method(self, method):
    self.driver.quit()

  def test_test1(self):
    self.driver.get("https://www.pta.gov.pk/")
    time.sleep(5)
    print("Title:", self.driver.title)
    print("URL:", self.driver.current_url)
    
    # Main page ka content nikalo
    headings = self.driver.find_elements(By.CSS_SELECTOR, "h1, h2, h3")
    for h in headings:
      if h.text.strip():
        print("Heading:", h.text.strip())
