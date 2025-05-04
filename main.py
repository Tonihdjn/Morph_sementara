import streamlit as st
import ollama
import voice 
# Sidebar navigation
st.set_page_config(page_title="Morph.AI",page_icon="morph_logo.png")
st.sidebar.title("Navigation")
client = ollama.Client()
def response(prompt, model): 
        response = client.generate(model=model, prompt=prompt)
        return response['response']
page = st.sidebar.radio("Go to", ["DASHBOARD", "SIDEKICK", "PERSONAL PSYCOLOG", "Conflict Ressolution"])
if page == "DASHBOARD":
    st.title("🤖 WELCOME TO MORPH.AI 🤖")
    print("taruh piz")
elif page == "SIDEKICK":
    st.title("🦾 SIDEKICK Voice Assistant")
    SIDEKICK = "JINGS.SIDEKICK"
    if "sidekick_history" not in st.session_state:
        st.session_state.sidekick_history = []
    for msg in st.session_state.sidekick_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    col1, col2 = st.columns([1, 2])
    with col1:
        if st.button("🎤 Speak"):
            with st.spinner("Listening..."):
                user_text = voice.spToText()
    with col2:
        user_text_fallback = st.text_input("Or type here...")
    user_text = user_text if "user_text" in locals() and user_text else user_text_fallback
    if user_text and user_text.lower() not in {"quit", "exit"}:
        st.session_state.sidekick_history.append({"role": "user", "content": user_text})
        with st.chat_message("user"):
            st.markdown(user_text)
        with st.chat_message("assistant"):
            with st.spinner("SIDEKICK is thinking..."):
                ai_response = response(user_text, SIDEKICK)
                st.markdown(ai_response)
        voice.SpeakText(ai_response)
        st.session_state.sidekick_history.append({"role": "assistant", "content": ai_response})

    elif user_text.lower() in {"quit", "exit"}:
        st.write("👋 Goodbye!")
        voice.SpeakText("Goodbye!")
elif page == "PERSONAL PSYCOLOG" : 
    st.title("🙂 Consult with Pycolog 🙂")
    pycolog = "JINGS.pycolog"
    if "messages_Pycolog" not in st.session_state:
        respon = response("hello", pycolog)
        st.session_state["messages_Pycolog"] = [{"role": "assistant", "content": respon}]
    for msg in st.session_state["messages_Pycolog"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    user_input = st.chat_input("Type your message...")
    if user_input:
        st.session_state["messages_Pycolog"].append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                respon = response(user_input, pycolog)
                st.markdown(respon)
        st.session_state["messages_Pycolog"].append({"role": "assistant", "content": respon})

elif page == "Conflict Ressolution" : 
    st.title("🙂 Consult with Raya mediator 🙂")
    CRE = "JINGS.CR"
    if "messages_CRE" not in st.session_state:
        respon = response("hello", CRE)
        st.session_state["messages_CRE"] = [{"role": "assistant", "content": respon}]
    for msg in st.session_state["messages_CRE"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    user_input = st.chat_input("Type your message...")
    if user_input:
        st.session_state["messages_CRE"].append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                respon = response(user_input, CRE)
                st.markdown(respon)
        st.session_state["messages_CRE"].append({"role": "assistant", "content": respon})