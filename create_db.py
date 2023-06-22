from GeoGuesser import create_app, db, bcrypt

from GeoGuesser.models import User

app = create_app()
app.app_context().push()

db.drop_all()
db.create_all()

user = User(
    firstname = "Cassie",
    lastname = "Mojar",
    alias = "cmojar",
    password = bcrypt.generate_password_hash('password'),
    email = "c.mojar@surreyschools.ca"
)

db.session.add(user)
db.session.commit()