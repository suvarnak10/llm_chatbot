from sqlalchemy.orm import Session
from database import SessionLocal, Supplier, Product

def seed_data():
    db: Session = SessionLocal()

    # Insert suppliers
    supplier1 = Supplier(name="TechSupply", contact_info="tech@example.com", product_categories="Laptops, Phones")
    supplier2 = Supplier(name="GadgetWorld", contact_info="gadget@example.com", product_categories="Headphones, Accessories")

    db.add(supplier1)
    db.add(supplier2)
    db.commit()

    # Insert products
    product1 = Product(name="ThinkPad X1", brand="Lenovo", price=1500, category="Laptops", description="A high-performance laptop.", supplier_id=1)
    product2 = Product(name="AirPods Pro", brand="Apple", price=250, category="Headphones", description="Noise-cancelling wireless earbuds.", supplier_id=2)

    db.add(product1)
    db.add(product2)
    db.commit()

    db.close()

if __name__ == "__main__":
    seed_data()
