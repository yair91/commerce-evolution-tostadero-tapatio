from pathlib import Path

from sqlalchemy import func, select

from store import create_app
from store.db import get_session
from store.models import Product

PRODUCTS = [
    ("TT-100", "Chiapas Altura", "Washed coffee from the highlands of Chiapas. Notes of milk chocolate, almond and red apple. 340 g, medium roast.", 28900, 25, "/static/images/chiapas.svg"),
    ("TT-110", "Veracruz Coatepec", "Bright and sweet cup from Coatepec, Veracruz. Notes of orange peel, panela and cacao. 340 g, medium-light roast.", 29900, 20, "/static/images/veracruz.svg"),
    ("TT-120", "Oaxaca Pluma Hidalgo", "Classic Pluma variety from the Oaxaca coast. Notes of caramel, walnut and soft spice. 340 g, medium roast.", 32900, 15, "/static/images/oaxaca.svg"),
    ("TT-130", "V60 Ceramic Dripper", "Size 02 ceramic pour-over dripper for one to three cups. Includes 40 paper filters.", 44900, 10, "/static/images/dripper.svg"),
    ("TT-140", "Moka Pot 6 Cups", "Aluminum stovetop espresso maker for strong, concentrated coffee at home.", 68900, 8, "/static/images/moka.svg"),
    ("TT-150", "Barro Mug", "Handmade clay mug from Tonalá, Jalisco. Holds 300 ml and keeps coffee warm longer.", 21900, 18, "/static/images/barro-mug.svg"),
]


def seed() -> None:
    app = create_app()
    with app.app_context():
        db = get_session()
        count = db.scalar(select(func.count()).select_from(Product))
        if count:
            print(f"Database already contains {count} products; nothing changed.")
            return
        for sku, name, description, price, stock, image_url in PRODUCTS:
            db.add(Product(
                sku=sku,
                name=name,
                description=description,
                price_cents=price,
                stock_quantity=stock,
                image_url=image_url,
                active=1,
            ))
        db.commit()
        print(f"Seeded {len(PRODUCTS)} products.")


if __name__ == "__main__":
    seed()
