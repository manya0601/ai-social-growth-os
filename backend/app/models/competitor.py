from sqlalchemy import Column, Integer, String

from app.db.database import Base

class Competitor(Base):
    __tablename__ = "competitors"

    id = Column(Integer, primary_key=True, index=True)

    company_name = Column(String, index=True)

    instagram_handle = Column(String)
    twitter_handle = Column(String)
    linkedin_url = Column(String)