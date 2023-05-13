from sqlalchemy import Column, Date, DateTime, Float, Integer, String

from trade_telegram_bot.models.base import Base


class Option(Base):
    __tablename__ = "option"
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Integer)
    date = Column(DateTime)
    ticker = Column(String(10))
    expiration = Column(Date)
    strike_price = Column(Float)
    put_or_call = Column(String(10))
