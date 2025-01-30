import json
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
)
import mysql.connector

app = Flask(__name__)
app.secret_key = "your-secret-key-here"

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="x",
        password="x",
        database="hotel_booking",
    )

@app.route("/")
def list_rooms():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM CAMERA")
    rooms = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("list.html", rooms=rooms)

@app.route("/add", methods=("GET", "POST"))
def add_room():
    if request.method == "POST":
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        numero = request.form["numero"]
        tipo = request.form["tipo"]
        disponibile = bool(request.form["disponibile"])
        prezzo = request.form["prezzo"]
        numero_posti = request.form["numero_posti"]

        cursor.execute(
            "INSERT INTO CAMERA (numero, tipo, disponibile, prezzo, numero_posti) VALUES (%s, %s, %s, %s, %s)",
            (numero, tipo, disponibile, prezzo, numero_posti),
        )
        conn.commit()
        cursor.close()
        conn.close()
        flash("Room added successfully!")
        return redirect(url_for("list_rooms"))
    return render_template("add.html")

@app.route("/book/<int:room_id>", methods=("GET", "POST"))
def book_room(room_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM CAMERA WHERE numero = %s", (room_id,))
    room = cursor.fetchone()

    if request.method == "POST":
        cliente = request.form["cliente"]
        data_inizio = request.form["data_inizio"]
        data_fine = request.form["data_fine"]

        cursor.execute(
            "INSERT INTO PRENOTAZIONE (camera_numero, cliente, data_inizio, data_fine) VALUES (%s, %s, %s, %s)",
            (room_id, cliente, data_inizio, data_fine),
        )
        conn.commit()
        cursor.close()
        conn.close()
        flash("Room booked successfully!")
        return redirect(url_for("list_rooms"))

    cursor.close()
    conn.close()
    return render_template("book.html", room=room)

@app.route("/bookings")
def list_bookings():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM PRENOTAZIONE")
    bookings = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("bookings.html", bookings=bookings)

if __name__ == "__main__":
    app.run(debug=True)