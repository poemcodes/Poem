class Love(Feeling):
    def __init__(self):
        self.love_subject = None
        self.strength = 0

    def fall_in(self, lover):
        self.love_subject = lover
        self.strength = 10

    def time_passes(self, activity):
        if "good times" in activity:
            self.strength += 1
        else:
            self.strength -= 1

        if self.strength < 0:
            return hate(self.love_subject)