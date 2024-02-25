from sqlalchemy import Column, Integer, String, Date, Float, Time, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from typing import Optional,List
from app.database import Base
import datetime
from datetime import datetime, time

class Pilot(Base):
    __tablename__= 'pilots'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    surname: Mapped[str] = mapped_column(String(30), nullable=False)
    typeRate: Mapped[str] = mapped_column(String(30), nullable=False)
    instructorCategory: Mapped[str] = mapped_column(String(2), nullable=False)
    flights: Mapped[List["Flight"]] = relationship(back_populates="pilot")
    
    
    
    def __init__(self, name=None, surname=None, typeRate=None, instructorCategory=None):
        self.name = name
        self.surname = surname
        self.typeRate = typeRate
        self.instructorCategory = instructorCategory
        
    def __repr__(self):
        return self.surname
    
class Flight(Base):
    __tablename__= 'flights'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    #pilot: Mapped[str] = mapped_column(String(30), nullable=False)
    flightType: Mapped[str] = mapped_column(String(30), nullable=False)
    takeoff: Mapped[time] = mapped_column(Time, nullable=False)
    flightDuration: Mapped[float] = mapped_column(Float(2), nullable=False)
    landings: Mapped[int] = mapped_column(nullable=False)
    SFO: Mapped[int] = mapped_column(nullable=False)
    missionAccomplished: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    pilot_id: Mapped[int] = mapped_column(ForeignKey("pilots.id"))
    pilot: Mapped["Pilot"] = relationship(back_populates="flights")
    
    
    
    """ def __init__(self, date=None, pilot=None, flightType=None, takeoff=None, flightDuration=None, landings=None, SFO=None, missionAccomplished=None):
        self.date = date
        self.pilot = pilot
        self.flightType = flightType
        self.takeoff = takeoff
        self.flightDuration = flightDuration
        self.landings = landings
        self.SFO = SFO
        self.missionAccomplished = missionAccomplished """
        
    def __repr__(self):
        return f'<Flight {self.date!r}>'