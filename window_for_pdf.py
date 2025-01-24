import tkinter as tk
from tkinter import filedialog
from generate_pdf import merge_pdf


def select_file1():
    file1_entry.delete(0, tk.END)
    filepath = filedialog.askopenfilename()
    if filepath:
        file1_entry.insert(0, filepath)

def select_file2():
    file2_entry.delete(0, tk.END)
    filepath = filedialog.askopenfilename()
    if filepath:
        file2_entry.insert(0, filepath)

def merge_pdfs():
    file1 = file1_entry.get()
    file2 = file2_entry.get()
    file_to_gen = file_to_generate_entry.get()

    result = merge_pdf(file1, file2, file_to_gen)
    if result == "success":
        label_feedback.config(text=f"PDF generated successfully: {file_to_gen}", fg="green")
    else:
        label_feedback.config(text=result, fg="red")


root = tk.Tk()
root.title("PDF Merger")
root.geometry("650x400")
root.configure(bg="#f4f4f9")

label_instruction = tk.Label(
    root,
    text="Merge 2 PDF in 1",
    font=("Helvetica", 16, "bold"),
    bg="#f4f4f9",
    fg="#333",
)
label_instruction.pack(pady=20)

file1_label = tk.Label(root, text="File 1:")
file1_label.pack()
file1_entry = tk.Entry(root, width=35)
file1_entry.pack(padx=10)
file1_button = tk.Button(root, text="Browse...", command=select_file1)
file1_button.pack()

file2_label = tk.Label(root, text="File 2:")
file2_label.pack()
file2_entry = tk.Entry(root, width=35)
file2_entry.pack(padx=10)
file2_button = tk.Button(root, text="Browse...", command=select_file2)
file2_button.pack()

file_to_generate = tk.Label(root, text="Name of PDF to Generate:")
file_to_generate.pack()
file_to_generate_entry = tk.Entry(root, width=35)
file_to_generate_entry.pack(padx=10)

merge_button = tk.Button(root, text="Merge PDF", command=merge_pdfs)
merge_button.pack(pady=20)

label_feedback = tk.Label(root, text="", bg="#f4f4f9", fg="#333")
label_feedback.pack(pady=10, padx=10)

root.mainloop()
