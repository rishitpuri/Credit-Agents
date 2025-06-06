import os
import requests
import json
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def call_deepseek(messages, model="deepseek/deepseek-r1:free"):
    payload = {
        "model": model,
        "messages": messages
    }
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

def extract_financial_entities(state: Dict[str, Any]) -> Dict[str, Any]:
    description = state["description"]
    prompt = f"""
Based on the following customer's financial background, assess their risk level for loan approval on a scale from 1 (low risk) to 5 (high risk). Provide only the risk rating number.

Customer Description:
\"\"\"
{description}
\"\"\"
"""
    messages = [
        {"role": "system", "content": "You are a financial risk assessment assistant."},
        {"role": "user", "content": prompt}
    ]
    response = call_deepseek(messages)
    state["risk_score"] = response.strip()
    return state


def compute_financial_ratios(state: Dict[str, Any]) -> Dict[str, Any]:
    data = state["extracted_data"]
    income = float(data.get("income", 0))
    expenses = float(data.get("expenses", 0))
    debt = float(data.get("debt", 0))

    dti = (debt / income) if income else None
    savings_rate = ((income - expenses) / income) if income else None

    state["financial_ratios"] = {
        "dti": round(dti, 2) if dti is not None else None,
        "savings_rate": round(savings_rate, 2) if savings_rate is not None else None
    }
    return state

def assess_risk(state: Dict[str, Any]) -> Dict[str, Any]:
    ratios = state["financial_ratios"]
    data = state["extracted_data"]
    dti = ratios.get("dti")
    savings_rate = ratios.get("savings_rate")
    credit_score = int(data.get("credit_score", 0))
    employment_status = data.get("employment_status", "").lower()

    risk_score = 3  # Default risk

    if dti is not None:
        if dti > 0.5:
            risk_score += 1
        elif dti < 0.3:
            risk_score -= 1

    if savings_rate is not None:
        if savings_rate < 0.1:
            risk_score += 1
        elif savings_rate > 0.2:
            risk_score -= 1

    if credit_score >= 750:
        risk_score -= 1
    elif credit_score < 600:
        risk_score += 1

    if employment_status in ["unemployed", "student"]:
        risk_score += 1
    elif employment_status in ["full-time", "self-employed"]:
        risk_score -= 0.5

    risk_score = max(1, min(5, round(risk_score)))
    state["risk_score"] = risk_score
    return state

def generate_explanation(state: Dict[str, Any]) -> Dict[str, Any]:
    description = state["description"]
    risk_score = state["risk_score"]
    prompt = f"""
You are a financial risk analyst. Given the following customer description and assigned risk score, provide a concise explanation for the risk assessment.

Customer Description:
\"\"\"
{description}
\"\"\"

Assigned Risk Score: {risk_score}

Explanation:
"""
    messages = [
        {"role": "system", "content": "You are a financial risk analyst."},
        {"role": "user", "content": prompt}
    ]
    response = call_deepseek(messages)
    state["explanation"] = response.strip()
    return state
