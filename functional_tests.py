import time
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):
  
  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self):
    self.browser.get('http://localhost:8000')

    self.assertIn('To-Do', self.browser.title)
    header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
    self.assertIn('To-Do', header_text)

    inputbox = self.browser.find_element(By.ID, 'id_new_item')
    self.assertEqual(
      inputbox.get_attribute('placeholder'),
      'Enter a to-do item'
    )

    to_do_item = 'Buy peacock feathers'
    inputbox.send_keys(to_do_item)

    inputbox.send_keys(Keys.Enter)
    time.sleep(1)

    table = self.browser.find_element(By.ID, 'id_list_table')
    rows = table.find_element(By.TAG_NAME, 'tr')
    self.assertTrue(
      any(row.text == f'1: {to_do_item}' for row in rows)
    )

    self.fail('Finish the test')


if __name__ == '__main__':
  unittest.main(warnings='ignore')
