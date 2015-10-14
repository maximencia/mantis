# -*- coding: utf-8 -*-
import pytest,datetime,json,os.path
from fixture.application import Application


now_time = datetime.datetime.now()

fixture = None
target = None

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    #читаем из файла конфигурации все что касается web
    web_config = load_config(request.config.getoption("--target"))['web']
    # если фикстура не создана или невалидна то создаем ее
    if fixture is None or not fixture.fixture_is_valid():
        fixture = Application(browser=browser,base_url=web_config['base_url'])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def final():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(final)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json") # имя файла с опциями по умолчанию


# функция загрузки из файла
def load_config(from_file):
    global target
    if target is None:
        path_to_config = os.path.join(os.path.dirname(os.path.abspath(__file__)),from_file)
        with open(path_to_config) as config_file:
            target=json.load(config_file)
    return target


