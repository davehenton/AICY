from typing import List
import sqlite3
from TableStorage import *
from TableStorage import CONTACTS__1_0_pre as c_1_0_p

conn = sqlite3.connect('Client.db')
c = conn.cursor()

#c.execute('CREATE TABLE test (date text, trans text, symbol text, qty real, price real)')
#c.execute('DROP TABLE test')

#contacts__1_0_pre(c)

# OPTIMIZE: Shorten by changing Syntax; renaming vars
def checkTableExists(nameIn, column = []) -> bool:
    if (isinstance(nameIn, List)):
        name = nameIn[0]
        column = nameIn[1]
    else:
        name = nameIn
    c.execute('SELECT name FROM sqlite_master WHERE type="table" AND name=?', [name])
    if (c.fetchone() == None):
        return False;
    else:
        if (len(column) == 0):
            return True;
        else:
            if (isinstance(column[0],List)):
                for i in column:
                    c.execute("SELECT COUNT(*) AS CNTREC FROM pragma_table_info(?) WHERE name=?", [name, i[0]])
                    if (c.fetchone()[0] == 0):
                        return False
                    c.execute("SELECT COUNT(*) AS CNTREC FROM pragma_table_info(?) WHERE type=?", [name, i[1]])
                    if (c.fetchone()[0] == 0):
                        return False
                return True
            elif (isinstance(column[0],str)):
                for i in column:
                    c.execute("SELECT COUNT(*) AS CNTREC FROM pragma_table_info(?) WHERE name=?", [name, i])
                    if (c.fetchone()[0] == 0):
                        return False
                    return True


print(checkTableExists("test"))#False
print(checkTableExists("contacts"))#True
print(checkTableExists(c_1_0_p[0], c_1_0_p[1]))#True
print(checkTableExists(c_1_0_p))#True
