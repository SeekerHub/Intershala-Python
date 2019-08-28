import sqlite3 as db
conn = db.connect('Info.db')
cursor = conn.cursor()
ch = 'y'
while(ch=='y'):
    value = int(input())
    Matches = int(input())
    Runs = int(input())
    Century = int(input())
    HCentury = int(input())

    ctg = input()

    cursor.execute("INSERT INTO Stats (Matches, Runs, Century, HCentury, value, ctg) values (?, ?, ?, ?, ?, ?)", (Matches, Runs, Century, HCentury, value, ctg))
    conn.commit()
    ch = input("Enter y/n")

conn.close()
    # Id = int(input())
    # Player = input()
    # Scored = int(input())
    # Faced = int(input())
    # Fours = int(input())
    # Sixes = int(input())
    # Bowled = int(input())
    # Maiden = int(input())
    # Given = int(input())
    # Wkts = int(input())
    # Catches = int(input())
    # Stumping = int(input())
    # RO = int(input())
    # cursor.execute("INSERT INTO Match (Id,Player,Scored,Faced,Fours,Sixes,Bowled,Maiden,Given,Wkts,Catches,Stumping,RO) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (Id,Player,Scored,Faced,Fours,Sixes,Bowled,Maiden,Given,Wkts,Catches,Stumping,RO))
    # conn.commit()
    # ch = input("Enter y/n")
