from enum import Enum
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QComboBox, QSlider, QLabel, QHBoxLayout, QApplication


class Appearance(Enum):
    BORDER = "Border"
    FILL = "Fill"


class Backdrop(QWidget):
    def __init__(self, appearance, bd_height):
        super(Backdrop, self).__init__()
        self.appearance = appearance
        self.bd_height = bd_height
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel()
        self.label.setText(f"Appearance: {self.appearance.value}, BD Height: {self.bd_height}")

        layout.addWidget(self.label)

        self.setLayout(layout)

    def set_appearance(self, appearance):
        self.appearance = appearance
        self.label.setText(f"Appearance: {self.appearance.value}, BD Height: {self.bd_height}")

    def set_bd_height(self, bd_height):
        self.bd_height = bd_height
        self.label.setText(f"Appearance: {self.appearance.value}, BD Height: {self.bd_height}")


class BackdropFactory:
    def __init__(self):
        pass

    @staticmethod
    def create(appearance, bd_height):
        return Backdrop(appearance, bd_height)


class BackdropAppearance(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.combo_box = QComboBox()
        self.combo_box.addItems([appearance.value for appearance in Appearance])
        self.combo_box.currentIndexChanged.connect(self.on_combo_box_change)

        layout.addWidget(self.combo_box)

        self.slider = QSlider()
        self.slider.setOrientation(1)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(10)
        self.slider.valueChanged.connect(self.on_slider_change)

        layout.addWidget(self.slider)

        self.setLayout(layout)

    def on_combo_box_change(self, index):
        appearance = Appearance(self.combo_box.itemText(index))
        selected_node = nuke.selectedNode()

        if selected_node and selected_node.Class() == "BackdropNode":
            selected_node.knob("appearance").setValue(appearance.value)
            selected_node["bdheight"].setValue(selected_node["bdheight"].value())

    def on_slider_change(self, value):
        selected_node = nuke.selectedNode()

        if selected_node and selected_node.Class() == "BackdropNode":
            selected_node["bdheight"].setValue(value)

    def resizeEvent(self, event):
        self.slider.setFixedHeight(self.combo_box.height())
        event.accept()


if __name__ == '__main__':
    app = QApplication([])
    window = BackdropAppearance()
    window.show()
    app.exec_()
