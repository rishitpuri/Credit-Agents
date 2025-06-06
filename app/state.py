from typing import TypedDict, Optional

class CustomerState(TypedDict):
    description: str
    risk_score: Optional[str]

