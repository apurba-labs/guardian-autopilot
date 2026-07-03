from __future__ import annotations

from openai import OpenAI

from config.settings import get_settings


def main() -> None:
    settings = get_settings()

    client = OpenAI(
        api_key=settings.dashscope_api_key,
        base_url=settings.qwen_base_url,
    )

    response = client.chat.completions.create(
        model=settings.qwen_model,
        messages=[
            {
                "role": "user",
                "content": (
                    "Reply with exactly: "
                    "'Hello from Qwen Cloud! Connection successful.'"
                ),
            }
        ],
        temperature=0,
    )

    print("\n========== Qwen Cloud ==========\n")
    print(response.choices[0].message.content)
    print("\n================================\n")


if __name__ == "__main__":
    main()