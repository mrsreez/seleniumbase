from seleniumbase import BaseCase
from page_objects.home_page import HomePage

class homeTest(HomePage):

    def setUp(self):
        super().setUp()
        #Login
        self.login()



        self.open_page()

    def tearDown(self):
        self.open("https://practice.automationbro.com/my-account/")
        self.click(".woocommerce-MyAccount-content a[href*=logout]")
        self.assert_element_visible("button[name=login]")

        super().tearDown()

        
    def test_home_page(self):
        # open home page



        self.assert_title_contains("Practice E-Commerce")

        # assert page title
        self.assert_element(self.logo_icon)

        # click on get start button
        self.click(self.get_started_btn)
        get_started_url = self.get_current_url()
        #using the entier url
        self.assert_equal(get_started_url, "https://practice.automationbro.com/#get-started")
        #using the partial test
        self.assert_true("get-started" in get_started_url)

        #gett the value of header and assert the text
        self.assert_text("Think different. Make different.", self.heading_text)

        # scroll all way to bottom and assert copywrite text

        #Copyright © 2020

        self.scroll_to_bottom()
        self.assert_text("Copyright © 2020 Automation Bro", self.copyright_text )


    def test_menu_links(self):

        expected_menus_items = ['Home', 'About', 'Shop', 'Blog' ,'Contact', 'My account', 'Home' , 'About', 'Blog' ,'Contact', 'Support Form']

        # find menu links
        elements = self.find_elements(self.menu_links)
        print(elements)

        for idx, ele in enumerate(elements):
            #print(idx, ele.text)
            self.assertEqual(expected_menus_items[idx], ele.text)






