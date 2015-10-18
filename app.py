from flask import Flask, render_template
app = Flask(__name__)

import sqlite3

@app.route('/')
def hello_world():
    title = "Min portofolio"
    name = "John Dinh"


    db = sqlite3.connect("portfolio.db")
    db.execute("drop table if exists portfolio")
    db.execute("create table portfolio (overskrift text, beskrivelse text)")
    db.execute("insert into portfolio (overskrift, beskrivelse) values (?,?)", ("Mettes kaffekort", "det var en lang dag"))
    db.execute("insert into portfolio (overskrift, beskrivelse) values (?,?)", ("mathildes kasdt", "det var asdsadasg dag"))
    db.commit()
    cursor = db.execute("select * from portfolio order by overskrift")
    for row in cursor:
        print(row)

    print(len(row))


    bodywidth = ((25+25)*2)+385+(((25+1+25)*2+374)*2)+((25+1+25)*2+474)

    return render_template('index.html', title=title, name=name, bodywidth=bodywidth)

if __name__ == "__main__":
    app.run()