from docx import Document

document = Document()
Name = input('what is your name?' )
phone_number = input('what is your telephone number?' )
email = input('what is your email?' )
document.add_paragraph(
    name + ' | ' + phone_number + ' | ' + email)




Document.save('cv.docx')