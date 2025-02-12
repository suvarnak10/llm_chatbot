from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, DECIMAL
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

DATABASE_URL = "mysql+pymysql://root:password@db/chatbot_db"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    contact_info = Column(Text, nullable=True)
    product_categories = Column(Text, nullable=True)

    products = relationship("Product", back_populates="supplier")

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    brand = Column(String(255), nullable=True)
    price = Column(DECIMAL(10, 2), nullable=True)
    category = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"), nullable=True)

    supplier = relationship("Supplier", back_populates="products")

def init_db():
    Base.metadata.create_all(bind=engine)
