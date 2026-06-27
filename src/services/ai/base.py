from abc import ABC, abstractmethod

class AIProvider(ABC):
    """Abstract AI provider interface."""

    @abstractmethod
    def chat(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.1,
    ) -> str:
        """Generate a chat completion."""
        raise NotImplementedError