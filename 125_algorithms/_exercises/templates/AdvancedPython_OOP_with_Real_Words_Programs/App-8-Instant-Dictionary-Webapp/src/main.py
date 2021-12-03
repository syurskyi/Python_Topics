_____ inspect

_____ justpy as jp

____ webapp _____ page
____ webapp.about _____ About
____ webapp.home _____ Home
____ webapp.dictionary _____ Dictionary


imports = list(globals().values())

for obj in imports:
    if inspect.isclass(obj):
        if issubclass(obj, page.Page) and obj is not page.Page:
            jp.Route(obj.path, obj.serve)

# jp.Route(Home.path, Home.serve)
# jp.Route(About.path, About.serve)
# jp.Route(Dictionary.path, Dictionary.serve)


jp.justpy(port=8001)