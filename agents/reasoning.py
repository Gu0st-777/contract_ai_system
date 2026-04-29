
from openai import OpenAI
from utils.prompt import reasoning_prompt
from rag.vector_store import search_knowledge

client = OpenAI()

class ReasoningAgent:
    def run(self, clauses):
        knowledge = search_knowledge(clauses)
        prompt = reasoning_prompt(clauses, knowledge)
        res = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return res.choices[0].message.content
