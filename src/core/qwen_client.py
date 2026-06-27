from __future__ import annotations

from openai import OpenAI

from config.settings import get_settings


class QwenClient:
    """Reusable Qwen Cloud client."""

    def __init__(self) -> None:
        settings = get_settings()

        self.client = OpenAI(
            api_key=settings.qwen_api_key,
            base_url=settings.qwen_base_url,
        )

        self.model = settings.qwen_model

    def chat(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.1,
    ) -> str:
        """Execute a chat completion."""

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=temperature,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
        )

        return response.choices[0].message.content or ""