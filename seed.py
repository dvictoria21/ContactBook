from models import db, Contact

db.connect()

db.create_tables([Contact], safe=True)

contact = Contact.create(
    first_name="Daija", last_name="Watt", phone_number="201-388-3052"
)

db.close()
