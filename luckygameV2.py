import random


class luckygame1:
    def __init__(self):
        self.myChangeBox = 2
        self.myMoney = 0
        self.total_scores = 0
        self.mojeze = 0
        self.GoldCoin = 0
    
    def change(self):
        sampleList = ['Normal Box', 'Rare Box', 'Epic Box', 'Legendary Box', 'chance again', 'point 200']
        randomit = random.choices(sampleList, weights=(600, 350, 150, 30, 140, 6))
        print(f'Box: {randomit}')
        
        if randomit == ['Normal Box']:
            self.myScoure += 15
            self.GoldCoin += 2
        elif randomit == ['Rare Box']:
            self.myScoure += 30
            self.GoldCoin += 4
        elif randomit == ['Epic Box']:
            self.myScoure += 60
            self.GoldCoin += 8
        elif randomit == ['Legendary Box']:
            self.myScoure += 120
            self.GoldCoin += 16
        elif randomit ==  ['chance again']:
            self.myChangeBox += 1
        elif randomit == ['point 200']:
            self.myScoure += 200
            self.mojeze += 1
            self.GoldCoin += 50
            print(f'♥♥♥ mojeze: {self.mojeze}')


        self.myChangeBox -= 1
        self.totall_boxes += 1
        print("Number of boxes opened:", self.myChangeBox)
        print("Your score from  this box:", self.myScoure)


    def luckyGame(self):
        while True:
            luckygame = input("Open the box width: 'openbox' OR finish with: 'exit'>>>")
            if luckygame == 'openbox':
                if self.myChangeBox != 0:
                    self.change()
                        
                else:
                    print()
                    print("NO...\tRemaining chance: 0")
                    
            elif luckygame == "exit":
                self.starter()

            if self.myChangeBox == 0 and self.myScoure < 30:
                print()
                print("you not lucky enough! try again...")
                print("totall boxes:", self.totall_boxes)
                print(100*'-')
                self.stats2()
                exit()
            else:
                self.luckyGame()
           
    def starter(self):
        while True:
            starter = input("luckygame, store, stats, for end program \"exit\">>>")
            if starter == "luckygame":
                self.luckyGame()
            elif starter == "stats":
                self.stats()
            elif starter == "store":
                self.store()
            elif starter == "exit":
                print(100*'-')
                self.stats2()
                exit()
            else:
                print("luckygame, store, for end program \"exit\">>>")

    def store(self):
        while True:
            print("your Money:", self.myMoney,"your chances:", self.myChangeBox)
            store = input("30 Scores for 1 chance: \"buy\" exit: \"exit\">>>")
            if store == "buy":
                if self.myScoure < 30:
                    print("not enough Score")
                    if self.myChangeBox > 0:
                        self.luckyGame()
                    else:
                        self.stats2()
                        exit()

                else:
                    self.myChangeBox += 1
                    self.myMoney -= 30
                    print("purchase successful!")
            elif store == "exit":
                break

        self.luckyGame()
    
    def stats(self):
        print(f'$$ GoldCoin: {self.GoldCoin}\nsum Score: {self.myMoney}\t\tyour chances: {self.myChangeBox}\ntotal box: {self.totall_boxes}\t\tmojeze: {self.mojeze}')
        print()
        self.starter()

    def stats2(self):
        print(f'$$ GoldCoin: {self.GoldCoin}\nsum Score: {self.myMoney}\t\tyour chances: {self.myChangeBox}\ntotal box: {self.totall_boxes}\t\tmojeze: {self.mojeze}')
        print()
  
rungame = luckygame1()
rungame.starter()


    
