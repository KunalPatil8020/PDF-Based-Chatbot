# PDF-Based Chatbot
This project implements a chatbot that answers user queries based on the content of a PDF document. The chatbot uses semantic search techniques to find relevant answers and provides a fallback response if no relevant match is found.

## Overview
- Extracts and processes text from PDF files.
- Answers user queries by retrieving the most relevant content from the document.
- Provides a fallback response for queries that cannot be matched.
- Includes a text-based interface for user interaction.
- Modular design for easy customization and expansion.

## Requirements
- Python 3.8 or higher

## Getting Started
1. Clone the repository:
    ```bash
    https://github.com/KunalPatil8020/PDF-Based-Chatbot.git
    ```
2. ```bash
    pip install -r requirements.txt
    ```
3. Update the file path in chatbot.py:
    ```bash
    chatbot = PDFChatbot("input.pdf")
    ```
4. Run the chatbot application:
    ```bash
    python3 app.py
    ```

    Ask your questions directly in the terminal. For example:

    ```bash
    You: What are the eligibility criteria for the Bachelor in Business Administration program?
    Bot: Eligibility Criteria for the program is given below:
        • Bachelor in Business Administration:
            • HSC (10+2) in any discipline from a recognized Board with minimum 50%, or,
            • HSC (10+2) in any discipline from a recognized Board with 45% and minimum 2 years work experience, or,
            • SSC (10) + 3 years Diploma recognized by AICTE with 60%.
    ```
