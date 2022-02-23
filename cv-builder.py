from docx import Document

document = Document()

name = input("What is your name : ")
phone = input("What is your phone no. ")
email = input("What is your email : ")

document.add_paragraph(name + " | " + phone + " | " + email)

document.save("my-cv.docx")
