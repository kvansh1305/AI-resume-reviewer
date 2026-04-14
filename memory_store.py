from collections import deque
from dataclasses import dataclass, field

@dataclass
class MemoryStore:
    history: deque = field(default_factory=lambda: deque(maxlen=10))

    def add(self, role: str, content: str):
        self.history.append({"role": role, "content": content})

    def get_context(self) -> str:
        if not self.history:
            return ""
        return "\n".join(
            f"{m['role'].upper()}: {m['content']}" for m in self.history
        )

    def clear(self):
        self.history.clear()

memory = MemoryStore()