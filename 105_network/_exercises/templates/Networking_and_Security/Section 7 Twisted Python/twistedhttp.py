____ twisted.internet ______ reactor
____ twisted.web.client ______ getPage
____ twisted.python.util ______ println

getPage("http://www.microsoft.com/").addCallbacks(
    callback_lambda value:(println(value),reactor.stop),
    errback_lambda error:(println("an error occurred", error),reactor.stop))
reactor.run