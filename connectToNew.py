import mysql.connector
'''
newconnection (Function)
This function has to be called before running the main program if the program is shifted to a new system. 
It creates a database score on the new system with some existing values from the old database.
'''
def newconnection(user, pwd):
    connection = mysql.connector.connect(host = 'localhost', user = user, passwd = pwd)
    cursor = connection.cursor()
    try:
        cursor.execute('create database score')
    except:
        pass
    cursor.execute('use score')
    try:
        cursor.execute('create table scoreboard(`name` varchar(64) DEFAULT NULL, `score` int DEFAULT NULL)')
    except:
        pass
    qry=(
    ('aa',30),('bb',45),('cc',60),('dd',70),('ee',81),('ff',98),('gg',83),('ll',56),
    ('kk',67),('nn',20),('ft',15),('eg',0),('def',30),('praak',106),('praak',107),('praak',86),
    ('praak',137),('praak',96),('praak',108),('praak',90),('praak',131),('praak',0),('praak',88),
    ('praak',0),('praak',0),('praak',45),('praak',110),('praak',100),('praak',45),('praak',125),
    ('praak',89),('praak',16),('praak',75),('praak',75),('praak',0),('praak',45),('praak',75),
    ('praak',15),('praak',0),('praak',80),('praak',110),('praak',97),('praak',117),('praak',80),
    ('praak',75),('praak',0),('praak',75),('praak',0),('praak',60),('praak',75),('praak',75),
    ('praak',6),('praak',0),('praak',75),('praak',49),('praak',0),('praak',25),('praak',38),
    ('praak',31),('praak',25),('praak',25),('praak',25),('praak',25),('praak',25),('praak',25),
    ('praak',25),('praak',25),('praak',117),('praak',87),('praak',82),('praak',104),('praak',89),
    ('praak',85),('praak',1),('praak',84),('praak',0),('praak',12),('praak',7),('praak',93),
    ('praak',25),('praak',63),('praak',0),('praak',0),('praak',70),('praak',118),('praak',15),
    ('praak',55),('praak',13),('praak',153),('praak',25),('praak',0),('praak',0),('praak',0),
    ('praak',0),('praak',10),('praak',3)
    )
    for i in qry:
        cursor.execute('INSERT INTO scoreboard VALUES {}'.format(i))
    cursor.execute('select * from scoreboard')
    print(cursor.fetchall())

newconnection(pwd='sql123', user='root')