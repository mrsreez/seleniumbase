from seleniumbase import BaseCase

class contactTest(BaseCase):
    def test_contact_page(self):

        self.open("https://practice.automationbro.com/contact/")

        # scroll to the form and take screenshot
        self.scroll_to("#evf-form-277")
        self.save_screenshot("empty_contact_form", "custom_screenshot")
        # fill in form
        self.send_keys('#evf-277-field_ys0GeZISRs-1', 'Test name')
        self.send_keys("//input[@id='evf-277-field_LbH5NxasXM-2']", 'test@gmail.com')
        self.send_keys("#evf-277-field_66FR384cge-3", '123456789')
        self.send_keys("#evf-277-field_yhGx3FOwr2-4", 'This is the text area')

        # atke screen shot after form is filler
        self.save_screenshot("filled_contact_form", "custom_screenshot")
        # button
        self.click("#evf-submit-277")

        # verify the submit message

        self.assert_text("Thanks for contacting us! We will be in touch with you shortly", "div[role=alert]")


