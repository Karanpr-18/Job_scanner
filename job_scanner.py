from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy
import subprocess
import sys

model_name = "en_core_web_lg"


nlp = spacy.load('en_core_web_lg')

def __init__(job_desc, cv_text):

    job_desc = job_desc.lower()

    doc=nlp(job_desc)
    
    job_tokens=[]
    for token in doc:
        if token.is_punct or token.is_stop:
            continue
        job_tokens.append(token.lemma_)
    job= " ".join(job_tokens)

    cv_desc = cv_desc.lower()

    doc=nlp(cv_desc)
    
    cv_tokens=[]
    for token in doc:
        if token.is_punct or token.is_stop:
            continue
        cv_tokens.append(token.lemma_)
    cv= " ".join(cv_tokens)

    return calculate_match_score(job, cv)

def calculate_match_score(job_desc, cv_text):
    model = TfidfVectorizer()
    vectors = model.fit_transform([job_desc, cv_text])
    cosine_sim = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    score = round(cosine_sim * 100, 2)
    return score

import en_core_web_lg
print(en_core_web_lg.__file__)
