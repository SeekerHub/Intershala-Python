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
    wkt=r[0][9]
    balls=(r[0][6])*6
    runs2=r[0][8]
    score+=wkt*10
    if wkt>=3:
        score=score+5
    if wkt>=5:
        score=score=score+10
    if balls>0:
        er=runs2/balls
        if er<=2:
            score=score+10
        if er>2 and er<=3.5:
            score=score+7
        if er>3.5 and er<=4.5:
            score=score+4
    d = score
    return d


con = db.connect('Info.db')
curs = con.cursor()
scored = []
def Score_calculator(play,match):
    scored = []
    match_no = str(match)
    for i in play:
        sqlc = 'SELECT * FROM {} where Player=\'{}\''.format(match_no,i)
        curs.execute(sqlc)
        r= curs.fetchall()
        scored.append(str(score(r)))
    return scored
