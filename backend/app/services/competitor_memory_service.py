from app.scrapers.twitter_scraper import scrape_twitter_competitor

from app.services.memory_service import store_memory

def ingest_competitor_posts():

    posts = scrape_twitter_competitor()

    stored_count = 0

    for post in posts:

        metadata = {
            "platform": post["platform"],
            "engagement_score": post["engagement"],
            "source": "competitor"
        }

        store_memory(
            post["content"],
            metadata
        )

        stored_count += 1

    return {
        "stored_posts": stored_count
    }