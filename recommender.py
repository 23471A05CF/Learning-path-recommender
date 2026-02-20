import pandas as pd

def recommend_courses(domain, level):
    df = pd.read_csv("data/courses.csv")
    recommendations = df[
        (df["domain"] == domain) &
        (df["level"] == level)
    ]
    return recommendations