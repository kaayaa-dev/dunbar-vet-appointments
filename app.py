from flask import Flask, flash, redirect, render_template, request, url_for

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
    q = request.args.get("q", "").strip()
    conn = db.get_connection()
    if q:
        rows = conn.execute(
            "SELECT * FROM clients WHERE name LIKE ? OR phone LIKE ? ORDER BY id DESC",
            (f"%{q}%", f"%{q}%"),
        ).fetchall()
    else:
        rows = conn.execute("SELECT * FROM clients ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("clients.html", clients=rows, q=q)


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
            flash("Client added.")
            return redirect(url_for("list_clients"))
    return render_template("client_form.html", error=error)


@app.route("/properties")
def list_properties():
    conn = db.get_connection()
    rows = conn.execute(
        """SELECT p.*, c.name AS client_name FROM properties p
           JOIN clients c ON c.id = p.client_id ORDER BY p.id DESC"""
    ).fetchall()
    conn.close()
    return render_template("properties.html", properties=rows)


@app.route("/properties/new", methods=["GET", "POST"])
def new_property():
    conn = db.get_connection()
    clients = conn.execute("SELECT id, name FROM clients ORDER BY name").fetchall()
    error = None
    if request.method == "POST":
        client_id = request.form.get("client_id", "").strip()
        address = request.form.get("address", "").strip()
        property_type = request.form.get("property_type", "").strip()
        if not client_id or not address:
            error = "Client and address are required."
        else:
            conn.execute(
                "INSERT INTO properties (client_id, address, property_type) VALUES (?, ?, ?)",
                (client_id, address, property_type),
            )
            conn.commit()
            conn.close()
            flash("Property added.")
            return redirect(url_for("list_properties"))
    conn.close()
    return render_template("property_form.html", clients=clients, error=error)


@app.route("/animals")
def list_animals():
    conn = db.get_connection()
    rows = conn.execute(
        """SELECT a.*, c.name AS client_name FROM animals a
           JOIN clients c ON c.id = a.client_id ORDER BY a.id DESC"""
    ).fetchall()
    conn.close()
    return render_template("animals.html", animals=rows)


@app.route("/animals/new", methods=["GET", "POST"])
def new_animal():
    conn = db.get_connection()
    clients = conn.execute("SELECT id, name FROM clients ORDER BY name").fetchall()
    error = None
    if request.method == "POST":
        client_id = request.form.get("client_id", "").strip()
        name = request.form.get("name", "").strip()
        species = request.form.get("species", "").strip()
        breed = request.form.get("breed", "").strip()
        if not client_id or not name or not species:
            error = "Owner, name and species are required."
        else:
            conn.execute(
                "INSERT INTO animals (client_id, name, species, breed) VALUES (?, ?, ?, ?)",
                (client_id, name, species, breed),
            )
            conn.commit()
            conn.close()
            flash("Animal added.")
            return redirect(url_for("list_animals"))
    conn.close()
    return render_template("animal_form.html", clients=clients, error=error)


if __name__ == "__main__":
    app.run(debug=config.FLASK_DEBUG)