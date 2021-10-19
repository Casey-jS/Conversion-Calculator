import Model
import View

class Controller:
    def __init__(self, parent):
        self.parent = parent
        self.model = Model(self)
        self.view = View(self)

    if View.state == "Num":
        pass

    if View.state == "Calc":
        pass

    if View.state == "Unit":
        pass
