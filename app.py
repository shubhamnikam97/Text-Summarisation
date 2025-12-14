import streamlit as st
import validators
from langchain_classic.chains.summarize import load_summarize_chain
from langchain_groq import ChatGroq
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
from langchain_core.prompts import PromptTemplate
from langchain_classic.schema import Document


# Streamlit app
# st.set_page_config(page_title="LangChain: Summarize Text From Website", page_icon="🦜")
st.title("🦜 LangChain: Summarize Text From Website")
st.subheader("Summarize URL")

# Get groq api key and url (Youtube or website) to summarize
with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", value="", type="password")

generic_url = st.text_input("URL", label_visibility="collapsed")

# Prompt template
prompt_template="""
Provide the summary of following content in 300 words.
Content:{text}
"""

prompt = PromptTemplate(template=prompt_template, input_variable=["text"])

if st.button("Summarize the Content from Website"):
    # Validate all the inputs url and groq api
    if not groq_api_key.strip() and not generic_url.strip():
        st.error("Please provide the information to get started.")
    elif not validators.url(generic_url):
        st.error("Please enter valid website url.")
    else:
        try:
            with st.spinner("Waiting..."):
                # loading the website or YT video data
                if "youtube.com" in generic_url:
                    loader = YoutubeLoader.from_youtube_url(
                        generic_url,
                        add_video_info=True,
                        language=["en"],
                        translation="en" 
                    )
                else:
                    loader = UnstructuredURLLoader(
                        urls=[generic_url],
                        ssl_verify=False,
                        headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
                    )
                    
                docs=loader.load()

                # Loading llm chat model - groq
                llm = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=groq_api_key)

                # Chain for summarization
                chain=load_summarize_chain(
                    llm=llm,
                    chain_type="stuff",
                    prompt=prompt
                )
                output_summary = chain.run(docs)
                st.success(output_summary)

        except Exception as e:
            st.exception(f"Exception:{e}")
            

