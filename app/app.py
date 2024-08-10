import streamlit as st
from src.agent import Agent
from langchain.callbacks import StreamlitCallbackHandler

agent = Agent().agent
st.set_page_config(page_title="Numerix")
st.title("Numerix")

# Initializing streamlit session state
if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {
            "role":"assistant",
            "content":"Hi, I'm a Numerix a GenAI based mathematical problem solving Agent"
        }
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])

st.subheader("Question")
question = st.text_input("Put your question here...")
if st.button("Answer"):
    if question:
        with st.spinner("Generate response.."):
            st.session_state.messages.append({
                "role":"user",
                "content":question
            })
            st.chat_message("user").write(question)

            st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            response = agent.run(st.session_state.messages,callbacks = [st_cb]
                                         )
            st.session_state.messages.append({'role':'assistant',"content":response})
            st.write('### Response:')
            st.success(response)

    else:
        st.warning("Please enter the question")
