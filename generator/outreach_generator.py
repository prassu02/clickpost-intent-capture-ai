INTENT_MESSAGES = {
    "hiring": "your company is actively hiring and expanding operations.",
    "funding": "your recent funding activity suggests business growth.",
    "expansion": "your recent expansion initiatives indicate increasing customer demand.",
    "leadership": "your recent leadership changes often accompany strategic growth.",
    "complaint": "recent customer experience discussions indicate opportunities to improve post-purchase operations.",
    "general": "recent public activity around your company caught our attention."
}


def get_explanation(reasons):

    reason_list = [r.strip().lower() for r in reasons.split(",")]

    explanation = []

    for reason in reason_list:
        explanation.append(
            INTENT_MESSAGES.get(
                reason,
                INTENT_MESSAGES["general"]
            )
        )

    return " ".join(explanation)


def generate_email(company, reasons):

    explanation = get_explanation(reasons)

    return f"""
Subject: Helping {company} Improve Post-Purchase Experience

Hi {company} Team,

I noticed that {explanation}

As brands grow, delivery tracking, returns, and customer communication become increasingly important.

ClickPost helps brands automate shipment tracking, returns management, delivery notifications, and customer communication while improving customer satisfaction.

Would you be open to a quick 15-minute conversation to explore whether ClickPost could help {company}?

Best Regards,

Prasanna Kumar
AI Engineer
""".strip()


def generate_linkedin(company, reasons):

    explanation = get_explanation(reasons)

    return (
        f"Hi {company} Team! "
        f"I noticed that {explanation} "
        f"ClickPost helps fast-growing eCommerce brands improve delivery tracking, "
        f"returns, and customer communication. "
        f"I'd love to connect and exchange ideas!"
    )