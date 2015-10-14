# -*- coding: utf-8 -*-
__author__ = 'Maxim.Rumyantsev'
from selenium import webdriver
from fixture.session_f import SessionHelper

class Application:

  # проверка валидности фикстуры через возврат url
    def fixture_is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def __init__(self,browser, base_url):
        # параметр отвечает за запуск браузера бля тестов
        if browser=="firefox":
            self.wd = webdriver.Firefox()
        elif browser=="chrome":
            self.wd = webdriver.Chrome()
        elif browser=="ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" %browser)

        #self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.base_url = base_url

 # заполнение  тестовых полей name- имя поля; send_keys_parameters - текст для заполнения
    def fill_text_field(self,name,send_keys_parameters):
        wd = self.wd
        if send_keys_parameters is not None:
            wd.find_element_by_name(name).click()
            wd.find_element_by_name(name).clear()
            wd.find_element_by_name(name).send_keys(send_keys_parameters)

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()








