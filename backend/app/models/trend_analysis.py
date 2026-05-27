from sqlalchemy import Column, Integer, String, Text

from app.db.database import Base

class TrendAnalysis(Base):
    __tablename__ = "trend_analysis"

    id = Column(Integer, primary_key=True, index=True)

    trend_name = Column(String)
    platform = Column(String)
    virality_score = Column(Integer)
    analysis = Column(Text)