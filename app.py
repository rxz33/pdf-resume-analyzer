import streamlit as st
import requests

st.title("📄 PDF to Resume Analyzer")

# Upload PDF file
uploaded_file = st.file_uploader("Upload your resume PDF", type=["pdf"])

# Select job role
job_roles = [
    "Frontend Developer",
    "Backend Developer",
    "Data Scientist",
    "Product Manager",
    "Designer"
]
job_role = st.selectbox("Select Job Role", job_roles)

if st.button("Analyze Resume"):

    if uploaded_file is None:
        st.error("Please upload a resume PDF file!")
    else:
        with st.spinner("Analyzing..."):
            # Prepare multipart form-data
            files = {"file": (uploaded_file.name, uploaded_file, "application/pdf")}
            data = {"job_role": job_role}
            
            try:
                response = requests.post("https://pdf-resume-analyzer.onrender.com", files=files, data=data)
                response.raise_for_status()
                result = response.json()
                st.success("Analysis complete!")
                st.markdown(result["feedback"])
            except requests.exceptions.RequestException as e:
                st.error(f"API request failed: {e}")

