_____ justpy as jp
_____ definition
____ webapp _____ layout
____ webapp _____ page

_____ requests

c_ Dictionary(page.Page):
    path  "/dictionary"

    @classmethod
    ___ serve(cls, req):
        wp  jp.QuasarPage(tailwindTrue)

        lay  layout.DefaultLayout(awp)
        container  jp.QPageContainer(alay)


        div  jp.Div(acontainer, classes"bg-gray-200 h-screen")
        jp.Div(adiv, text"Instant English Dictionary", classes"text-4xl m-2")
        jp.Div(adiv, text"Get the definition of any English word instantly as you type.", classes"text-lg")

        input_div  jp.Div(adiv, classes"grid grid-cols-2")


        output_div  jp.Div(adiv, classes"m-2 p-2 text-lg border-2 h-40")

        input_box  jp.Input(ainput_div, placeholder"Type in a word here...", outputdiv  output_div,
                 classes"m-2 bg-gray-100 border-2 border-gray-200 rounded w-64 focus:bg-white focus:outline-none focus:border-purple-500 "
                         "py-2 px-4 ")
        input_box.on('input', cls.get_definition)

        print(cls, req)

        r_ wp

    @staticmethod
    ___ get_definition(widget, msg):
        defined  definition.Definition(widget.value).get()
        widget.outputdiv.text  " ".join(defined)


