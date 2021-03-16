from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()


    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000/polls/')

        # She notices the page title and header mention to-do lists
        self.assertIn('My Poll App', self.browser.title)
        self.fail('Finish the test!')
        #User Story
        # there are a list of polls on the page

        # the polls are selectable

        # when you click on a poll it the url is at the poll's id number

        # the user can click on the radio button to vote

        # the user can click on vote and that takes them to the results page

        # the results page has a link to vote again which takes them to the previous page


if __name__ == '__main__':
    unittest.main()