from sqlalchemy import Column, Integer, String, Text

from app.db.database import Base

class SocialPost(Base):
    __tablename__ = "social_posts"

    id = Column(Integer, primary_key=True, index=True)

    platform = Column(String)
    content = Column(Text)
    engagement_score = Column(Integer)