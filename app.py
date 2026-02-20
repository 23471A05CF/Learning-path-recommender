import streamlit as st
from recommender import recommend_courses

st.set_page_config(
    page_title="Learning Path Recommender",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 AI Learning Path Recommender")
st.markdown("Personalized course suggestions based on your profile")

name = st.text_input("👤 Your Name")

domain = st.selectbox(
    "📚 Select Your Interest",
    ["AI", "Data Science", "Web Development"]
)

level = st.selectbox(
    "📊 Select Your Level",
    ["Beginner", "Intermediate", "Advanced"]
)

if st.button("🚀 Generate Learning Path"):
    if name:
        st.success(f"Hello {name}! Here is your learning path 👇")
        result = recommend_courses(domain, level)

        if result.empty:
            st.warning("No courses found for your selection.")
        else:
            st.dataframe(result, use_container_width=True)
    else:
        st.error("Please enter your name")