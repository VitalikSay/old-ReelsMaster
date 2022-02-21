class Reel():

    def __init__(self, symbols, weights):
        self.symbols = symbols
        self.weights = weights

    def GetSymbols(self):
        return self.symbols

    def GetWeights(self):
        return self.weights

    def SetSymbols(self, new_symbols):
        self.symbols = new_symbols

    def SetWeights(self, new_weights):
        self.weights = new_weights

    def PrintReel(self):
        pass
