#  HR Resume Scanner (Mini ATS System)

## Project Overview

This project is a **Resume Screening System** that compares a candidate's resume with a job description and determines their eligibility for the role.

It works like a simplified **Applicant Tracking System (ATS)** used by companies to filter resumes automatically.

---

## Features

* Extracts and processes text from resume and job description
* Identifies key skills from both inputs
* Calculates:

  * Skill Match Score
  * Cosine Similarity Score
* Generates a **Final Score**
* Determines **Eligibility (Eligible / Not Eligible)**
* Interactive **Streamlit Web Interface**

---

## How It Works

1. **Text Preprocessing**

   * Converts text to lowercase
   * Removes special characters using regex

2. **Skill Extraction**

   * Matches predefined skills from resume and job description

3. **Scoring System**

   * Skill Match Score = (Matched Skills / Required Skills)
   * Cosine Similarity using TF-IDF
   * Final Score = Weighted combination

4. **Eligibility Check**

   * If score ≥ 60 → Eligible
   * Else → Not Eligible

---

## Technologies Used

* Python
* Streamlit (for GUI)
* Scikit-learn (TF-IDF & similarity)
* Regular Expressions (`re`)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/hr-resume-scanner.git
cd hr-resume-scanner
```

### 2. Install dependencies

```bash
pip install streamlit scikit-learn pandas
```

---

## Running the App

```bash
streamlit run your_file_name.py
```

Then open:

```
http://localhost:8501
```

---

## Usage

1. Paste resume text
2. Paste job description
3. Click **Analyze Resume**
4. View:

   * Final Score
   * Eligibility
   * Matched Skills
   * Missing Skills

---

## Test Cases

The project includes basic test cases to ensure:

* Scores are valid
* Eligibility output is correct
* Edge cases (no matching skills) are handled

---

## Future Improvements

* Upload PDF resumes
* Advanced NLP (Named Entity Recognition)
* Better UI/UX design
* Deploy app online
* Add more skill datasets

---

## Author

**Karthika K Pillai**

---

## Acknowledgment

This project is built as a learning implementation of ATS systems used in recruitment.

---

## License

This project is for educational purposes.
