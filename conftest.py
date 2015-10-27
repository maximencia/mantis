# -*- coding: utf-8 -*-
import pytest,datetime,json,os.path
from fixture.application import Application
import ftputil

now_time = datetime.datetime.now()

fixture = None
target = None

@pytest.fixture
def app(request,config):
    global fixture
    browser = request.config.getoption("--browser")
    # если фикстура не создана или невалидна то создаем ее
    if fixture is None or not fixture.fixture_is_valid():
        fixture = Application(browser=browser,base_url=config['web']['base_url'])
    fixture.session.ensure_login(username=config['webadmin']['username'],password=config['webadmin']['password'])
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


@pytest.fixture(scope="session", autouse=True)
def configure_server(request,config):
    install_server_configuration(config['ftp']['host'],config['ftp']['username'],config['ftp']['password'])
    def fin():
        restore_server_configuration(config['ftp']['host'],config['ftp']['username'],config['ftp']['password'])
    request.addfinalizer(fin)

@pytest.fixture(scope = "session")
def config(request):
    return load_config(request.config.getoption("--target"))


def install_server_configuration(host, username, password):
    with ftputil.FTPHost(host, username, password) as remote:
        if remote.path.isfile("config_inc.php.bak"):
            remote.remove("config_inc.php.bak")
        if remote.path.isfile("config_inc.php"):
            remote.rename("config_inc.php","config_inc.php.bak")
        remote.upload(os.path.join(os.path.dirname(__file__),"resources/config_inc.php"),"config_inc.php")

def restore_server_configuration(host, username, password):
    with ftputil.FTPHost(host, username, password) as remote:
        if remote.path.isfile("config_inc.php.bak"):
            if remote.path.isfile("config_inc.php"):
                remote.remove("config_inc.php")
            remote.rename("config_inc.php.bak","config_inc.php")
