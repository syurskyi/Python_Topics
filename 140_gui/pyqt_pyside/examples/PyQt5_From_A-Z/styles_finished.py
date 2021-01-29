def styleDeleteButton():
    return """
        QPushButton {
            background-color:red; 
            color:white; 
            border-radius:10px; 
            border:1px solid #404040; 
            padding:5px;
        }
        QPushButton:hover {
            border-color:white;
        }
        """

def styleSaveButton():
    return """
        QPushButton {
            background-color:green; 
            color:white; 
            border-radius:10px; 
            border:1px solid #404040; 
            padding:5px;
        }
        QPushButton:hover {
            border-color:white;
        }
        """

def styleRadioButtons(dark=False):
    if dark:
        return """
            QRadioButton {
                background-color:red;
                color: green
            }
        """
    else:
        return """
            QRadioButton {
                background-color:green;
                color: red
            }
        """
