import random
#############====accound-details====#############

myChance = 3
myScore = 0
totall_boxes = 0

#############====defs====#############

def chance():
    global myScore, sampleList
    sampleList = ['Normal Box', 'Rare Box', 'Epic Box', 'Legendary Box']
    ehtemalat = random.choices(sampleList, weights=(400, 200, 100, 50))
    print(ehtemalat)
    if ehtemalat == ['Normal Box']:
        myScore = myScore + 15
    elif ehtemalat == ['Rare Box']:
        myScore = myScore + 30
    elif ehtemalat == ['Epic Box']:
        myScore = myScore + 60
    elif ehtemalat == ['Legendary Box']:
        myScore = myScore + 120
    print("your corrent Score:", myScore)

def luckygame():
    global myChance, totall_boxes
    while True:
        luckygame = input("use your chance: \"getbox\" or finish with \"exit\">>>")
        if luckygame == "getbox":
            if myChance != 0:
                myChance = myChance - 1
                totall_boxes = totall_boxes + 1
                chance()
                print("your chances left:", myChance)
            else:
                print("no chances left: 0")
        elif luckygame == "exit":
            starter()
        if myScore < 30 and myChance == 0:
            print("you not lucky enough! try again...")
            print("totall boxes:", totall_boxes)
            exit()

def starter():
    while True:
        starter = input("luckygame, store, stats, for end program \"exit\">>>")
        if starter == "luckygame":
            luckygame()
        elif starter == "stats":
            stats()
        elif starter == "store":
            store()
        elif starter == "exit":
            break
        else:
            print("luckygame, store, for end program \"exit\">>>")

def store():
    global myScore, myChance
    while True:
        print("your Score:", myScore,"your chances:", myChance)
        store = input("30 Scores for 1 chance \"buy\" for exit \"exit\">>>")
        if store == "buy":
            if myScore < 30:
                print("not enough Score")
            elif myScore >= 30:
                myChance = myChance + 1
                myScore = myScore - 30
                print("purchase successful!")
        elif store == "exit":
            break
        else:
            print("1 chance for 30 Scores\"buy\" for exit \"exit\">>>")
    starter()

def stats():
    global myScore, myChance, totall_boxes
    print("your Score:", myScore,"your chances:", myChance, "totall boxes:", totall_boxes)
    starter()

#############====program-run====#############

starter()


