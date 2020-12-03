from admin import Admin
from atm import ATM
import time
import csv
import os
from user import User
from card import Card
import time
class HomePage:
    #找桌面路径
    def GetDesktopPath(self):
        return os.path.join(os.path.expanduser("~"), 'Desktop')
    def __init__(self):
        self.allUserD={} # 使用字典存储数据
        self.atm=ATM(self.allUserD)
        self.admin=Admin()# 管理员开机界面
    def saveUser(self):
        self.allUserD.update(self.atm.alluser)
        with open(self.GetDesktopPath()+'\\user_data.txt', 'w', encoding='utf-8') as data:
            writer = csv.DictWriter(data,
                                    fieldnames=['userId', 'name', 'phone', 'cardId', 'cardPwd', 'money', 'cardLock'])
            writer.writeheader()
            for cardId in self.allUserD:
                writer.writerow({"userId": self.allUserD.get(cardId).id,
                                 "name": self.allUserD.get(cardId).name,
                                 "phone": self.allUserD.get(cardId).phone,
                                 "cardId": cardId,
                                 'cardPwd': self.allUserD.get(cardId).card.cardPwd,
                                 "money": self.allUserD.get(cardId).card.money,
                                 "cardLock": str(self.allUserD.get(cardId).card.cardLock)})
        print("数据存盘成功")

    # 初始化用户数据
    def init(self):
        try:
            os.path.getsize(self.GetDesktopPath()+'\\user_data.txt')
        except FileNotFoundError as e:
            print('文件为空')
        else:
            with open(self.GetDesktopPath()+'\\user_data.txt', 'r', encoding='utf-8') as data:
                reader = csv.DictReader(data)
                for i in reader:
                    name = i['name']
                    ID = i['userId']
                    phone = i['phone']
                    cardId = i['cardId']
                    oncePwd = i['cardPwd']
                    prestMoney = i['money']
                    cardLock=i['cardLock']
                    if cardLock=="True":
                        cardLock=True
                    else:
                        cardLock=False
                    # print(name,ID,phone,cardId,oncePwd,prestMoney)
                    card = Card(cardId=cardId, cardPwd=oncePwd, money=float(prestMoney),cardLock=cardLock)  # 创建卡
                    user = User(name=name, id=ID, phone=phone, card=card)  # 创建用户
                    self.atm.alluser[cardId] = user  # 存入用户字典

    # 程序的入口
    def main(self):
        self.admin.printGuide()
        resL=self.admin.adminOpen()
        if not resL:
            while True:
                self.admin.printHome()
                self.init()
                option = input("请输入您的操作：")
                if option not in ("1", "2", "3", "4", "5","6", "7", "S", "Q", "q"):
                    print("输入操作项有误,请仔细确认！")
                    time.sleep(1)
                if option == "1":  # 开户
                    self.atm.creatUser()
                elif option == "2":  # 查询
                    self.atm.searchUser()
                elif option == "3":  # 取款
                    self.atm.getMoney()
                elif option == "4":  # 存储
                    self.atm.saveMoney()
                elif option == "5":  # 转账
                    self.atm.transferMoney()
                elif option == "6":  # 锁定
                    self.atm.lockCard()
                elif option == "7":  # 解锁
                    self.atm.unlockCard()
                elif option.upper() == "Q":
                    if not (self.admin.adminOpen()):
                        self.saveUser()
                        print('退出系统')
                        return -1
if __name__ == '__main__':
    homepage=HomePage()
    homepage.main()
