_____ justpy as jp


c_ Doc:

    ___ serve _
        wp  jp.WebPage()


        div  jp.Div(awp, classes"bg-gray-200 h-screen")

        jp.Div(adiv, text"Instant Dictionary API", classes"text-4xl m-2")
        jp.Div(adiv, text"Get definitions of words:", classes"text-lg")
        jp.Hr(adiv)
        jp.Div(adiv, text"www.example.com/api?w=moon")
        jp.Hr(adiv)
        jp.Div(adiv, text"""
        {"word": "moon", 
        "definition": 
        ["A natural satellite of a planet.", "A month, particularly a lunar month (approximately 28 days).", 
        "To fuss over adoringly or with great affection.", 
        "Deliberately show ones bare ass (usually to an audience, or at a place, where this is not expected or deemed appropriate).", 
        "To be lost in phantasies or be carried away by some internal vision, having temorarily lost (part of) contact to reality."]}
        """)
        r_ wp

