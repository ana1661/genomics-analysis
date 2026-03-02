import streamlit as st
import requests
import json

st.set_page_config(page_title="Cancer Predictor", layout="centered")
st.title("🧬 Cancer Gene Expression Predictor")

st.markdown("""
Paste a **single line** of gene expression values below. It must contain exactly **22,269 comma-separated** numbers.
""")

user_input = st.text_area("Gene Expression Sample (comma-separated)", height=200)

if st.button("Check for Cancer"):
    try:
        # Parse input into list of floats
        values = [float(v.strip()) for v in user_input.split(',') if v.strip() != '']

        if len(values) != 22269:
            st.error(f"⚠️ You entered {len(values)} values. Please enter exactly 22,269 values.")
        else:
            payload = {"features": values}
            headers = {"Content-Type": "application/json"}
            url = "https://994codcwt2.execute-api.us-east-1.amazonaws.com/dev/predict"

            with st.spinner("Sending data to model..."):
                response = requests.post(url, headers=headers, data=json.dumps(payload))

            if response.status_code == 200:
                result = response.json()
                pred = result.get("prediction")
                if pred == 0:
                    st.error("⚠️ The sample is predicted to be **Cancerous**.")
                elif pred == 1:
                    st.success("✅ The sample is predicted to be **Non-Cancerous**.")
                else:
                    st.warning(f"Unexpected response: {result}")
            else:
                st.error(f"Server error: {response.status_code}")

    except Exception as e:
        st.error(f"❌ Failed to process input: {e}")

