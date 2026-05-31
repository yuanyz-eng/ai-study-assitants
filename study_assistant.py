import streamlit as st
from pypdf import PdfReader
from datetime import date

# ------------------
# PAGE CONFIG
# ------------------

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚",
    layout="wide"
)

# ------------------
# CUSTOM CSS
# ------------------

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.stButton>button {
    border-radius: 10px;
    height: 45px;
    width: 100%;
}

.card {
    background-color: #1E1E1E;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)

# ------------------
# SIDEBAR
# ------------------

with st.sidebar:

    st.title("📚 AI Study Assistant")

    menu = st.radio(
        "Menu",
        [
            "Dashboard",
            "Chat AI",
            "Summary",
            "Study Plan"
        ]
    )

# ------------------
# DASHBOARD
# ------------------

if menu == "Dashboard":

    st.title("📚 AI Study Assistant")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Documents", "12")

    with col2:
        st.metric("Study Hours", "35")

    with col3:
        st.metric("Quiz Score", "88%")

    st.divider()

    st.subheader("Learning Progress")

    st.progress(70)

# ------------------
# CHAT
# ------------------

elif menu == "Chat AI":

    st.title("🤖 AI Chat")

    question = st.text_input(
        "Ask your question"
    )

    if st.button("Send"):

        if question:

            st.success(
                f"Question: {question}"
            )

            st.info(
                "This is where OpenAI/Ollama answer will appear."
            )

# ------------------
# SUMMARY
# ------------------

elif menu == "Summary":

    st.title("📄 PDF Summary")

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if uploaded_file:

        pdf = PdfReader(uploaded_file)

        text = ""

        for page in pdf.pages:
            text += page.extract_text()

        st.subheader("Preview")

        st.write(text[:1000])

        if st.button("Generate Summary"):

            summary = text[:500]

            st.success("Summary Generated")

            st.write(summary)

# ------------------
# STUDY PLAN
# ------------------

elif menu == "Study Plan":

    st.title("📅 Study Planner")

    subject = st.text_input(
        "Subject"
    )

    exam_date = st.date_input(
        "Exam Date",
        date.today()
    )

    hours = st.slider(
        "Hours per day",
        1,
        8,
        2
    )

    if st.button("Create Plan"):

        st.success(
            f"""
            Study Plan for {subject}

            Day 1 → Read Chapter 1

            Day 2 → Read Chapter 2

            Day 3 → Practice Questions

            Day 4 → Review

            Day 5 → Mock Exam

            {hours} hours/day
            """
        )