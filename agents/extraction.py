
from openai import OpenAI
from utils.prompt import extraction_prompt

client = OpenAI()

class ExtractionAgent:
    def run(self, text):
        prompt = extraction_prompt(text)
        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return res.choices[0].message.content
