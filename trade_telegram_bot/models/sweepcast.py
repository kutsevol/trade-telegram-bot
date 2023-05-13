from sqlalchemy import Column, Date, DateTime, Float, Integer, String

from trade_telegram_bot.models.base import Base


class Sweepcast(Base):
    __tablename__ = "sweepcast"
    id = Column(String(100), primary_key=True, unique=True)
    date_timestamp = Column(DateTime)
    ticker = Column(String(10))
    activity_type = Column(String(200))
    put_or_call = Column(String(10))
    sentiment = Column(String(10))
    sweep_score = Column(Float)
    volume = Column(Integer)
    open_interest = Column(Integer)
    strike_price = Column(Float)
    expiration = Column(Date)
    premium = Column(Integer)
    count = Column(Integer)
    price = Column(Float)
