# -*- coding: utf-8 -*-

class ProjectHelper:

    def __init__(self,app):
        self.app=app

    def create(self):
        wd = self.app.wd
        t=self.count()
        self.open_project_form()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(t+1)

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

    def open_project_form(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_css_selector("td.form-title > form > input.button-small").click()

    def count(self):
        wd = self.app.wd
        #откроем страницу с отчетами
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        # посчитаем количество чекпоксов на форме
        p=wd.find_elements_by_xpath('//table[3]/tbody/tr')
        pe=len(p)
        return pe-2

    def del_first_project(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

        wd.find_element_by_xpath("/html/body/table[@class='width100'][2]/tbody/tr[@class='row-1'][1]/td[1]/a").click()
        wd.find_element_by_css_selector("form > input.button").click()
        wd.find_element_by_css_selector("input.button").click()