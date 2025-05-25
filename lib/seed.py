#!/usr/bin/env python3

# Script goes here!

# lib/seed.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

# Connect to the database
engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create tables if they don’t exist
Base.metadata.create_all(engine)

# Clear existing data (optional: good for dev purposes)
session.query(Freebie).delete()
session.query(Dev).delete()
session.query(Company).delete()

# Create companies
c1 = Company(name="Flatiron School", founding_year=2012)
c2 = Company(name="Google", founding_year=1998)
c3 = Company(name="OpenAI", founding_year=2015)

# Create devs
d1 = Dev(name="Alice")
d2 = Dev(name="Bob")
d3 = Dev(name="Charlie")

# Create freebies
f1 = Freebie(item_name="T-Shirt", value=20, company=c1, dev=d1)
f2 = Freebie(item_name="Sticker", value=5, company=c2, dev=d1)
f3 = Freebie(item_name="Mug", value=15, company=c2, dev=d2)
f4 = Freebie(item_name="Notebook", value=10, company=c3, dev=d3)

# Add and commit
session.add_all([c1, c2, c3, d1, d2, d3, f1, f2, f3, f4])
session.commit()

print("✅ Database seeded successfully!")

