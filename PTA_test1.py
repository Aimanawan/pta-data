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
    self.driver = webdriver.Chrome(
      service=Service(ChromeDriverManager().install()),
      options=options
    )
    self.vars = {}

  def teardown_method(self, method):
    self.driver.quit()

  def test_test1(self):
    self.driver.get("https://www.pta.gov.pk/")
    time.sleep(3)
    print("Title:", self.driver.title)
    print("URL:", self.driver.current_url)
    self.driver.find_element(By.LINK_TEXT, "Numbering").click()
    time.sleep(3)
    print("New URL:", self.driver.current_url)
