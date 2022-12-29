from app import app
from models import db, Cupcake


db.drop_all()
db.create_all()

c1 = Cupcake(
    flavor="cherry",
    size="large",
    rating=5,
)

c2 = Cupcake(
    flavor="chocolate",
    size="small",
    rating=9,
    image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
)

c3 = Cupcake(
    flavor="maple bacon",
    size="yuge",
    rating=3.73,
    image="https://thescranline.com/wp-content/uploads/2021/03/Chocolate-Cupcakes.jpg"
)
c4 = Cupcake(
    flavor="fart",
    size="not too big",
    rating=7.35,
    image='https://thescranline.com/wp-content/uploads/2021/03/Galaxy-Cupcakes.jpg'
)

c5 = Cupcake(
    flavor="dudu",
    size="kinda small",
    rating=9.99,
    image=Cupcake.DEFAULT
)
c6 = Cupcake(
    flavor="caca",
    size="super medium",
    rating=4.20,
    image="https://www.bhg.com/thmb/3apC0EjPZ_WjzsnK3JrcL9M6kJs=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/santa-hat-cupcakes-RU235817-76f8ace8c5f94f74832b3d1e8f75956e.jpg"
)

db.session.add_all([c1, c2, c3, c4, c5, c6])
db.session.commit()