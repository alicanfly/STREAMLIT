# 🤖 AI Resume Critiquer

An AI-powered Streamlit app that reviews resumes and provides intelligent feedback based on the job role you’re applying for.

---

## 🔍 Features

- Upload resumes in **PDF** or **TXT**
- Personalized analysis using **OpenAI GPT-3.5**
- Feedback on content, skills, and experience
- Clean UI with robust error handling

---

## 🛠 Tech Stack

- Python, Streamlit
- OpenAI API (GPT-3.5 Turbo)
- PyPDF2, dotenv

---

## ⚙️ Setup

1. Clone the repo & install requirements:

```bash
git clone https://github.com/your-username/streamlit-resume-critiquer.git
cd streamlit-resume-critiquer
pip install -r requirements.txt
````

2. Add your API key to `.env`:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
```

3. Run the app:

```bash
streamlit run main.py
```

---

## 📌 Notes

* `.env` is ignored for safety (listed in `.gitignore`)
* Feedback is generated by GPT and not a substitute for expert career advice

---

## 📄 License

MIT — use freely and improve as needed.

---
