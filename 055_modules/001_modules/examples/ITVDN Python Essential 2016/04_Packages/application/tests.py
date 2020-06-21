# Пример относительного импорта из текущего пакета
from .controllers import home

def run_app_test():
    print('Running test application')

    home_ctrl = home.HomeController()
    home_ctrl.get()