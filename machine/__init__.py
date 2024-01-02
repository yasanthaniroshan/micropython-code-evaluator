class Pin:
    OUT = 0
    def __init__(self, pin, mode):
        self.pin = pin
        self.mode = mode
    def on(self):
        print("Pin %d is on" % self.pin)
    def off(self):
        print("Pin %d is off" % self.pin)