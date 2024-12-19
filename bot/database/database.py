from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:rus_2900@localhost:5432/MusaitTask"

engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'bot_user'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    full_name = Column(String, nullable=True)
    username = Column(String, nullable=True)
    phone_number = Column(String, unique=True, nullable=True)
    telegram_id = Column(String, unique=True, nullable=True)
    tg_username = Column(String, unique=True, nullable=True)
    password = Column(String, nullable=False)

    def __repr__(self):
        return f"<User(email='{self.email}')>"
