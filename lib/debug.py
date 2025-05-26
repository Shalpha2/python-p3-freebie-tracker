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

    
    print("\nOldest Company:", Company.oldest_company(session).name)

    
    nathan = session.query(Dev).filter_by(name="Nathan").first()
    print("\nDid Nathan receive a T-Shirt?", nathan.received_one("T-Shirt"))
    print("Did Nathan receive a Mug?", nathan.received_one("Mug"))


    caroline= session.query(Dev).filter_by(name="Caroline").first()
    pen = session.query(Freebie).filter_by(item_name="Pen").first()

    print("\nBefore give_away - Pen owned by:", pen.dev.name)
    caroline.give_away(nathan, pen)
    session.commit()
    print("After give_away - Pen now owned by:", pen.dev.name)

    
    print("\nCompanies Alice received freebies from:", [c.name for c in nathan.companies])

    
    meta= session.query(Company).filter_by(name="Meta").first()
    print("Devs who got freebies from OpenAI:", [d.name for d in meta.devs])

    
    #import ipdb; ipdb.set_trace()


