from scraper.news_scraper import get_news_signals
from scraper.jobs_scraper import get_hiring_signals
from scraper.reddit_scraper import get_reddit_signals


def collect_signals(company_name):
    """
    Collect all buying intent signals.
    """

    signals = []

    # News Signals
    news = get_news_signals(company_name)

    if news:
        signals.extend(news)

    # Hiring Signal
    hiring = get_hiring_signals(company_name)

    if hiring:
        signals.append(hiring)

    # Reddit Signal
    reddit = get_reddit_signals(company_name)

    if reddit:
        signals.append(reddit)

    return signals