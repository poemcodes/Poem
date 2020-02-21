from Childhood import Mom, Dad, Love, Fears, Genetics
from Feeling import Anxiety
import Mind
import random

class Life(Mom, Dad):
    def __init__(self, Love, Fears, Genetics):
        Mind.GenThought()
        self.confidence = random.choice([Love, Fears, Genetics])
        return Anxiety()

    def something_happned(self, something):
        Mind.GenThought()
        anxiety_level = Anxiety.eval(something)
        if self.confidence < anxiety_level:
            self.condifence -= 1
            return Anxiety()

    def nothing_happend(self):
        Mind.GenThought()
        self.confidence -= 1
        return Anxiety()