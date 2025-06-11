from pydantic import BaseModel
from typing import Optional, Dict

class CreditAgentState(BaseModel):
    description: str
    extracted_data: Optional[Dict] = None
    financial_ratios: Optional[Dict] = None
    risk_score: Optional[int] = None
    explanation: Optional[str] = None
    validation_summary: Optional[str] = None  # ✅ NEW FIELD

