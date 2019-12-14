# Пример относительного импорта из родительского пакета
from ..models.article import ArticleModel

class HomeController(object):
    """Эмуляция контроллера домашней страницы"""

    def get(self):
        print('HTTP GET request to /home/')
        ArticleModel.get_objects()
        print('Rendering HTML page')
