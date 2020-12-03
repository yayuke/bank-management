class Card:
    def __init__(self,cardId,cardPwd,money,cardLock=False):
        self.cardId=cardId
        self.cardPwd=cardPwd
        self.money=money
        self.cardLock=cardLock