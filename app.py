from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
import os

app = Flask(__name__)
app.secret_key = "employee-secret-key"


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DB"),
    )


@app.route("/health")
def health():
    return "OK", 200


@app.route("/")
def dashboard():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM employees ORDER BY id DESC")
    employees = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("dashboard.html", employees=employees)


@app.route("/add", methods=["GET", "POST"])
def add_employee():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        department = request.form["department"]
        salary = request.form["salary"]

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO employees(name,email,department,salary)
            VALUES(%s,%s,%s,%s)
            """,
            (name, email, department, salary),
        )

        conn.commit()

        cursor.close()
        conn.close()

        flash("Employee Added Successfully", "success")

        return redirect(url_for("dashboard"))

    return render_template("add_employee.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_employee(id):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        department = request.form["department"]
        salary = request.form["salary"]

        cursor.execute(
            """
            UPDATE employees
            SET name=%s,email=%s,department=%s,salary=%s
            WHERE id=%s
            """,
            (name, email, department, salary, id),
        )

        conn.commit()

        flash("Employee Updated Successfully", "success")

        cursor.close()
        conn.close()

        return redirect(url_for("dashboard"))

    cursor.execute("SELECT * FROM employees WHERE id=%s", (id,))
    employee = cursor.fetchone()

    cursor.close()
    conn.close()

    return render_template("edit_employee.html", employee=employee)


@app.route("/delete/<int:id>")
def delete_employee(id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM employees WHERE id=%s", (id,))
    conn.commit()

    cursor.close()
    conn.close()

    flash("Employee Deleted Successfully", "success")

    return redirect(url_for("dashboard"))


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
