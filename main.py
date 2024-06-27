import fitz  # PyMuPDF
from reportlab.lib.pagesizes import A0
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()  # Hide the main tkinter window

# Open file dialog for selecting the input PDF
input_pdf_path = filedialog.askopenfilename(
    title="Select input PDF file", filetypes=[("PDF files", "*.pdf")]
)

# Open file dialog for selecting the output PDF location
output_pdf_path = filedialog.asksaveasfilename(
    title="Save output PDF as",
    defaultextension=".pdf",
    filetypes=[("PDF files", "*.pdf")],
)

# Open the input PDF
input_pdf = fitz.open(input_pdf_path)

# Create a new PDF for the output
output_pdf = fitz.open()

# Parameters for A2 size (seems to be a mistake in the comment, corrected here)
a4_width, a4_height = A0

for page_num in range(len(input_pdf)):
    page = input_pdf[page_num]
    rect = page.rect

    y_offset = 0
    while y_offset < rect.height:
        # Create a new blank page with A4 size
        new_page = output_pdf.new_page(width=a4_width, height=a4_height)

        # Define the visible area of the long page to copy
        visible_area = fitz.Rect(
            0, y_offset, rect.width, min(y_offset + a4_height, rect.height)
        )

        # Copy the visible area from the long page to the new A4 page
        # Copy the visible area from the long page to the new A4 page
        new_page.show_pdf_page(new_page.rect, input_pdf, page_num, clip=visible_area)

        # Increment y_offset by the height of an A4 page
        y_offset += a4_height


output_pdf.save(output_pdf_path)
