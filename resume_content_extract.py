import pymupdf
import re
import easyocr
import api

# COMMENT: data[(resume_data,([number],[email])),]

def reformat_data(ai, regex):
    name = ai.name
    lname = ai.lname
    introduce = ai.introduce
    skill = ai.additional_skill
    phone = regex[0][0]
    email = ai.email
    return name, lname, introduce, skill, phone, email

# regex is not useful if its condition is too complexed which lead to slow heavy long process
def personal_data_extract(content):
    phone = re.findall(r'0\d{2}-?\d{3}-?\d{4}', content)
    email = re.findall(r'[\w\.-]+@[\w\.-]+', content) # unused due to mistake in ocr in some image, this regex not detected the whole email
    return phone, email

def data_extract(resume_files):
    data = []
    photo_extension = ('.jpg', '.jpeg', '.png')
    for resume in resume_files:
        if resume.endswith(photo_extension):
            data.append(image_extraction(resume))
        else:
            data.append(pdf_extraction(resume))
    return data

def image_extraction(file):
    doc = easyocr.Reader(['en','th'])
    image_data = doc.readtext(file, detail = 0)
    text = ' '.join(image_data)
    ai_extract = api.send_to_ai(text)
    return reformat_data(ai_extract, personal_data_extract(text))

def pdf_extraction(file):
    doc = pymupdf.open(file)
    page = doc[0]
    text = page.get_text()
    ai_extract = api.send_to_ai(text)
    return reformat_data(ai_extract, personal_data_extract(text))
