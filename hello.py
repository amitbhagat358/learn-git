import PyPDF2
from itertools import product
import string

def crack_pdf_password(pdf_path):
    # Characters for the letter part of the password
    letters = string.ascii_lowercase

    # Generate all possible passwords with specific digit ranges
    for letter_combination in product(letters, repeat=4):
        for day in range(1, 32):  # Days from 01 to 31
            for month in range(1, 13):  # Months from 01 to 12
                day_str = f"{day:02d}"  # Format day as two digits
                month_str = f"{month:02d}"  # Format month as two digits
                password = ''.join(letter_combination) + day_str + month_str
                print(f"Trying password: {password}")

                try:
                    # Open the PDF file
                    with open(pdf_path, 'rb') as file:
                        pdf_reader = PyPDF2.PdfReader(file)
                        # Try to decrypt the PDF with the current password
                        if pdf_reader.decrypt(password):
                            print(f"Password found: {password}")
                            return password
                except PyPDF2.utils.PdfReadError:
                    continue

    print("Password not found.")
    return None

# Use raw string for the file path
pdf_path = r"C:\Users\amitb\Downloads\Account_Statement.pdf"
crack_pdf_password(pdf_path)
