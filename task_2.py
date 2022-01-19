class Stationery:
    _title = "Stationery"

    @staticmethod
    def draw(self):
        return "Start drawing.."

    @classmethod
    def get_title(cls):
        return cls._title


class Pen(Stationery):
    _title = "Pen"

    def draw(self):
        return f"Start drawing with {super().get_title().lower()}.."


class Pencil(Stationery):
    _title = "Pencil"

    def draw(self):
        return f"Start drawing with {super().get_title().lower()}.."


class Handle(Stationery):
    _title = "Handle"

    def draw(self):
        return f"Start drawing with {super().get_title().lower()}.."


pen = Pen()
pencil = Pencil()
handle = Handle()
print(*map(lambda obj: obj.draw(), [pen, pencil, handle]), sep="\n")
