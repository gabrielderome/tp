import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

#for each file in the folder("C:\Users\Gabriel\Downloads\info_notes"), print the name of the file and the text extracted from it
import os

folder_path = "C:\\Users\\Gabriel\\Downloads\\info_notes\\"
all_files = os.listdir(folder_path)
print(f"All files in directory: {all_files}")

print(extract_text_from_pdf(folder_path + "Cours_110124.pdf"))

