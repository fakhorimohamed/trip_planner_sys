# ✈️ AI Travel Planner System

An intelligent AI-powered travel planning assistant built using **LangGraph**, **LangChain**, and LLMs (GROQ). The system leverages AI agents and specialized tools to generate personalized travel itineraries, search for destinations, retrieve weather information, convert currencies, and perform travel-related calculations.

---

## 🚀 Features

-  Agentic workflow powered by LangGraph
-  Intelligent place search
-  Real-time weather information
-  Currency conversion
-  Calculator tool
-  Export travel plans to documents
-  YAML-based configuration
-  Experimentation with Jupyter Notebook

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/trip_planner_sys.git
```

Move into the project directory:

```bash
cd trip_planner_sys
```

---

## 2. Deactivate any active Conda environment (Optional)

If your terminal shows an active Conda environment, deactivate it before creating the project's virtual environment.

Example:

Before:

```text
(base) PS C:\Users\hp>
```

Deactivate:

```bash
conda deactivate
```

Repeat if necessary until your prompt looks like:

```text
PS C:\Users\hp>
```

---

## 3. Create a virtual environment

```bash
uv venv
```

---

## 4. Activate the virtual environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## 5. Install dependencies

```bash
uv sync
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

Example:

```env
GOOGLE_API_KEY=your_google_api_key
OPENAI_API_KEY=your_openai_api_key
```

> **Note:** Never commit your `.env` file to GitHub.

---

## ▶️ Running the Project

Run the application:

```bash
python app.py
```

or

```bash
python main.py
```


---

## 👨‍💻 Author

**Mohamed Elfakhori**

Master's Student in **Web Intelligence & Data Science (WISD)**

Interested in:

- Artificial Intelligence
- Large Language Models (LLMs)
- Agentic AI
- LangGraph
- Retrieval-Augmented Generation (RAG)
- Machine Learning
- Data Science

GitHub:
https://github.com/fakhorimohamed

LinkedIn:
[www.linkedin.com/in/mohamed-el-fakhori-89a87624b](https://www.linkedin.com/in/mohamed-el-fakhori)

---