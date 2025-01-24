import os
from PyPDF2 import PdfWriter, PdfReader

def merge_pdf(file1, file2, file_to_generate):

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    if not file_to_generate.lower().endswith(".pdf"):
        file_to_generate = file_to_generate+".pdf"
    file_to_generate = os.path.join(desktop_path, file_to_generate)

    # create generated file
    content = PdfWriter()

    try:
        # open existing files
        with open(file1, "rb") as file1, open(file2, "rb") as file2:
            file1_reader = PdfReader(file1)
            file2_reader = PdfReader(file2)

            # add existing pdf into new generated pdf
            if file1_reader.pages:
                content.add_page(file1_reader.pages[0])

            for i in range(len(file2_reader.pages)):
                content.add_page(file2_reader.pages[i])

            # open the new pdf file and write the content inside
            with open(file_to_generate, "wb") as gen_file:
                content.write(gen_file)
        return "success"
    except FileNotFoundError as e:
        return e
    except Exception as e:
        return e
