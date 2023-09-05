from flask import Flask, jsonify, request
from models import Contact

app = Flask(__name__)

from models import db

db.connect()


@app.route("/contact/", methods=["GET", "POST"])
@app.route("/contact/<int:id>", methods=["GET", "PUT", "DELETE"])
def endpoint(id=None):
    if request.method == "GET":
        if id:
            return jsonify(Contact.get_or_none(Contact.id == id).__dict__)
        else:
            contact_list = [contact.__dict__ for contact in Contact.select()]
            return jsonify(contact_list)

    if request.method == "PUT":
        body = request.get_json()
        Contact.update(**body).where(Contact.id == id).execute()
        return f"Contact {id} has been updated."

    if request.method == "POST":
        new_contact = Contact(**request.get_json())
        new_contact.save()
        return jsonify({"success": True})

    if request.method == "DELETE":
        Contact.delete().where(Contact.id == id).execute()
        return f"Contact {id} has been deleted."


if __name__ == "__main__":
    app.run(debug=True, port=9000)
