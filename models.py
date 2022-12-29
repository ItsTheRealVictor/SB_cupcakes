from flask_sqlalchemy import SQLAlchemy
import random

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    
    
class Cupcake(db.Model):
    
    __tablename__ = 'donuts'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    
    pics = ['https://tinyurl.com/demo-cupcake',
                'https://www.bhg.com/thmb/3apC0EjPZ_WjzsnK3JrcL9M6kJs=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/santa-hat-cupcakes-RU235817-76f8ace8c5f94f74832b3d1e8f75956e.jpg',
                'https://www.allrecipes.com/thmb/Ww77yR5gKXffjyLBsr2dDlS7PKI=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Homemade-Yellow-Cupcakes-2000-5a8b982200574822838b55d08daa6231.jpg',
                'https://i2.wp.com/www.twosisterscrafting.com/wp-content/uploads/2021/12/christmas-swirl-cupcakes-1200-main.jpg',
                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR03C9Yq4RWo1OFMc0TuHXLaftzxzuBPyR67w&usqp=CAU'
                ]
    
    image = db.Column(db.Text, default=random.choice(pics))
    
    def serialize(self):
        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image
        }