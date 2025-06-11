from dotenv import load_dotenv
load_dotenv()

from workflow import build_workflow

def main():
    customer_description = customer_description = """
I am John Carter, a mid-level executive in the tech industry with a stable annual salary and periodic bonuses. I own a Tesla Model 3 and a BMW X5, both fully paid off. My investment portfolio includes shares in Apple, Amazon, and Nvidia. I carry a mortgage on my primary residence and have a manageable student loan balance. My credit score remains strong due to consistent payments and moderate credit utilization. I actively contribute to a retirement fund and maintain an emergency savings account. While I have some debt, it is well-structured and does not impact my overall financial health.
"""


    graph = build_workflow()
    result = graph.invoke({"description": customer_description})

    print("\n--- Evaluation Result ---")
    print(f"Extracted Data: {result.get('extracted_data')}")
    print(f"Financial Ratios: {result.get('financial_ratios')}")
    print(f"Validation Summary: {result.get('validation_summary')}")  # ✅ New
    print(f"Risk Score: {result.get('risk_score')}")
    print(f"Explanation: {result.get('explanation')}")

if __name__ == "__main__":
    main()

