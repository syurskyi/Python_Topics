_____ justpy as jp

@jp.SetRoute("/home")
___ home():
    wp  jp.QuasarPage(tailwindTrue)
    div  jp.Div(awp, classes"bg-gray-200 h-screen")

    div1  jp.Div(adiv, classes"grid grid-cols-3 gap-4 p-4")
    in_1  jp.Input(adiv1, placeholder"Enter first value",
             classes"form-input")
    in_2  jp.Input(adiv1, placeholder"Enter second value",
             classes"form-input")
    d_output  jp.Div(adiv1, text"Result goes here...", classes"text-gray-600")
    jp.Div(adiv1, text"Just another div...", classes"text-gray-600")
    jp.Div(adiv1, text"Yet another div", classes"text-gray-600")

    div2  jp.Div(adiv, classes"grid grid-cols-2 gap-4")
    jp.Button(adiv2, text"Calculate", click  sum_up, in1in_1, in2in_2,
              d  d_output,
              classes"border border-blue-500 m-2 py-1 px-4 rounded "
                      "text-blue-600 hover:bg-red-500 hover:text-white")
    jp.Div(adiv2, text"I am a cool interactive div!", mouseentermouse_enter,
           mouseleavemouse_leave,
           classes  "hover:bg-red-500")
    r_ wp

@jp.SetRoute("/about")
___ about():
    wp  jp.QuasarPage(tailwindTrue)

___ sum_up(widget, msg):
    s..  f__(widget.in1.value) + f__(widget.in2.value)
    widget.d.text  s..

___ mouse_enter(widget, msg):
    widget.text  "A mouse entered the house!"

___ mouse_leave(widget, msg):
    widget.text  "The mouse left!"

jp.justpy()
