class Admin:
    name="admin"
    password="123456"
    def printGuide(self):
        print("******************************************")
        print("*** ***")
        print("*** ***")
        print("*** 欢迎登录银行系统 ***")
        print("*** ***")
        print("*** ***")
        print("******************************************")
    def printHome(self):
        print("***********************************************")
        print("*** ***")
        print("*** 1.开户(1) 2.查询(2) ***")
        print("*** 3.取款(3) 4.存款(4) ***")
        print("*** 5.转账(5) 6.锁定(6) ***")
        print("*** 7.解锁(7) ***")
        print("*** ***")
        print("*** 退出(Q) ***")
        print("*** ***")
        print("***********************************************")
    def adminOpen(self):
        adminInpt=input("请输入管理员账户:")
        if adminInpt!=self.name:
            print("管理员账号输入错误！！！")
            return -1
        passwordInput=input("请输入管理员密码:")
        if passwordInput!=self.password:
            print("管理员密码输入错误！！！")
            return -1
        else:
            print("登录成功")
            return 0