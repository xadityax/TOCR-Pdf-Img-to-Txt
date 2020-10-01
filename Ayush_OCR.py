#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pytesseract


# In[3]:


pip install fpdf


# In[2]:


try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


# In[12]:


try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
import os
from fpdf import FPDF 

pdf = FPDF()    
pdf.add_page() 
pdf.set_font("Arial", size = 15) 

global address
address = input("Plese enter folder address \n")
while True: 
    if address=='9' :
        exit()
    elif os.path.isdir(address):
        break
    else :
        address = input("Enter correct address(if want to quit press 9) \n")

def iterate_over_all_images():
    x=address  
    for img in os.listdir(x):
        doc_text = pytesseract.image_to_string(Image.open(x+'/'+img))
        print(doc_text)
        f = open("{myfile}.txt".format(myfile=img), "w")
        f.write(doc_text)

iterate_over_all_images()
print("done")


# In[ ]:


from fpdf import FPDF 
pdf = FPDF()    
pdf.add_page() 
pdf.set_font("Arial", size = 15) 
f = open("myfile.txt", "r") 
for x in f: 
    pdf.cell(200, 10, txt = x, ln = 1, align = 'C') 

pdf.output("mygfg.pdf") 


# In[ ]:


from wand.image import Image as wi
pdf = wi(filename="cs1.pdf", resolution=300)
pdfimage = pdf.convert("jpeg")
i=1
for img in pdfimage.sequence:
    page = wi(image=img)
    page.save(filename=str(i)+".jpg")
    i +=1

