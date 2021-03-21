import mysql.connector

#the database and table have already been created
def getConnection():
    connection = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'pa123456', database = 'score')
    return connection
    
def scoreboard(name, score):
    #adding a name and the score and displaying in desending order
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute('use score') #score is the database

    if connection.is_connected():
        n = name
        sc = score
        sql = 'insert into scoreboard (name, score) values (%s, %s)'
        row = [(n, sc)]
        cursor.executemany(sql, row) #name varchar(30) primary key, score int(10)
        connection.commit()
        cursor.close()
        connection.close()
    else:
        print('cannot connect to the database. please try connecting again.')

def fetchscore():
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute('use score') #score is the database
    if connection.is_connected():
        try:
            cursor.execute('select * from scoreboard order by score desc')
            scores = cursor.fetchmany(10)
            try:
                cursor.fetchall()
            except:
                pass
            cursor.close()
            connection.close()
            return scores
        except Exception as e:
            print(e)
            cursor.close()
            connection.close()
            return None
             
    else:
        print('cannot connect to the database. please try connecting again.')
        return None
    

        
    
    
    
