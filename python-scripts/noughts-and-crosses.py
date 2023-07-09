from pyscript import Element  # type: ignore


class NoughtsAndCrosses:
    def __init__(self):
        self.turn = 1

    def make_move(self, id):
        cell = Element(id)

        if self.turn % 2 == 1:
            cell.element.innerText = "o"

        else:
            cell.element.innerText = "x"

        self.turn += 1


game = NoughtsAndCrosses()
