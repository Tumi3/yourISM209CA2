from main import db

class User(db.Model):
__tablename__= 'userregister'
id=db.Column(db.Integer, primary_key=True)
firstname=db.Column(db.String(20), unique=False, nullable=False)
surname = db.Column(db.String(20), unique=False, nullable=False)
dateofbirth = db.Column(db.String(20), unique=False, nullable=True)
Nationality = db.Column(db.String(50), unique=False, nullable=False)
nationalidentificationnumber= db.Column(db.String(256), unique=True, nullable=False)

def __repr__(self):
 return '<Register {}>'.format(self.id)