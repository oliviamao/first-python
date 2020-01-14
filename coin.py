class Pound:

    def __init__(self, rare=False):

        self.rare = rare

        if self.rare:
            self.value = 1.25
        else:
            self.rare = 1.00
            
        self.value = 1.00
        self.colour = "gold"
        self.num_edges = 1
        self.diameter = 22.5  # mm
        self.thinckness = 3.15 # mm
        self.heads = True

    def rust(self):
        self.colour = "greenish"

    def clean(self):
        self.colour = "gold"
        
