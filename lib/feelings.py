"""Show some feelings"""


def smile():
    """Be happy!"""
    return ":)"


def frown():
    """Sometimes life strikes hard."""
    return ":("


class Feelings:
    """This is a class to express emotions in covid times."""

    def __int__(self):
        """Instance initializer"""
        self.mood = smile()

    def change_mood(self):
        """A turnaround in your feelins"""
        if self.mood == frown():
            print('Lets not get sad... smile!')
            self.mood = smile()
        else:
            print('You cannot win all the times')
            self.mood = frown()
