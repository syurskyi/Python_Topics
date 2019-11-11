from functools import lru_cache


@lru_cache(maxsize=30)
def get_articles(on_date):
    # Здесь затратная операция, выбирающая статьи
    # на определённую дату.
    articles = [...]
    return articles
get_articles('2017-12-12')
get_articles('2017-12-13')
get_articles('2017-12-12')  # Взяты из кеша.
# Рассмотрим эффективность кеша:
get_articles.cache_info()
# CacheInfo(hits=1, misses=2, maxsize=20, currsize=2)