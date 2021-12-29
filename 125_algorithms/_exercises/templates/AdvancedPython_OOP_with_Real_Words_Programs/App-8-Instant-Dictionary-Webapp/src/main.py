_____ i___

_____ justpy as jp

____ webapp _____ page
____ webapp.about _____ About
____ webapp.home _____ Home
____ webapp.dictionary _____ Dictionary


imports  l..(globals().values())

___ obj __ imports:
    __ i___.isclass(obj):
        __ issubclass(obj, page.Page) a.. obj __ n.. page.Page:
            jp.Route(obj.path, obj.serve)

# jp.Route(Home.path, Home.serve)
# jp.Route(About.path, About.serve)
# jp.Route(Dictionary.path, Dictionary.serve)


jp.justpy(port8001)