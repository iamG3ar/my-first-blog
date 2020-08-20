#from django.test import TestCase
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Victor heard of the new cool website. He goes
        #to check its homepage
        self.browser.get('http://127.0.0.1:8000')

        #he notices the header and page title mentions thought...
        self.assertIn('Thoughts...', self.browser.title)
        self.fail('Finish the test! ')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
