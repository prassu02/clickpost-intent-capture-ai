import feedparser
from urllib.parse import quote

from signals.intent_classifier import classify_news


def get_news_signals(company_name, max_results=5):
    """
    Fetch Google News RSS and classify buying intent.
    """

    query = quote(company_name)

    url = (
        f"https://news.google.com/rss/search?q={query}"
        "&hl=en-US&gl=US&ceid=US:en"
    )

    feed = feedparser.parse(url)

    signals = []

    for entry in feed.entries[:max_results]:

        intents, score = classify_news(entry.title)

        signals.append(
            {
                "company": company_name,
                "signal_type": "News",
                "source": "Google News RSS",
                "title": entry.title,
                "link": entry.link,
                "published": getattr(entry, "published", ""),
                "intent": ", ".join(intents) if intents else "General",
                "score": score
            }
        )

    return signals