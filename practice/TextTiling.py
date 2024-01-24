import fitz  # PyMuPDF
import re
import nltk
nltk.download('stopwords')

# Function to extract text from PDF using PyMuPDF
def extract_text_from_pdf(pdf_path):
    with fitz.open(pdf_path) as pdf:
        text = ""
        for page in pdf:
            text += page.get_text()
    return text

# Define the function to clean the document
def clean_document(text):
    # Regular expression pattern to match the footer (Month Year and Page # of #)
    footer_pattern = re.compile(r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}\s+Page\s+\d+\s+of\s+\d+', re.IGNORECASE)
    # Remove the footer from the document
    cleaned_text = re.sub(footer_pattern, '', text)
    return cleaned_text.strip()  # Trim any leading or trailing whitespace

# Use the function to read and extract text from the PDF
document_text = extract_text_from_pdf('test_file_2.pdf')

# Clean the document
cleaned_document = clean_document(document_text)

# Manually locate the "Legal References:" section and the year pattern
legal_references_start = cleaned_document.find("Legal References:")
year_pattern_match = re.search(r"20\d\d", cleaned_document)

# Initialize indices for splitting
indices = [0, legal_references_start, year_pattern_match.end() if year_pattern_match else None]

# Extract the chunks based on the located indices
chunk1 = cleaned_document[:indices[1]].strip() if indices[1] else ""
chunk2 = cleaned_document[indices[1]:indices[2]].strip() if indices[1] and indices[2] else ""
chunk3 = cleaned_document[indices[2]:].strip() if indices[2] else ""

# Print the chunks with space between them
print("Chunk 1:\n\n", chunk1)
print("\n\nChunk 2:\n\n", chunk2)
print("\n\nChunk 3:\n\n", chunk3)
