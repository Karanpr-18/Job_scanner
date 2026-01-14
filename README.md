# 📄 CV Job Matcher AI

> 🔗 **Live Demo:** *https://job-scan-app.streamlit.app/*

An AI-powered web application that analyzes how well a candidate's CV matches a given job description. Built with **Streamlit**, **spaCy**, and **scikit-learn**, this tool provides an instant compatibility score to help job seekers tailor their resumes for specific roles.

---

## 🚀 Features

* 📄 Upload CV in **PDF format**
* 📝 Paste any **Job Description**
* 🧠 NLP-based text processing using **spaCy (en_core_web_lg)**
* 📊 Match score calculation using **TF-IDF & Cosine Similarity**
* 🎯 Clear match interpretation (Excellent / Good / Fair / Low)
* 🎨 Clean, responsive, and modern **Streamlit UI**

---

## 🛠️ Tech Stack

* **Frontend / App Framework:** Streamlit
* **NLP:** spaCy (`en_core_web_lg`)
* **ML & Similarity:** scikit-learn (TF-IDF, Cosine Similarity)
* **PDF Parsing:** PyPDF2
* **Language:** Python 3

---

## 📂 Project Structure

```
├── app.py              # Main Streamlit application
├── job_scanner.py      # NLP preprocessing & match score logic
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-link>
cd cv-job-matcher-ai
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Download spaCy Model

```bash
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_lg-3.8.0/en_core_web_lg-3.8.0-py3-none-any.whl
```

### 5️⃣ Run the App

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. The job description and CV text are **cleaned & lemmatized** using spaCy
2. Important keywords are extracted while removing stopwords
3. Texts are converted into vectors using **TF-IDF**
4. **Cosine Similarity** computes how closely the CV matches the job description
5. A percentage score is generated with an easy-to-understand interpretation

---

## 📌 Use Cases

* Job seekers optimizing resumes
* Students applying for internships
* Recruiters doing quick CV screening
* Career coaches & mentors

---

## 👨‍💻 Author

**Karan Bhoriya**

* 🔗 GitHub: [https://github.com/Karanpr-18](https://github.com/Karanpr-18)
* 🔗 LinkedIn: [https://www.linkedin.com/in/karan-bhoriya-b5a3382b7](https://www.linkedin.com/in/karan-bhoriya-b5a3382b7)

---

## 📜 License

This project is open-source and available under the **MIT License**.
