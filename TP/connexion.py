import sqlite3

con = sqlite3.connect("TP5.db")

cur = con.cursor()

##con.commit()
##cur.execute("""INSERT INTO Journaliste VALUES (16, 'Paul', 'Amploi'), (17, 'Anna', 'Konda')""")

def displayFullname(name, lastname):
    display = 'Nom: ' + lastname + '\n' + 'Prénom :' + name
    return display

id = cur.execute("SELECT id_journalist FROM Journaliste")
name = cur.execute("SELECT nom FROM Journaliste")
lastname = cur.execute("SELECT prenom FROM Journaliste")

for row in id:
    print(displayFullname(str(name), str(lastname)))

con.close()