import sqlite3
myplayers = sqlite3.connect('Myplayers.db')
curplay = myplayers.cursor()
curplay.execute('''INSERT INTO players''')
