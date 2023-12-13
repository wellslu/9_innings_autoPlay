import time
import telnetlib

#########################################請自行在"R=  "後插入遊戲區域

class Controler(object):
    def __init__(self, R):
        self.R = R # 畫面位置
        self.B1 = Location(-745, 382) # 連點無用位置
        self.count = 0

    # 空等時間
    def wait_and_click(self, picture, wait_time):
        self.R.wait(picture,wait_time)
        wait(1)
        self.R.click(picture)

    # 斷線
    def disconnect(self):
        self.wait_and_click("img/game_banner.png",10)
        if self.R.exists("img/next_schedule.png"):
            self.wait_and_click("img/next_schedule.png",10)
            self.wait_and_click(Pattern("img/play_ball.png").similar(0.60),10)
            self.wait_and_click("img/play_all_game.png",30)
        else:
            self.wait_and_click("img/continue.png",20)

    # 重新啟動
    def restart(self):
        print("restart",time.ctime())
        click(Location(817, 16))##關閉模擬器的位置
        wait(1)
        click(Location(545, 295))##重啟模擬器
        wait(10)
        doubleClick(Location(113, 839))##開遊戲
        wait(15)
        click(Location(788, 121))##點擊進入遊戲
        wait(60)
        if self.R.exists("img/cancel2.png"):
            self.R.click("img/cancel2.png")
            wait(5)
        if self.R.exists("img/cancel2.png"):
            self.R.click("img/cancel2.png")
        self.wait_and_click("img/game_banner.png",10)
        self.count = 0

    # 自動點擊
    def click_auto(self):
        while(1):
            if self.R.exists(Pattern("img/auto.png").similar(0.90)):
                self.R.click(Pattern("img/auto.png").similar(0.90))
                if self.R.exists("img/autoplaying.png"):
                    type("a",Key.CTRL)
            elif self.R.exists("img/next_page.png"):
                break
            elif self.R.exists("img/attend_game.png"):
                self.R.click("img/attend_game.png")
            elif self.R.exists("img/network_error.png"):
                    self.R.click("img/yes.png")
                    self.disconnect()
                    wait(10)
            else:
                click(self.B1)
                wait(3)
    
    def main(self):
        while(1):
            # homepage開打
            if self.R.exists("img/game_banner.png"):
                self.disconnect()
                self.click_auto()
            # 正在開打
            elif self.R.exists("img/autoplaying.png") or self.R.exists(Pattern("img/auto.png").similar(0.90)):
                self.click_auto()
            # 判斷打完了沒
            if self.R.exists("img/next_page.png"):
                self.R.click("img/next_page.png") # 下一頁
                type("a",Key.CTRL)
                # 跨天送卡
                if self.R.exists("img/day_new_card.png"):
                    self.R.click("img/yes.png")
                self.wait_and_click("img/yes.png",10) # 確定
                # 系列賽會出現點擊畫面
                if self.R.exists("img/click2.png",10):
                    self.wait_and_click("img/click2.png",3)
                elif self.R.exists("img/next_page.png",5):
                    self.wait_and_click("img/next_page.png",3) 
                # 季後賽結束會出現下一頁或沒有東西
                # # 每15場重啟一次模擬器
                # if self.count == 15:
                #     self.restart()
                # 跳過技能升級
                if self.R.exists("img/upgrade.png"):
                    self.R.click("img/cancel1.png")
                    wait(1)
                self.wait_and_click("img/next_schedule.png",10)
                # 判斷有沒有休賽日，沒有play ball就是休賽
                if self.R.exists(Pattern("img/play_ball.png").similar(0.60)):
                    self.R.click(Pattern("img/play_ball.png").similar(0.60))
                    self.wait_and_click("img/play_all_game.png",30)
                    self.click_auto()
                # 休賽日            
                else:
                    self.wait_and_click("img/click1.png",15)
                    self.wait_and_click("img/next_schedule.png",10)
                    self.wait_and_click(Pattern("img/play_ball.png").similar(0.60),10)
                    self.wait_and_click("img/play_all_game.png",30)
                    self.click_auto()
        ################################################################    
            if self.R.exists("img/error1.png"):
                self.R.click("img/yes.png")
        ################################################################斷線重連
            if self.R.exists("img/network_error.png"):
                self.R.click("img/yes.png")
                type("a",Key.CTRL)  
        ################################################################
                self.wait_and_click(Pattern("img/playing.png").similar(0.90),30)
                self.wait_and_click("img/continue.png",20)
                wait(10)
                self.click_auto()
        #################################################################   
            if self.R.exists("img/error2.png"):
                self.R.click("img/yes.png")
                type("a",Key.CTRL)
                self.wait_and_click(Pattern("img/playing.png").similar(0.90),30)
                self.wait_and_click("img/continue.png",20)
                wait(10)
                self.click_auto()
        #################################################################
            if self.R.exists("img/attend_game.png"):
                self.R.click("img/attend_game.png")
                type("a",Key.CTRL)
                self.click_auto()
                

Controler(Region(-1014,261,864,484)).main()
