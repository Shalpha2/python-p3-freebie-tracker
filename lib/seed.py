#!/usr/bin/env python3

# lib/seed.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

session.query(Freebie).delete()
session.query(Dev).delete()
session.query(Company).delete()

# Create companies
c1 = Company(name="Spotify", founding_year=2006)
c2 = Company(name="Google", founding_year=1998)
c3 = Company(name="Meta", founding_year=2004)

# Create devs
d1 = Dev(name="Nathan")
d2 = Dev(name="Caroline")
d3 = Dev(name="Shadrack")

# Create freebies
f1 = Freebie(item_name="T-Shirt", value=20, company=c1, dev=d1)
f2 = Freebie(item_name="Sticker", value=5, company=c2, dev=d1)
f3 = Freebie(item_name="Coffee Mug", value=15, company=c2, dev=d2)
f4 = Freebie(item_name="Notebook", value=10, company=c3, dev=d3)


f5 = c1.give_freebie(d2, "Pen", 3)
f6 = c3.give_freebie(d3, "Swag Bag", 50)

# Add all instances and commit
session.add_all([c1, c2, c3, d1, d2, d3, f1, f2, f3, f4, f5, f6])
session.commit()

print("✅ Database seeded successfully!")
