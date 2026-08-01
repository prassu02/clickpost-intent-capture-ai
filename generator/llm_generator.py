import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_ai_email(company, reason):

    prompt = f"""
Write a professional cold outreach email.

Company: {company}

Buying Intent:
{reason}

Product:
ClickPost

Explain how ClickPost can help improve logistics,
shipment tracking,
returns,
delivery notifications,
customer experience.

Keep it under 180 words.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content