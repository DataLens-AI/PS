# import streamlit as st
# from utils.gemini_helper import generate_quiz_questions
# from components.quiz_form import display_quiz_form
# from components.quiz_results import display_results

# def main():
#     st.title("🎯 AI-Powered Quiz Generator")
    
#     # Initialize session state
#     if 'quiz_started' not in st.session_state:
#         st.session_state.quiz_started = False
    
#     # Show configuration only if quiz hasn't started
#     if not st.session_state.quiz_started:
#         st.write("Generate custom quizzes on any topic using Google's Gemini AI!")
        
#         with st.form("quiz_config"):
#             topic = st.text_input("Enter the quiz topic:", placeholder="e.g., World History")
#             num_questions = st.slider("Number of questions:", min_value=1, max_value=10, value=5)
#             difficulty = st.select_slider(
#                 "Select difficulty level:",
#                 options=["Easy", "Medium", "Hard"],
#                 value="Medium"
#             )
            
#             generate_button = st.form_submit_button("Start Quiz")

#         if generate_button:
#             if not topic:
#                 st.warning("Please enter a topic!")
#                 return

#             with st.spinner("Generating your quiz..."):
#                 questions = generate_quiz_questions(topic, num_questions, difficulty)

#             if questions:
#                 # Store questions in session state
#                 st.session_state.questions = questions
#                 # Reset quiz state
#                 st.session_state.current_question = 0
#                 st.session_state.submitted = False
#                 st.session_state.answers = {}
#                 st.session_state.explanations = {}
#                 st.session_state.quiz_started = True
#                 st.experimental_rerun()
    
#     # Display quiz if it's started
#     else:
#         if 'questions' in st.session_state:
#             # Add a restart button
#             if st.sidebar.button("Start New Quiz"):
#                 st.session_state.quiz_started = False
#                 st.session_state.questions = None
#                 st.experimental_rerun()
            
#             if display_quiz_form(st.session_state.questions):
#                 display_results(st.session_state.questions)

# if __name__ == "__main__":
#     main()



import streamlit as st
from utils.gemini_helper import generate_quiz_questions
from components.quiz_form import display_quiz_form
from components.quiz_results import display_results
import PyPDF2  # For processing PDF files
from io import BytesIO


def extract_text_from_pdf(pdf_file):
    """Extracts text from an uploaded PDF file."""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


def main():
    st.title("🎯 AI-Powered Quiz Generator")
    
    # Initialize session state
    if 'quiz_started' not in st.session_state:
        st.session_state.quiz_started = False
    
    # Show configuration only if quiz hasn't started
    if not st.session_state.quiz_started:
        st.write("Generate custom quizzes from any PDF document using Google's Gemini AI!")
        
        with st.form("quiz_config"):
            pdf_file = st.file_uploader("Upload a PDF file:", type=["pdf"])
            num_questions = st.slider("Number of questions:", min_value=1, max_value=10, value=5)
            difficulty = st.select_slider(
                "Select difficulty level:",
                options=["Easy", "Medium", "Hard"],
                value="Medium"
            )
            
            generate_button = st.form_submit_button("Start Quiz")

        if generate_button:
            if not pdf_file:
                st.warning("Please upload a PDF file!")
                return

            with st.spinner("Extracting text from PDF..."):
                try:
                    pdf_text = extract_text_from_pdf(pdf_file)
                except Exception as e:
                    st.error(f"Error reading PDF: {e}")
                    return

            if not pdf_text.strip():
                st.warning("The uploaded PDF doesn't contain any extractable text!")
                return

            with st.spinner("Generating your quiz..."):
                questions = generate_quiz_questions(pdf_text, num_questions, difficulty)

            if questions:
                # Store questions in session state
                st.session_state.questions = questions
                # Reset quiz state
                st.session_state.current_question = 0
                st.session_state.submitted = False
                st.session_state.answers = {}
                st.session_state.explanations = {}
                st.session_state.quiz_started = True
                st.experimental_rerun()
    
    # Display quiz if it's started
    else:
        if 'questions' in st.session_state:
            # Add a restart button
            if st.sidebar.button("Start New Quiz"):
                st.session_state.quiz_started = False
                st.session_state.questions = None
                st.experimental_rerun()
            
            if display_quiz_form(st.session_state.questions):
                display_results(st.session_state.questions)


if __name__ == "__main__":
    main()
