import sqlite3

for x in range(1, 56):
    url = '"http://api.quirky.codes/' + str(x) + '.jpg"'

    conn = sqlite3.connect('nuts.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO nuts (id,URL) VALUES(' + str(x) + ', ' + url + ')')
    conn.commit()

    print("It worked!")

    conn.close()
