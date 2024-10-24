import PyPDF2
import nltk
import pandas as pd

nltk.download('punkt')

def read_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def tokenize_text(text):
    tokens = nltk.word_tokenize(text)
    return [word.lower() for word in tokens if word.isalpha()]  # Filter out punctuation

def match_values(extracted_tokens, reference_list):
    matches = set(extracted_tokens) & set(reference_list)
    return matches

def calculate_match_percentage(matches, total_tokens):
    if total_tokens == 0:
        return 0
    return (len(matches) / total_tokens) * 100

def generate_report(match_percentage):
    print(f"Match Percentage: {match_percentage:.2f}%")

def main(pdf_file_path, reference_list):
    # Step 1: Read PDF
    extracted_text = read_pdf(pdf_file_path)
    
    # Step 2: Process extracted content
    extracted_tokens = tokenize_text(extracted_text)
    
    # Step 3: Match values
    matches = match_values(extracted_tokens, reference_list)
    
    # Step 4: Calculate match percentage
    match_percentage = calculate_match_percentage(matches, len(extracted_tokens))
    
    # Step 5: Produce output
    generate_report(match_percentage)
    
    # Optionally, save to CSV
    df = pd.DataFrame({'Matches': list(matches)})
    df.to_csv('match_report.csv', index=False)

# Example usage
if __name__ == "__main__":
    pdf_file_path = "sample.pdf"  # Replace with your PDF file path
    reference_list = ["example", "sample", "test", "word"]  # Replace with your reference words
    main(pdf_file_path, reference_list)