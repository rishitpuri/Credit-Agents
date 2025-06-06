# 🧠 Credit Agents: AI-Powered Financial Risk Assessment
## 📌 Overview
Credit Agents is an AI-driven system designed to evaluate customer financial descriptions and provide a risk rating. Leveraging advanced language models and a structured workflow, the system processes unstructured financial narratives to deliver concise risk assessments.

## 🚀 Features
- Natural Language Processing: Understands and interprets unstructured financial descriptions.
- Modular Workflow: Utilizes a sequence of nodes for data extraction, ratio calculation, and risk scoring.
- AI Integration: Employs large language models (LLMs) for entity recognition and analysis.
- Scalable Architecture: Designed for easy integration and scalability.

## 🧩 Project Structure
```
credit-agents/
├── .env                 # Environment variables
├── .gitignore           # Git ignore file
├── LICENSE              # MIT License
├── README.md            # Project documentation
├── requirements.txt     # Python dependencies
├── app/
│   ├── main.py          # Entry point of the application
│   ├── nodes.py         # Node definitions for the workflow
│   ├── state.py         # State management for the workflow
│   └── workflow.py      # Workflow construction and execution
└── data/                # Directory for input/output data
```
## 🔄 Workflow Diagram
Here's a simplified representation of the workflow:

```
graph TD
    A[Start] --> B[Extract Entities]
    B --> C[Calculate Financial Ratios]
    C --> D[Compute Risk Score]
    D --> E[Generate Explanation]
    E --> F[Output Result]
Note: To render the above Mermaid diagram on GitHub, ensure that Mermaid is supported or provide an image alternative.
```
## 🛠️ Technologies Used
- Python 3.13
- LangGraph: For constructing the workflow.
- LangChain: For LLM integration.

## 📦 Installation
### Clone the Repository:

```
# Clone the repository
git clone https://github.com/yourusername/credit-agents.git
cd credit-agents

# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```
Set Up Environment Variables:

- Create a .env file in the root directory.
- Add necessary environment variables (e.g., API keys).

## ⚙️ Usage
### Run the application using:
```
python app/main.py

```
The system will process the predefined customer description and output the risk assessment.

## 📈 Example Outputs
Input Description:

- I have been working full-time as a software engineer for the past 5 years, earning a monthly income of $8,000...

## Output:

Risk Score: 1 

### 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

### 🤝 Contributing
Contributions are welcome! Please open issues or submit pull requests for any enhancements or bug fixes.

