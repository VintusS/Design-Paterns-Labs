class BaristaContext:
    def __init__(self) -> None:
        self.fatiuge = 0

    def increment_fatigue(self):
        self.fatiuge += 1

    def reset_fatigue(self):
        self.fatiuge = 0

    def get_fatigue(self):
        return self.fatiuge
