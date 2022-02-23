from docx import Document
from docx.shared import Inches 

doc = Document()

doc.add_picture(
    "musharraf.png",
    width=Inches(2.0)

)

name = input("What is your name : ")
phone = input("What is your phone no. ")
email = input("What is your email : ")

doc.add_paragraph(name + " | " + phone + " | " + email)

doc.save("my-cv.docx")
