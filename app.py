from flask import Flask, redirect, render_template, request, url_for

import config
import db

app = Flask(__name__)
app.secret_key = config.SECRET_KEY

db.init_db()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/clients")
def list_clients():
    keyword = request.args.get("q", "").strip()
    conn = db.get_connection()
    if keyword:
        clients = conn.execute(
            "SELECT * FROM clients WHERE name LIKE ? ORDER BY id DESC",
            (f"%{keyword}%",),
        ).fetchall()
    else:
        clients = conn.execute("SELECT * FROM clients ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("clients.html", clients=clients, keyword=keyword)


@app.route("/clients/new", methods=["GET", "POST"])
def new_client():
    error = None
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        email = request.form.get("email", "").strip()
        if not name or not phone:
            error = "Name and phone are required."
        else:
            conn = db.get_connection()
            conn.execute(
                "INSERT INTO clients (name, phone, email) VALUES (?, ?, ?)",
                (name, phone, email),
            )
            conn.commit()
            conn.close()
            return redirect(url_for("list_clients"))
    return render_template("client_form.html", error=error)


if __name__ == "__main__":
    app.run(debug=config.FLASK_DEBUG)