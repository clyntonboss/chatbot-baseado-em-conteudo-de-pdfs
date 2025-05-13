import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import os
import tempfile

st.set_page_config(page_title='Chatbot com PDFs', layout='wide')
st.title('🤖 Chatbot Inteligente com PDFs')
st.markdown('Faça perguntas e receba respostas com base nos documentos carregados.')

# Campo seguro para a chave da OpenAI
st.sidebar.title("Configurações")
api_key = st.sidebar.text_input("Insira sua OpenAI API Key:", type="password")
if api_key:
    os.environ['OPENAI_API_KEY'] = api_key

# Upload de múltiplos PDFs
uploaded_files = st.file_uploader("Carregue seus arquivos PDF", type='pdf', accept_multiple_files=True)

if uploaded_files and api_key:
    with st.spinner("Processando arquivos..."):
        docs = []
        for file in uploaded_files:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(file.read())
                loader = PyPDFLoader(tmp_file.name)
                docs.extend(loader.load())

        embeddings = OpenAIEmbeddings()
        db = FAISS.from_documents(docs, embeddings)
        chain = load_qa_chain(OpenAI(temperature=0), chain_type='stuff')

    st.success("Arquivos processados com sucesso!")

    # Campo para pergunta
    question = st.text_input("Digite sua pergunta sobre os PDFs:")

    if question:
        with st.spinner("Buscando resposta..."):
            results = db.similarity_search(question)
            answer = chain.run(input_documents=results, question=question)
            st.markdown("### Resposta:")
            st.success(answer)
elif not api_key and uploaded_files:
    st.warning("Insira sua chave da OpenAI na barra lateral para continuar.")
