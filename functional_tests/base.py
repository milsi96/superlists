import os
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

MAX_WAIT: int = 10


class FuncionalTest(StaticLiveServerTestCase):

  def get_item_input_box(self):
    return self.browser.find_element(By.ID, 'id_text')

  def setUp(self):
    self.browser = webdriver.Firefox()
    staging_server = os.environ.get('STAGING_SERVER')
    if staging_server:
      self.live_server_url = 'http://' + staging_server

  def tearDown(self):
    self.browser.quit()

  def wait_for_row_in_list_table(self, row_text: str):
    start_time = time.time()
    while True:
      try:
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(row_text, [row.text for row in rows])
        return
      except (AssertionError, WebDriverException) as e:
        if time.time() - start_time > MAX_WAIT:
          raise e
        time.sleep(0.5)

  def wait_for(self, fn):
    start_time = time.time()
    while True:
      try:
        return fn()
      except (AssertionError, WebDriverException) as e:
        if time.time() - start_time > MAX_WAIT:
          raise e
        time.sleep(0.5)
