import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class E2ETests(unittest.TestCase):
	def setUp(self):
		# self.driver = webdriver.Firefox(executable_path=r'/usr/local/bin/geckodriver')
		self.driver = webdriver.Firefox()
		self.driver.get('http://localhost:5000')

	def tearDown(self):
		self.driver.quit()

	def test_browser_title_contains_app_name(self):
		self.assertIn('Named Entity', self.driver.title)

	def test_page_heading_is_named_entity_finder(self):
		# heading = self.driver.find_element(By.CSS_SELECTOR, 'h1.heading').text
		heading = self._find("h1.data-test-heading").text
		self.assertEqual('Named Entity Finder', heading)

	def test_page_has_input_for_text(self):
		input_element = self._find("input.data-test-input-text").text
		self.assertEqual('', input_element)
	
	def test_page_has_button_for_submitting_text(self):
		submit_button = self._find("button.data-test-input-text-button").text
		self.assertIsNotNone(submit_button)
		
	def test_page_has_ner_table(self):
		input_element = self._find("input.data-test-input-text")
		submit_button = self._find("button.data-test-input-text-button")
		input_element.send_keys('Hire me as a senior software engineer')
		submit_button.click()
		table = self._find('table.data-test-ner-table')
		self.assertIsNotNone(table)

	def _find(self, val):
		return self.driver.find_element(By.CSS_SELECTOR, val)