import configparser
from operator import itemgetter

import sqlalchemy
from sqlalchemy import create_engine

# columns and their types, including fk relationships
from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

# declarative base, session, and datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


# configuring your database connection
config = configparser.ConfigParser()
config.read('config.ini')

u, pw, host, db = itemgetter('username', 'password', 'host', 'database')(config['db'])
dsn = f'postgresql://{u}:{pw}@{host}/{db}'
print(f'using dsn: {dsn}')

# SQLAlchemy engine, base class and session setup
engine = create_engine(dsn, echo=True)
Base = declarative_base()
Session = sessionmaker(engine)
session = Session()

# Write classes and code here

class AthleteEvent(Base):
    __tablename__ = 'athlete_events'
    
    athlete_event_id = Column('athlete_event_id', Integer, primary_key=True)
    id = Column('id', Integer)
    name = Column('name', String)
    sex = Column('sex', String)
    age = Column('age', Integer)
    height = Column('height', Integer)
    weight = Column('weight', Integer)
    team = Column('team', String)
    noc = Column('noc', String, ForeignKey('noc_region.noc'))
    games = Column('games', String)
    year =  Column('year', Integer)
    season = Column('season', String)
    city = Column('city', String)
    sport = Column('sport', String)
    event = Column('event', String)
    medal = Column('medal', String)
    noc_region = relationship('NOCRegion', back_populates = 'athlete_events')



    def __repr__(self):
        return f'{self.name} - {self.noc} - {self.season} - {self.year} - {self.event} - {self.medal}'
    
    def __str__(self):
        return self.__repr__() 


class NOCRegion(Base):
    __tablename__ = 'noc_region'
    
    noc = Column('noc', String, primary_key=True)
    region = Column('region', String)
    note = Column('note', String)
    athlete_events = relationship('AthleteEvent', back_populates = 'noc_region')

    def __repr__(self):
        return f'{self.noc} - {self.region} - {self.note}'
    
    def __str__(self):
        return self.__repr__() 

Base.metadata.create_all(engine)
new_record = AthleteEvent()
new_record.name = 'Yuto Horigome'
new_record.age = 21
new_record.team = 'Japan'
new_record.medal = 'Gold'
new_record.year = 2020
new_record.season = 'Summer'
new_record.city = 'Tokyo'
new_record.noc = 'JPN'
new_record.sport = 'Skateboarding'
new_record.event = 'Skateboarding, Street, Men'
session.add(new_record)

result = session.query(AthleteEvent).filter(AthleteEvent.noc == 'JPN',AthleteEvent.year >= 2016, AthleteEvent.medal == 'Gold')
for r in result:
    print(r.name, r.noc_region.region, r.event, r.year, r.season)

session.close()

