import sqlite3



book = sqlite3.connect("Books.db")
c = book.cursor()
# """Default books available"""
c.execute('''CREATE TABLE Books (Id int,Title char, Author char NOT NULL, Price )''')
c.execute('''INSERT INTO Books values ('1','Think Python','Allen B .Drowning',475.0);''')
c.execute('''INSERT INTO Books values ('2','Half-Girfriend','Chetan Bhagat',345.0);''')
c.execute('''INSERT INTO Books values ('3','Alchemist','Pablo Escobar',589.0);''')
book.commit()
book.close()
