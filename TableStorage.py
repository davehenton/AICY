#Version 1.0-pre
CONTACTS__1_0_pre = ["contacts", [["id", "int"], ["publicName", "text"], ["publicSurname", "text"],
                                ["privateName", "text"], ["privateSurName", "text"], ["privateStatus", "text"],
                                ["picture", "blob"], ["friendship", "int"], ["favorite", "int"]]]
def contacts__1_0_pre(c, mode: int):
    #c.execute('CREATE TABLE contacts (id int, publicName text, publicSurname text, privateName text, privateSurName text, privateStatus text, picture blob, friendship int, favorite int)')
    #c.execute('DROP TABLE contacts')
    print("contacts__1_0_pre(c)")
