import streamlit as st
import subprocess
def main():
    st.markdown("""
        <style>
        .stButton>button {
            width: 100%;
            height: 50px;
            font-size: 18px;
            font-weight: bold;
            border-radius: 10px;
            margin-bottom: 10px;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("🚀 Multi-Feature Streamlit App")
    
    st.write("### Choose an Option:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
         if st.button("🧠 Quiz"):
            st.success("Launching Quiz App...")
            quiz_path = r"D:\4-1\PS1\integration\QuizApp\project"  # Change to your actual path
            quiz_script = "quiz_app.py"  # Name of the quiz Streamlit app file
            
            subprocess.run(f"cd {quiz_path} && streamlit run {quiz_script}", shell=True)
 

         if st.button("🤖 Chatbot"):
            st.success("Launching Chat App...")
            quiz_path = r"D:\4-1\PS1\integration\AI-Image-Recogniton-Chatbot-LLM-Model\AI-Image-Recogniton-Chatbot-LLM-Model"  # Change to your actual path
            quiz_script = "vision-chat.py"  # Name of the quiz Streamlit app file
            
            subprocess.run(f"cd {quiz_path} && streamlit run {quiz_script}", shell=True)
    
    with col2:
        if st.button("🖥️ Visual Studio"):
            st.success("Launching Quiz App...")
            quiz_path = r"D:\4-1\PS1\integration\AI-Studio"  # Change to your actual path
            quiz_script = "Home.py"  # Name of the quiz Streamlit app file
            
            subprocess.run(f"cd {quiz_path} && streamlit run {quiz_script}", shell=True)
    
        if st.button("📜 Codex"):
            st.success("You clicked on Codex!")
            # Add Codex-related functionality here
    
    with col3:
        if st.button("📊 EDA"):
            st.success("Launching EDA App...")
            eda_path = r"D:\4-1\PS1\integration\AutoEDA-main"  
            eda_script = "main.py"  # Name of the quiz Streamlit app file
            
            subprocess.run(f"cd {eda_path} && streamlit run {eda_script}", shell=True)
    
        if st.button("🐍 pyWalker"):
            st.success("Launching PyGWalker App...")
            eda_path = r"D:\4-1\PS1\integration\pygW"  
            eda_script = "app.py"  # Name of the quiz Streamlit app file
            
            subprocess.run(f"cd {eda_path} && streamlit run {eda_script}", shell=True)
            # Add pyWalker functionality here

if __name__ == "__main__":
    main()
