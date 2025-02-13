import camelot
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

# Debugging: Print Camelot version
print(f"Camelot version: {camelot.__version__}")

# Function to extract tables from PDF and save to Excel
def extract_and_save(pdf_path, excel_path):
    try:
        # Debugging: Print PDF path
        print(f"Extracting tables from PDF: {pdf_path}")

        # Extract tables from PDF using Camelot
        tables = camelot.read_pdf(pdf_path, pages="all", flavor="stream")

        # Debugging: Print number of tables found
        print(f"Found {len(tables)} tables.")

        # Check if any tables were found
        if not tables:
            messagebox.showerror("Error", "No tables found in the PDF.")
            return

        # Combine all tables into a single DataFrame
        df = pd.concat([table.df for table in tables], ignore_index=True)

        # Automatically detect the header
        # Assume the first row is the header
        header = df.iloc[0].tolist()  # Extract the first row as the header
        df = df[1:]  # Remove the first row from the data
        df.columns = header  # Assign the header to the DataFrame

        # Save the DataFrame to an Excel file
        print(f"Saving to Excel: {excel_path}")
        df.to_excel(excel_path, index=False)
        messagebox.showinfo("Success", f"Excel file saved to {excel_path}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Application
class PDFToExcelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF to Excel Converter")
        self.root.geometry("500x300")

        # PDF File Input
        self.pdf_label = tk.Label(root, text="Select PDF File:")
        self.pdf_label.pack(pady=10)
        self.pdf_entry = tk.Entry(root, width=50)
        self.pdf_entry.pack(pady=5)
        self.pdf_button = tk.Button(root, text="Browse", command=self.browse_pdf)
        self.pdf_button.pack(pady=5)

        # Excel File Output
        self.excel_label = tk.Label(root, text="Save Excel File As:")
        self.excel_label.pack(pady=10)
        self.excel_entry = tk.Entry(root, width=50)
        self.excel_entry.pack(pady=5)
        self.excel_button = tk.Button(root, text="Browse", command=self.browse_excel)
        self.excel_button.pack(pady=5)

        # Convert Button
        self.convert_button = tk.Button(root, text="Convert to Excel", command=self.convert)
        self.convert_button.pack(pady=20)

    def browse_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        self.pdf_entry.delete(0, tk.END)
        self.pdf_entry.insert(0, file_path)

    def browse_excel(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
        self.excel_entry.delete(0, tk.END)
        self.excel_entry.insert(0, file_path)

    def convert(self):
        pdf_path = self.pdf_entry.get()
        excel_path = self.excel_entry.get()

        if not pdf_path or not excel_path:
            messagebox.showerror("Error", "Please provide both PDF and Excel file paths.")
            return

        extract_and_save(pdf_path, excel_path)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = PDFToExcelApp(root)
    root.mainloop()