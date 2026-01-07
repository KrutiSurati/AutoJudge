import streamlit as st
import joblib

# Load trained models
tfidf = joblib.load("tfidf_vectorizer.pkl")
clf_model = joblib.load("difficulty_classifier.pkl")
reg_model = joblib.load("difficulty_regressor.pkl")

# Page config
st.set_page_config(
    page_title="AutoJudge",
    page_icon="⚖️",
    layout="centered"
)

# Custom CSS for better UI
st.markdown("""
<style>
    .main {
        background-color: #ffffff;
    }
    .title-text {
        font-size: 40px;
        font-weight: 700;
        color: #ffffff;
        text-align: center;
    }
    .subtitle-text {
        font-size: 16px;
        color: #ffffff;
        text-align: center;
        margin-bottom: 30px;
    }
    .result-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #ffffff;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Title section
st.markdown('<div class="title-text">⚖️ AutoJudge</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle-text">Predict Programming Problem Difficulty using AI</div>',
    unsafe_allow_html=True
)

st.divider()

# Instructions
st.markdown("""
📝 **Instructions**
- Paste the programming problem details below  
- Click **Predict Difficulty**  
- Get the predicted **difficulty class** and **numerical score**
""")

# Input form
with st.form("prediction_form"):
    st.subheader("📌 Problem Details")

    title = st.text_input("Problem Title")

    description = st.text_area(
        "Problem Description",
        height=180,
        placeholder="Enter the complete problem description here..."
    )

    input_desc = st.text_area(
        "Input Description",
        height=130,
        placeholder="Describe the input format..."
    )

    output_desc = st.text_area(
        "Output Description",
        height=130,
        placeholder="Describe the output format..."
    )

    submit = st.form_submit_button("🚀 Predict Difficulty")

# Prediction logic
if submit:
    combined_text = " ".join([title, description, input_desc, output_desc])

    if combined_text.strip() == "":
        st.warning("⚠️ Please enter at least some problem details.")
    else:
        X_input = tfidf.transform([combined_text])

        predicted_class = clf_model.predict(X_input)[0]
        predicted_score = reg_model.predict(X_input)[0]

        # Results
        st.markdown('<div class="result-box">', unsafe_allow_html=True)

        st.markdown("### ✅ Prediction Results")
        st.success(f"📊 **Difficulty Class:** {predicted_class.upper()}")
        st.info(f"🔢 **Difficulty Score:** {round(predicted_score, 2)}")

        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.divider()
st.markdown(
    "<center>Built using Streamlit | AutoJudge Project</center>",
    unsafe_allow_html=True
)

