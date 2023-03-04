import pytest
from TestSuite.tests.test_base import BaseTest
from TestSuite.test_data import data

class TestAbout(BaseTest):
    
    def test_go_to_about_page(self, go_home):
        home_pg = self.pages['home_page']
        about_pg = self.pages['about_page']

        home_pg.click(home_pg.ABOUT_LINK)
        
        assert about_pg.get_element(about_pg.PAGE_HEADER).text == about_pg.PAGE_HEADER_TEXT