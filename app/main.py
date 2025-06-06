from dotenv import load_dotenv
load_dotenv()

from workflow import build_workflow

def main():
    customer_description = """
I am currently employed part-time as a retail associate, earning a monthly income of $2,500. My monthly expenses, including rent, utilities, and other essentials, total about $2,200. I have a credit score of 620 and carry debts amounting to $20,000, primarily from credit cards and a personal loan. My savings are minimal, less than $1,000. I live with a roommate to share living costs and am seeking a loan to consolidate my debts and manage monthly payments more effectively.

"""
    graph = build_workflow()
    result = graph.invoke({"description": customer_description})

    print("\n--- Evaluation Result ---")
    print(f"Risk Score: {result['risk_score']}")

if __name__ == "__main__":
    main()
