def get_hiring_signals(company_name):
    """
    Demo hiring signal.
    Replace with LinkedIn / Greenhouse scraping later.
    """

    keywords = [
        "Caraway",
        "True Classic",
        "Vuori",
        "Chubbies"
    ]

    if company_name in keywords:

        return {
            "company": company_name,
            "signal_type": "Hiring",
            "source": "Demo",
            "title": f"{company_name} is actively hiring",
            "link": "",
            "published": "",
            "intent": "hiring",
            "score": 20
        }

    return {
        "company": company_name,
        "signal_type": "Hiring",
        "source": "Demo",
        "title": "No hiring signal",
        "link": "",
        "published": "",
        "intent": "General",
        "score": 0
    }