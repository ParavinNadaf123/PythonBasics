from fpdf import FPDF
from fpdf.enums import XPos, YPos

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 14)
        self.cell(0, 10, "Python Data Structures Cheat Sheet", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")

    def chapter_title(self, title):
        self.set_font("Helvetica", "B", 12)
        self.cell(0, 10, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L")
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("Helvetica", "", 10)
        self.multi_cell(0, 8, body)
        self.ln()

pdf = PDF()
pdf.add_page()

# 📘 LIST Section
pdf.chapter_title("LIST")
pdf.chapter_body("""
- Ordered, mutable, allows duplicates.
- Methods: append(), extend(), insert(), remove(), pop(), clear(), index(), count(), sort(), reverse(), copy()

Example:
my_list = [1, 2, 3]
my_list.append(4)       # [1, 2, 3, 4]
my_list.extend([5, 6])  # [1, 2, 3, 4, 5, 6]
""")

# 📗 SET Section
pdf.chapter_title("SET")
pdf.chapter_body("""
- Unordered, mutable, no duplicates.
- Methods: add(), update(), remove(), discard(), pop(), clear(), union(), intersection(), difference(), symmetric_difference()

Example:
my_set = {1, 2, 3}
my_set.add(4)
my_set.update([5, 6])
""")

# 📙 DICT Section
pdf.chapter_title("DICTIONARY")
pdf.chapter_body("""
- Key-value pairs, unordered (ordered since Python 3.7), mutable, keys must be unique.
- Methods: get(), keys(), values(), items(), pop(), popitem(), update(), clear()

Example:
my_dict = {'a': 1, 'b': 2}
my_dict['c'] = 3
my_dict.update({'d': 4})
""")

# 🧪 PRACTICE PROBLEMS
pdf.chapter_title("PRACTICE PROBLEMS")
pdf.chapter_body("""
1. Create a list of numbers and write a function to return only the even numbers.
2. Write a function that counts how many times each item appears in a list.
3. Remove all duplicates from a list using a set.
4. Given a dictionary, print keys that have even values.
5. Create a dictionary that maps each word in a sentence to its length.
""")

# Save PDF
pdf.output("Python_Data_Structures_Cheat_Sheet.pdf")
print("PDF saved as: Python_Data_Structures_Cheat_Sheet.pdf")
