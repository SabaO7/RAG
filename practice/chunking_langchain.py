import fitz  # PyMuPDF
import re
from langchain.text_splitter import RecursiveCharacterTextSplitter

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
    # Adjust the pattern if the footer varies in format
    footer_pattern = re.compile(r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}\s+Page\s+\d+\s+of\s+\d+', re.IGNORECASE)
    # Remove the footer from the document
    cleaned_text = re.sub(footer_pattern, '', text)
    return cleaned_text.strip()  # Trim any leading or trailing whitespace

# Define the function to split the document into chunks
def split_document(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,  # Adjust the chunk size as needed
        chunk_overlap=20,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.split_text(text)

# Use the function to read and extract text from the PDF
document_text = extract_text_from_pdf('test_file_1.pdf')

# Clean the document
cleaned_document = clean_document(document_text)

# Now we split the cleaned document into chunks based on your requirements
split_texts = split_document(cleaned_document)

# Find the index for "Legal References:" and the year pattern "20\d\d"
legal_references_index = cleaned_document.find("Legal References:")
year_match = re.search("20\d\d", cleaned_document)

# If both patterns are found, we can extract the chunks
if legal_references_index != -1 and year_match:
    chunk1 = cleaned_document[:legal_references_index].strip()
    chunk2 = cleaned_document[legal_references_index:year_match.end()].strip()
    chunk3 = cleaned_document[year_match.end():].strip()
else:
    chunk1 = cleaned_document  # Assign the whole cleaned document to chunk1 if patterns not found
    chunk2 = ""
    chunk3 = ""

# Print the chunks with space between them
print("Chunk 1:\n\n", chunk1)
print("\n\nChunk 2:\n\n", chunk2)
print("\n\nChunk 3:\n\n", chunk3)
