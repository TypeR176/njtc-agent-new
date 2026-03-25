import streamlit as st
from agent.react_agent import ReactAgent
import time

st.set_page_config(
    page_title="智能助手",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
.stApp {
    background-color: #f8f9fa;
}

.stChatMessage {
    background-color: white;
    border-radius: 8px;
    padding: 12px 16px;
    margin: 8px 0;
    box-shadow: 0 1px 3px rgba(0,0,0,0.08);
}

.stChatMessage[data-testid="user"] {
    background-color: #007bff;
    color: white;
}

.stChatMessage[data-testid="assistant"] {
    background-color: white;
    color: #333;
}

.stTextInput>div>div>input {
    background-color: white;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
}

.stTextInput>div>div>input:focus {
    border-color: #007bff;
}
</style>
""", unsafe_allow_html=True)

st.title("🤖 智能助手")
st.caption("内江师范学院")

st.divider()

if "agent" not in st.session_state:
    st.session_state["agent"] = ReactAgent()

if "message" not in st.session_state:
    st.session_state["message"] = []

for message in st.session_state["message"]:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("输入您的问题...")

if prompt:
    st.chat_message("user").write(prompt)
    st.session_state["message"].append({"role": "user", "content": prompt})

    response_messages = []
    with st.spinner("思考中..."):
        res_stream = st.session_state["agent"].execute_stream(prompt)

        def capture(generator, cache_list):
            for chunk in generator:
                cache_list.append(chunk)
                for char in chunk:
                    time.sleep(0.005)
                    yield char

        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            full_response = ""
            
            for chunk in capture(res_stream, response_messages):
                full_response += chunk
                response_placeholder.write(full_response)
            
            st.session_state["message"].append({"role": "assistant", "content": response_messages[-1]})
            
        st.rerun()

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("清空对话", use_container_width=True):
        st.session_state["message"] = []
        st.rerun()
