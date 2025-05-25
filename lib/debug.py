#!/usr/bin/env python3

# lib/debug.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    companies = session.query(Company).all()
    devs = session.query(Dev).all()
    freebies = session.query(Freebie).all()

    print("Companies:", [c.name for c in companies])
    print("Devs:", [d.name for d in devs])
    print("Freebies:")
    for f in freebies:
        print(f.print_details())

    # Test class method
    print("\nOldest Company:", Company.oldest_company(session).name)

    # Test Dev.received_one
    alice = session.query(Dev).filter_by(name="Alice").first()
    print("\nDid Alice receive a T-Shirt?", alice.received_one("T-Shirt"))
    print("Did Alice receive a Mug?", alice.received_one("Mug"))

    # Test Dev.give_away
    bob = session.query(Dev).filter_by(name="Bob").first()
    pen = session.query(Freebie).filter_by(item_name="Pen").first()

    print("\nBefore give_away - Pen owned by:", pen.dev.name)
    bob.give_away(alice, pen)
    session.commit()
    print("After give_away - Pen now owned by:", pen.dev.name)

    # Test Dev.companies
    print("\nCompanies Alice received freebies from:", [c.name for c in alice.companies])

    # Test Company.devs
    openai = session.query(Company).filter_by(name="OpenAI").first()
    print("Devs who got freebies from OpenAI:", [d.name for d in openai.devs])

    
    #import ipdb; ipdb.set_trace()


