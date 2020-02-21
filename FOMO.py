class Me():
    def __init__(self):
        born()
        self.state = Cry()

    def living(self, options):
        current_happines = eval_happines(self.state)
        for option in options:
            if eval_happines(option) > current_happines:
                self.state = option

            else:
                self.state = FOMO()
