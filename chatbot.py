import pdfplumber
from sentence_transformers import SentenceTransformer
import faiss

class PDFChatbot:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.text_chunks = []
        self.embeddings = None
        self.index = None
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self._prepare()

    def _extract_text_from_pdf(self):
        """Extract text from the PDF using pdfplumber."""
        text = ""
        with pdfplumber.open(self.pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        # print(text)
        return text

    def _split_into_chunks(self, text, chunk_size=500):
        """Split the text into smaller chunks."""
        return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    def _prepare(self):
        """Prepare the chatbot by indexing the PDF content."""
        pdf_text = self._extract_text_from_pdf()
        self.text_chunks = self._split_into_chunks(pdf_text)
        embeddings = self.model.encode(self.text_chunks)
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(embeddings)
        self.embeddings = embeddings

    def ask(self, query):
        """Search for the query in the PDF and dynamically adjust the threshold."""
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(query_embedding, k=1)
        distance = distances[0][0]
        matched_chunk = self.text_chunks[indices[0][0]]
        
        print(f"Query: {query}")
        print(f"Distance: {distance} | Matched Chunk: {matched_chunk}")

        if distance < 0.8:  
            response = " ".join(matched_chunk.split())  
            return response

        # Fallback response
        return "Sorry, I didn’t understand your question. Do you want to connect with a live agent?"