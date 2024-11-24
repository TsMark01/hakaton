from dataclasses import dataclass


@dataclass
class MemberData:
    name: str
    role: bool
    age: int
    favour: tuple[str] = tuple()

@dataclass
class Leisure:
    pass