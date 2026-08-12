import streamlit as st
import os
from auth import register, login
from upload import save_document, get_documents
from gemini_ocr import extract_text_from_scanned_pdf
from document_processor import split_text
from vector_store import create_vector_store
from rag import ask_question
from sql_agent import get_tables, execute_sql
from dashboard import show_dashboard
from report_generator import generate_report
from dashboard import show_dashboard
import pandas as pd
import sqlite3
from sql_agent import get_tables, execute_sql
from logger import log_error

# ==========================================
# MODULE 9
# ==========================================

from evaluation import evaluate_answer
from logger import log_question, log_answer, log_error


# ==========================================
# SESSION STATE
# ==========================================

if "chunks" not in st.session_state:
    st.session_state.chunks = []

if "vector_index" not in st.session_state:
    st.session_state.vector_index = None

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI Enterprise Assistant",
    page_icon="🤖",
    layout="wide"
)


# ==========================================
# TITLE
# ==========================================

st.title(
    "🤖 AI-Powered Enterprise Assistant"
)

st.write(
    "Enterprise Document, RAG and Data Intelligence Platform"
)


# ==========================================
# SIDEBAR MENU
# ==========================================

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Home",
        "Register",
        "Login",
        "Upload Documents",
        "OCR",
        "Document Chunks",
        "RAG Question Answering",
        "SQL Agent",
        "Dashboard",
        "AI Report",
        "Evaluation",
        "API Information"
    ]
)


# ============================================================
# HOME
# ============================================================

if menu == "Home":

    st.header(
        "Welcome to AI Enterprise Assistant"
    )

    st.write("""
    This platform provides intelligent enterprise
    document and data processing capabilities.
    """)

    st.subheader("Features")

    st.write("""
    ✅ User Authentication

    ✅ Document Upload

    ✅ Gemini OCR

    ✅ Document Chunking

    ✅ Vector Search using FAISS

    ✅ RAG Question Answering

    ✅ SQL Database Query Agent

    ✅ Enterprise Dashboard

    ✅ AI Report Generation

    ✅ AI Response Evaluation

    ✅ Monitoring and Logging

    ✅ REST API
    """)


# ============================================================
# MODULE 1 / 2
# USER REGISTRATION
# ============================================================

elif menu == "Register":

    st.header(
        "👤 User Registration"
    )

    username = st.text_input(
        "Username"
    )

    email = st.text_input(
        "Email"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Register"):

        if not username or not email or not password:

            st.warning(
                "Please fill all fields."
            )

        else:

            try:

                result = register(
                    username,
                    email,
                    password
                )

                if result:

                    st.success(
                        "Registration Successful!"
                    )

                else:

                    st.error(
                        "User already exists."
                    )

            except Exception as e:

                st.error(
                    f"Registration Error: {e}"
                )


# ============================================================
# LOGIN
# ============================================================

elif menu == "Login":

    st.header(
        "🔐 User Login"
    )

    username = st.text_input(
        "Username"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if not username or not password:

            st.warning(
                "Please enter username and password."
            )

        else:

            try:

                result = login(
                    username,
                    password
                )

                if result:

                    st.session_state.logged_in = True

                    st.success(
                        "Login Successful!"
                    )

                else:

                    st.error(
                        "Invalid Credentials"
                    )

            except Exception as e:

                st.error(
                    f"Login Error: {e}"
                )


# ============================================================
# MODULE 3
# DOCUMENT UPLOAD
# ============================================================

elif menu == "Upload Documents":

    st.header(
        "📁 Document Management"
    )

    uploaded = st.file_uploader(
        "Choose a document",
        type=[
            "pdf",
            "txt",
            "docx"
        ]
    )

    if uploaded:

        try:

            path = save_document(
                uploaded
            )

            st.success(
                "File Uploaded Successfully!"
            )

            st.write(
                "Saved at:",
                path
            )

        except Exception as e:

            st.error(
                f"Upload Error: {e}"
            )


    st.subheader(
        "Uploaded Documents"
    )

    try:

        documents = get_documents()

        if documents:

            for document in documents:

                st.write(
                    f"📄 {document.filename}"
                )

        else:

            st.info(
                "No documents uploaded yet."
            )

    except Exception as e:

        st.error(
            f"Document Error: {e}"
        )


# ============================================================
# MODULE 4
# GEMINI OCR
# ============================================================

elif menu == "OCR":

    st.header(
        "📄 Gemini AI OCR"
    )

    uploaded_pdf = st.file_uploader(
        "Upload a scanned PDF",
        type=["pdf"]
    )

    if uploaded_pdf:

        os.makedirs(
            "uploads",
            exist_ok=True
        )

        pdf_path = os.path.join(
            "uploads",
            uploaded_pdf.name
        )

        with open(
            pdf_path,
            "wb"
        ) as file:

            file.write(
                uploaded_pdf.getbuffer()
            )

        st.success(
            "PDF uploaded successfully!"
        )


        if st.button(
            "Extract Text Using Gemini"
        ):

            try:

                with st.spinner(
                    "Gemini is reading the scanned PDF..."
                ):

                    extracted_text = (
                        extract_text_from_scanned_pdf(
                            pdf_path
                        )
                    )


                st.success(
                    "OCR completed successfully!"
                )


                st.subheader(
                    "Extracted Text"
                )

                st.text_area(
                    "Text",
                    extracted_text,
                    height=400
                )


                # ==========================================
                # MODULE 5
                # DOCUMENT CHUNKING
                # ==========================================

                chunks = split_text(
                    extracted_text
                )

                st.session_state.chunks = chunks


                st.success(
                    f"Created {len(chunks)} document chunks."
                )


                # ==========================================
                # MODULE 6
                # VECTOR STORE
                # ==========================================

                with st.spinner(
                    "Creating vector store..."
                ):

                    index = create_vector_store(
                        chunks
                    )

                st.session_state.vector_index = index

                st.success(
                    "FAISS vector store created successfully!"
                )


                # Save extracted text

                text_filename = (
                    os.path.splitext(
                        uploaded_pdf.name
                    )[0]
                    + ".txt"
                )

                text_path = os.path.join(
                    "uploads",
                    text_filename
                )

                with open(
                    text_path,
                    "w",
                    encoding="utf-8"
                ) as file:

                    file.write(
                        extracted_text
                    )


                st.success(
                    f"Text saved as {text_filename}"
                )


            except Exception as e:

                log_error(
                    str(e)
                )

                st.error(
                    f"OCR Error: {e}"
                )


# ============================================================
# MODULE 5
# DOCUMENT CHUNKS
# ============================================================

elif menu == "Document Chunks":

    st.header(
        "📚 Document Chunks"
    )

    chunks = st.session_state.chunks


    if not chunks:

        st.warning(
            "No document chunks available."
        )

        st.info(
            "Upload and process a document using OCR first."
        )

    else:

        st.write(
            f"Total Chunks: {len(chunks)}"
        )

        for i, chunk in enumerate(chunks):

            with st.expander(
                f"Chunk {i + 1}"
            ):

                st.write(
                    chunk
                )


# ============================================================
# MODULE 7
# RAG QUESTION ANSWERING
# ============================================================

elif menu == "RAG Question Answering":

    st.header(
        "🤖 RAG Question Answering"
    )


    if not st.session_state.chunks:

        st.warning(
            "No documents are available."
        )

        st.info(
            "Upload and process a document first."
        )


    elif st.session_state.vector_index is None:

        st.warning(
            "Vector store is not available."
        )


    else:

        question = st.text_input(
            "Ask a question about your document"
        )


        if st.button(
            "Ask AI"
        ):

            if not question.strip():

                st.warning(
                    "Please enter a question."
                )

            else:

                try:

                    log_question(
                        question
                    )


                    with st.spinner(
                        "Searching documents and generating answer..."
                    ):

                        answer, sources = ask_question(
                            question,
                            st.session_state.chunks,
                            st.session_state.vector_index
                        )


                    st.subheader(
                        "💡 AI Answer"
                    )

                    st.write(
                        answer
                    )


                    log_answer(
                        answer
                    )


                    st.subheader(
                        "📚 Retrieved Sources"
                    )


                    for i, source in enumerate(
                        sources
                    ):

                        with st.expander(
                            f"Source {i + 1}"
                        ):

                            st.write(
                                source
                            )


                except Exception as e:

                    log_error(
                        str(e)
                    )

                    st.error(
                        f"RAG Error: {e}"
                    )


# ============================================================
# MODULE 8A
# SQL DATABASE QUERY AGENT
# ============================================================

elif menu == "SQL Agent":

    st.header(
        "🗄️ SQL Database Query Agent"
    )


    try:

        tables = get_tables()


        st.subheader(
            "Available Database Tables"
        )

        st.write(
            tables
        )


        query = st.text_area(
            "Enter SQL Query",
            value="SELECT * FROM employees;"
        )


        if st.button(
            "Execute SQL"
        ):

            if not query.strip():

                st.warning(
                    "Please enter a SQL query."
                )

            else:

                try:

                    log_question(
                        query
                    )


                    result = execute_sql(
                        query
                    )


                    st.subheader(
                        "📊 Query Result"
                    )


                    st.dataframe(
                        result,
                        use_container_width=True
                    )


                except Exception as e:

                    log_error(
                        str(e)
                    )

                    st.error(
                        f"SQL Error: {e}"
                    )


    except Exception as e:

        st.error(
            f"Database Error: {e}"
        )


# ============================================================
# MODULE 8B
# DASHBOARD
# ============================================================

elif menu == "Dashboard":

    st.header(
        "📊 Enterprise Dashboard"
    )


    try:

        tables = get_tables()


        if not tables:

            st.warning(
                "No database tables found."
            )


        else:

            selected_table = st.selectbox(
                "Select Table",
                tables
            )


            query = f"""
            SELECT *
            FROM {selected_table}
            """


            data = execute_sql(
                query
            )


            show_dashboard(
                data
            )


    except Exception as e:

        log_error(
            str(e)
        )

        st.error(
            f"Dashboard Error: {e}"
        )


# ============================================================
# MODULE 8C
# AI REPORT GENERATION
# ============================================================

elif menu == "AI Report":

    st.header(
        "📄 AI Enterprise Report"
    )


    report_data = st.text_area(
        "Enter data or analysis",
        height=300
    )


    if st.button(
        "Generate Report"
    ):

        if not report_data.strip():

            st.warning(
                "Please enter data first."
            )

        else:

            try:

                with st.spinner(
                    "Generating AI report..."
                ):

                    report = generate_report(
                        report_data
                    )


                st.subheader(
                    "📋 Generated Report"
                )

                st.write(
                    report
                )


                log_answer(
                    report
                )


            except Exception as e:

                log_error(
                    str(e)
                )

                st.error(
                    f"Report Error: {e}"
                )


# ============================================================
# MODULE 9A
# AI RESPONSE EVALUATION
# ============================================================

elif menu == "Evaluation":

    st.header(
        "🧪 AI Response Evaluation"
    )


    context = st.text_area(
        "Document Context",
        height=200
    )


    answer = st.text_area(
        "AI Answer",
        height=200
    )


    if st.button(
        "Evaluate Answer"
    ):

        if (
            not context.strip()
            or not answer.strip()
        ):

            st.warning(
                "Enter both context and answer."
            )


        else:

            try:

                result = evaluate_answer(
                    answer,
                    context
                )


                st.subheader(
                    "Evaluation Result"
                )


                st.metric(
                    "Score",
                    f"{result['score']}%"
                )


                st.write(
                    "Status:",
                    result["status"]
                )


            except Exception as e:

                log_error(
                    str(e)
                )

                st.error(
                    f"Evaluation Error: {e}"
                )


# ============================================================
# MODULE 9B
# REST API INFORMATION
# ============================================================

elif menu == "API Information":

    st.header(
        "🔌 REST API"
    )


    st.write(
        "AI Enterprise Assistant REST API"
    )


    st.subheader(
        "Available Endpoints"
    )


    st.code(
        """
GET  /
GET  /health
GET  /documents
POST /ask
POST /sql
"""
    )


    st.subheader(
        "Start API"
    )


    st.code(
        "uvicorn api:app --reload"
    )


    st.info(
        "The REST API runs separately from Streamlit."
    )