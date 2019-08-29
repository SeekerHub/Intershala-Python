

def Batting(runs,four,six,ball,field):
    total = 0

    if runs>50:
        total+=5
        if runs>100:
            total+=10

    fours = four*4
    sixs = six*6
    strike = (runs*100)/ball
    fields = field*10
    # print(fours,sixs,strike,fields)
    runs = runs-fours-sixs
    runs = runs/2
    # print(runs)
    total = runs+four+(six*2)+field+total


    if runs>50:
        total+=5
        if runs>100:
            total+=10
    total=strikerate(strike,total)
    print(total)

def strikerate(strike,total):
    if 80<=strike and strike<100:
        total+=2
        return total
    elif strike>=100:
        total+=4
        return total

def Bowling(wkts,overs,runs,field):
    total = 0
    eco = runs/overs
    # print(eco)
    if wkts==3:
        total+=5
        print(total)
    elif wkts>4:
        total+=10
    wickets = wkts*10
    # total = wick(wkts)
    # print("Fist total {}".format(total))
    if eco<=4.5 and eco>3.5:
        total+=4
        # print(eco)
    elif 2<eco and eco<=3.5:
        total+=7
        # print(total)
    elif eco<=2:
        total+=10
    fields = field*10
    # print(total)
    print(wickets,fields,total)
    total=wickets+fields+total
    print(total)
