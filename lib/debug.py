#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Company, Dev, Freebie

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Sample queries to use in ipdb
    companies = session.query(Company).all()
    devs = session.query(Dev).all()
    freebies = session.query(Freebie).all()

    # Print some results
    print("Companies:", [c.name for c in companies])
    print("Devs:", [d.name for d in devs])
    print("Freebies:", [f.print_details() for f in freebies])

    # Test aggregate methods (optional)
    print("Oldest Company:", Company.oldest_company(session).name)
    print("Alice received a T-Shirt?", devs[0].received_one("T-Shirt"))
    
    # Enter interactive debugging shell
   
    #import ipdb; ipdb.set_trace()

