__author__ = 'Maxim.Rumyantsev'

class ProjectHelper:

    def __init__(self,app):
        self.app=app

    def create(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_css_selector("td.form-title > form > input.button-small").click()

        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys("111")

        if not wd.find_element_by_xpath("//table[@class='width75']/tbody/tr[3]/td[2]/select//option[2]").is_selected():
            wd.find_element_by_xpath("//table[@class='width75']/tbody/tr[3]/td[2]/select//option[2]").click()

        if wd.find_element_by_name("inherit_global").is_selected():
            wd.find_element_by_name("inherit_global").click()

        if not wd.find_element_by_xpath("//table[@class='width75']//select[normalize-space(.)='publicprivate']//option[2]").is_selected():
            wd.find_element_by_xpath("//table[@class='width75']//select[normalize-space(.)='publicprivate']//option[2]").click()

        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys("description")
        wd.find_element_by_css_selector("input.button").click()