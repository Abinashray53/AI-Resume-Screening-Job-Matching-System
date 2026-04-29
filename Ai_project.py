from pdfminer.high_level import extract_text
text = extract_text("resume.pdf")
print(text)
import nltk
from nltk.corpus import stopwords
import re
nltk.download('stopwords')
def clean_text(text):
    text = re.sub(r'\W', ' ', text)
    text = text.lower()
    words = text.split()
    words = [w for w in words if w not in stopwords.words('english')]
    return " ".join(words)
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([resume_text, job_description])
from sklearn.metrics.pairwise import cosine_similarity
score = cosine_similarity(vectors[0], vectors[1])
print("Match Score:", score[0][0])
import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp(resume_text)
skills = [ent.text for ent in doc.ents]
print(skills)
import streamlit as st
st.title("AI Resume Matcher")
resume = st.file_uploader("Upload Resume")
job_desc = st.text_area("Paste Job Description")
if st.button("Analyze"):
    st.write("Match Score:", score)