from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()   
engine = create_engine("sqlite:///chatbot.db")
Session = sessionmaker(bind=engine)


class Booking(Base):
    __tablename__ = 'reservation'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    number_sits = Column(Integer)
    event = Column(String)


    


class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    description = Column(String)
    location = Column(String)
    available_sits = Column(Integer)
    total_sits = Column(Integer)
    date_time = Column(DateTime)


# Creazione delle tabelle DOPO aver definito tutti i modelli
Base.metadata.create_all(engine)


class Database:
    def __init__(self):
        pass

    def salva_prenotazione(self, name, event, number_sits):
        # Gestione sicura della sessione
        with Session() as session:
            evento = session.query(Event).filter_by(name=event).first()

            if evento:
                evento.available_sits -= number_sits
                session.add(evento)

            prenotazione = Booking(name=name, event=event, number_sits=number_sits)
            session.add(prenotazione)

            session.commit()

    


# Istanza globale
db = Database()
