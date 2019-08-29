import sqlite3





z = 'y'
while(z=='y'):
    while(z=='y'):

        name = input('Enter the name of Book:\t')
        # print(type(name))
        bok = sqlite3.connect('Books.db')
        curs = bok.cursor()
        sqlc = 'select * from Books where title = \'{}\';'.format(name)
        curs.execute(sqlc)
        r= curs.fetchone()
        if r==None:
            print('Sorry! Book is not available at the moment')
            break
        print(r)


        qty  = int(input('Enter the Quantity:\t'))
        sqlc = 'select price from Books where title = \'{}\';'.format(name)
        # print(sqlc)
        curs = bok.cursor()
        # curs.execute('''SELECT * FROM Books WHERE title= '''+ str(name) +''';''' )
        curs.execute(sqlc)
        found = 1
        while found!=0:
            record = curs.fetchone()

            if record==None:
                # print('Sorry! Book is not available at the moment')
                found+=1
                break
            print('Total price to be paid :',  record[0]*qty)
            found=0

        if found!=0 :
            print('Sorry! Book is not available at the moment')
        print('\n')
        z = input('Add more Books (y/n):\t')
        if z=='n':
            break
    if z=='n':
        break
    z = input('Add more Books (y/n):\t')
    # if z=='n':
    #     break
