from functional_tests.base import FunctionalTest


class SearchTest(FunctionalTest):
    fixtures = ['users.json', 'team_data.json', 'message_data.json', 'team_list.json']

    def timeout(self, time_to_sleep):
        import time
        time.sleep(time_to_sleep)

    def test_search(self):
        self.login()
        self.create_issues()
        self.browser.find_element_by_id('q').send_keys('content')
        self.browser.find_element_by_id('btn_search').click()
        search_1 = self.browser.find_element_by_id('element0')
        search_2 = self.browser.find_element_by_id('element1')
        self.assertEqual(search_1.text, 'Test-Issue-01')
        self.assertEqual(search_2.text, 'Test-Issue-02')

        self.timeout(2)
