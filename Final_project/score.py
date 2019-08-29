import sqlite3 as db

def score(r):
    runs=r[0][2]
    faced=r[0][3]
    batscore=int(runs/2)
    four=r[0][4]
    six=r[0][5]
    score=int(runs/2)
    if score>=50:
        score+=5
    if score>=100:
        score+=10
    if runs>0:
        sr=runs*100/faced
        if sr>=80 and sr<100:
            score+=2
        if sr>=100:
            score+=4
            score=score+four
            score=score+2*six
        # return {'name':nameratscore}
    wkt=r[0][9]
    balls=(r[0][6])*6
    runs=r[0][8]
    score=wkt*10
    # name=r[0][1]
    if wkt>=3:
        score=score+5
    if wkt>=5:
        score=score=score+10
    if balls>0:
        er=runs/balls
    #print ("eco:",er)
        if er<=2:
            score=score+10
        if er>2 and er<=3.5:
            score=score+7
        if er>3.5 and er<=4.5:
            score=score+4
    # d = {'name':name,'score':score}
    d = score
    # print(d)
    return d


# if __name__=='__main__':
    # play = ['Kohli', 'Yuvraj', 'Rahane', 'Dhawan', 'Dhoni', 'Axar', 'Pandya', 'Jadeja', 'Kedar', 'Ashwin', 'Umesh']
con = db.connect('Info.db')
curs = con.cursor()
scored = []
# sqlc = 'select PLayer from Books where title = \'{}\';'.format(name)
# sqlc = 'SELECT * FROM Match where Player=\'{}\'
def Score_calculator(play):
    match = 'Match'
    for i in play:
        sqlc = 'SELECT * FROM {} where Player=\'{}\''.format(match,i)
        curs.execute(sqlc)
        r= curs.fetchall()
        # print(r[0][7])
        scored.append(str(score(r)))
    # print(scored)
    return scored
