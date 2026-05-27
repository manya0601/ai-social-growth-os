from app.db.database import engine, Base

from app.models.user import User
from app.models.competitor import Competitor
from app.models.social_post import SocialPost
from app.models.trend_analysis import TrendAnalysis

def create_tables():
    Base.metadata.create_all(bind=engine)