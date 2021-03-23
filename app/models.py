from . import db




class Properties (db.Model):

    __tablename__ = 'properties'
    pid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(150))
    propertyDescription = db.Column(db.String(300))
    Bedrooms = db.Column(db.Integer)
    Bathrooms = db.Column(db.Integer)
    price = db.Column(db.Float)
    propertytype = db.Column(db.String(20))
    location = db.Column(db.String(100))
    photo = db.Column(db.String(300))



    def __init__(self, title, propertyDescription, Bedrooms, Bathrooms, price, propertytype, location, photo):

        self.title = title
        self.propertyDescription = propertyDescription
        self.Bedrooms = Bedrooms
        self.Bathrooms = Bathrooms
        self.price = price
        self.propertytype = propertytype
        self.location = location
        self.photo = photo



    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<Property %r>' % self.title