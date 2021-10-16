import Model
import View

class Controller:
    def __init__(self, parent):
        self.parent = parent
        self.model = Model(self)
        self.view = View(self)