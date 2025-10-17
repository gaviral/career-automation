import os
from pypdf import PdfReader, PdfWriter

def change_pdf_metadata(file_path, new_title, new_subject):
    """
    Changes the Title and Subject metadata of a PDF file.

    Args:
        file_path (str): The path to the input PDF file.
        new_title (str): The new title for the PDF metadata.
        new_subject (str): The new subject for the PDF metadata.
    """
    try:
        # Create a PDF reader object
        reader = PdfReader(file_path)
        
        # Create a PDF writer object
        writer = PdfWriter()

        # Copy all pages from the reader to the writer
        for page in reader.pages:
            writer.add_page(page)

        # Update the metadata
        writer.add_metadata({
            "/Title": new_title,
            "/Subject": new_subject
        })
        
        # Create a new filename for the updated PDF
        directory, original_filename = os.path.split(file_path)
        filename_root, extension = os.path.splitext(original_filename)
        output_filename = os.path.join(directory, f"{filename_root}_updated{extension}")

        # Write the updated content to a new file
        with open(output_filename, "wb") as f:
            writer.write(f)
            
        print(f"Successfully updated metadata!")
        print(f"New file saved as: {output_filename}")

    except Exception as e:
        print(f"An error occurred: {e}")

# --- Configuration ---
# Replace with the actual path to your resume file
input_pdf = "Aviral_Garg_Resume_Agentic_Al.pdf" 
new_title_value = "Aviral Garg - Resume - AI Engineer"
new_subject_value = "Aviral Garg - Resume"

# --- Run the script ---
change_pdf_metadata(input_pdf, new_title_value, new_subject_value)