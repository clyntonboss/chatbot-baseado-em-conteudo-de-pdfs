# 🤖 Chatbot Inteligente com PDFs

Este projeto foi desenvolvido como parte do desafio da DIO para criação de um chatbot que responde com base no conteúdo de arquivos PDF utilizando **IA generativa**, **embeddings** e **busca vetorial**. Ele é ideal para quem precisa explorar grandes volumes de informação, como estudantes, pesquisadores e profissionais.

## 💡 Visão Geral

Imagine que você está escrevendo um TCC e precisa revisar diversos artigos científicos. Com este sistema, basta carregar os PDFs e perguntar o que quiser — o chatbot responderá com base no conteúdo dos arquivos.

## 🚀 Funcionalidades

- Upload de múltiplos PDFs
- Geração de embeddings com OpenAI
- Busca vetorial usando FAISS
- Geração de respostas contextuais via LLM
- Interface interativa com Streamlit
- Campo seguro para inserir a OpenAI API Key

## 📂 Estrutura do Projeto

```
chatbot_pdf/
├── app.py              # Código principal da aplicação
├── .gitignore          # Arquivos ignorados no versionamento
├── README.md           # Este arquivo
└── inputs/             # Diretório para colocar seus arquivos .txt e PDFs
```

## 🧪 Como Executar

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/chatbot_pdf.git
cd chatbot_pdf
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute a aplicação:
```bash
streamlit run app.py
```

4. Insira sua **OpenAI API Key** no menu lateral da interface.

## 📸 Prints da Aplicação

![Upload de Arquivos](https://via.placeholder.com/800x400.png?text=Upload+de+PDFs)
![Chat em Ação](https://via.placeholder.com/800x400.png?text=Perguntas+e+Respostas)

## 🧠 Insights

- IA generativa é poderosa para transformar documentos em interfaces conversacionais.
- Embeddings e buscas vetoriais permitem navegar no conhecimento de forma inteligente.
- O uso de `.env` ou campos protegidos é essencial para segurança de APIs.

## ✨ Possibilidades Futuras

- Suporte a outros formatos como DOCX e TXT
- Análise semântica para resumos automáticos
- Histórico de conversas e anotações personalizadas

---

Desenvolvido com carinho durante o desafio da DIO.
