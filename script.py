class Sceneray:

    # Constructor to initialize the data.
    def __init__(self, cause, points):
        self.causeDamage = cause
        self.damagePoints = points

    # Methord to check if damage can be caused.

    def GiveDamagePoints(self):

        # The damage points are returned only if damage is caused.
        if self.causeDamage == True:
            return self.damagePoints

    def GiftBox(self, x, y, w, h, img):
        self.xAxis = x
        self.yAxis = y
        self.width = w
        self.height = h
        self.image = img

    def GetDetails(self):
        return self.__dict__


# Testing with sample data.
e = Sceneray(True, 50)
e.GiftBox(150, 150, 50, 74, "box.png")

# testing git commit
