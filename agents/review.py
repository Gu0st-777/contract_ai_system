
from openai import OpenAI
from utils.prompt import review_prompt

client = OpenAI()

class ReviewAgent:
    def run(self, clauses, risks):
        prompt = review_prompt(clauses, risks)
        res = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return res.choices[0].message.content
