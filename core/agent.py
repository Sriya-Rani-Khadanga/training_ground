import os
from openai import OpenAI

class Agent:
    def __init__(self, system_prompt=None, model=None):
        self.model = model or os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
        self.system_prompt = system_prompt or "You are a helpful agent."
        self.client = OpenAI(
            base_url=os.getenv("API_BASE_URL", "https://router.huggingface.co/v1"),
            api_key=os.getenv("HF_TOKEN") or os.getenv("API_KEY"),
        )

    def run(self, user_input: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user",   "content": user_input},
            ],
            temperature=0.0,
            max_tokens=512,
        )
        return response.choices[0].message.content

    def swap_model(self, new_model: str):
        self.model = new_model
        print(f"[Agent] swapped model → {new_model}")

    def patch_prompt(self, patch: str):
        self.system_prompt = self.system_prompt + "\n\n" + patch