def get_reddit_signals(company_name):
    """
    Placeholder Reddit signal.
    Future version can integrate Reddit API (PRAW).
    """

    return {
        "company": company_name,
        "signal_type": "Reddit",
        "source": "Demo",
        "title": f"No Reddit discussion found for {company_name}",
        "link": "",
        "published": "",
        "intent": "General",
        "score": 0
    }