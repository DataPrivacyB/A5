class liveShare :
    def __init__(self,Name,Quantity,livePrice,buyPrice):
        self.Name =Name
        self.Quantity = Quantity
        self.livePrice = livePrice
        self.buyPrice = buyPrice
        self.liveValue = Quantity*livePrice
        self.investment = Quantity*buyPrice
        self.pl = self.liveValue - self.investment
