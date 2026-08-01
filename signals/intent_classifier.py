INTENT_RULES = {
    "hiring": [
        "hiring",
        "recruiting",
        "job opening",
        "careers",
    ],
    "funding": [
        "funding",
        "raised",
        "investment",
        "series a",
        "series b",
    ],
    "expansion": [
        "expand",
        "expansion",
        "new store",
        "launch",
        "growth",
    ],
    "leadership": [
        "ceo",
        "chief",
        "president",
        "executive",
        "leadership",
    ],
}


def classify_news(text):
    """
    Returns:
    (matched_intents, score)
    """

    text = str(text).lower()

    matched = []
    score = 5

    for intent, keywords in INTENT_RULES.items():

        for keyword in keywords:

            if keyword in text:
                matched.append(intent)
                score += 10
                break

    return matched, score