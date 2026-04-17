import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ================================
# 1. Preprocessing
# ================================
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    return text

# ================================
# 2. Skills List
# ================================
skills_list = [
    "python", "sql", "machine learning", "data analysis",
    "data visualization", "statistics", "deep learning",
    "pandas", "scikit learn"
]

def extract_skills(text, skills):
    return [skill for skill in skills if skill in text]

# ================================
# 3. Scoring Function
# ================================
def calculate_scores(resume_clean, jd_clean, resume_skills, jd_skills):
    matched_skills = list(set(resume_skills) & set(jd_skills))
    missing_skills = list(set(jd_skills) - set(resume_skills))

    skill_score = (len(matched_skills) / len(jd_skills)) * 100 if jd_skills else 0

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume_clean, jd_clean])
    cosine_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0] * 100

    final_score = (skill_score * 0.6) + (cosine_score * 0.4)
    eligibility = "Eligible" if final_score >= 60 else "Not Eligible"

    return matched_skills, missing_skills, skill_score, cosine_score, final_score, eligibility

# ================================
# 4. Test Cases
# ================================
def run_tests():
    test_resume = "Python SQL Machine Learning"
    test_jd = "Python SQL Machine Learning Data Visualization"

    rc = preprocess(test_resume)
    jc = preprocess(test_jd)

    rs = extract_skills(rc, skills_list)
    js = extract_skills(jc, skills_list)

    _, _, _, _, final_score, eligibility = calculate_scores(rc, jc, rs, js)

    assert final_score >= 0
    assert eligibility in ["Eligible", "Not Eligible"]

    # Edge case
    test_resume2 = "HTML CSS"
    test_jd2 = "Python SQL"

    rc2 = preprocess(test_resume2)
    jc2 = preprocess(test_jd2)

    rs2 = extract_skills(rc2, skills_list)
    js2 = extract_skills(jc2, skills_list)

    _, _, _, _, final_score2, _ = calculate_scores(rc2, jc2, rs2, js2)

    assert final_score2 >= 0

run_tests()

# ================================
# 5. STREAMLIT APP
# ================================
import streamlit as st

st.title("📄 HR Resume Scanner (Mini ATS)")

resume_input = st.text_area("Paste Resume Text")
jd_input = st.text_area("Paste Job Description")

if st.button("Analyze Resume"):
    if not resume_input.strip() or not jd_input.strip():
        st.error("Please enter both Resume and Job Description")
    else:
        resume_clean = preprocess(resume_input)
        jd_clean = preprocess(jd_input)

        resume_skills = extract_skills(resume_clean, skills_list)
        jd_skills = extract_skills(jd_clean, skills_list)

        matched_skills, missing_skills, skill_score, cosine_score, final_score, eligibility = calculate_scores(
            resume_clean, jd_clean, resume_skills, jd_skills
        )

        st.subheader("📊 Results")
        st.write(f"**Final Score:** {final_score:.2f}%")
        st.write(f"**Eligibility:** {eligibility}")

        st.write("### ✅ Matched Skills")
        st.write(matched_skills)

        st.write("### ❌ Missing Skills")
        st.write(missing_skills)

        