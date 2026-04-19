import os
import time
from app.utils.logger import get_logger
from app.utils.constants import SUPPORTED_PROVIDERS, DEFAULT_ANTHROPIC_MODEL

logger = get_logger(__name__)


class ModelClient:
    def __init__(self):
        self.provider = os.getenv("PROVIDER", "openai").lower()
        self.model = os.getenv("MODEL", "gpt-4o-mini")

        if self.provider not in SUPPORTED_PROVIDERS:
            raise ValueError(f"Unsupported provider: {self.provider}")

        if self.provider == "anthropic" and "gpt" in self.model:
            logger.warning("Switching to default Anthropic model")
            self.model = DEFAULT_ANTHROPIC_MODEL

    def generate(self, prompt: str, retries: int = 2, delay: int = 2) -> str:
        for attempt in range(retries + 1):
            try:
                if self.provider == "anthropic":
                    return self._call_anthropic(prompt)
                return self._call_openai(prompt)

            except Exception as e:
                logger.error(f"LLM call failed (attempt {attempt+1}): {e}")
                time.sleep(delay)

        raise RuntimeError("LLM call failed after retries")

    def _call_openai(self, prompt: str) -> str:
        from openai import OpenAI

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        res = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        return res.choices[0].message.content

    def _call_anthropic(self, prompt: str) -> str:
        import anthropic

        client = anthropic.Anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )

        res = client.messages.create(
            model=self.model,
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}]
        )

        return res.content[0].text
