#! python

# pdf module PyPDF
import PyPDF2

def reading():
       #counting number of pages in pdf
       pageNum=readingPdf.numPages
       print "Total Number of Pages:", pageNum
       print("\n")
       for i in range(pageNum):
              # GetPage method sent only one page
              page=readingPdf.getPage(i)
              # Extracting text from page variable
              print(page.extractText())
#Reading pdf 
readingPdf=PyPDF2.PdfFileReader(open('abc.pdf' , 'rb'))
# If gievn pdf have password 
if readingPdf.isEncrypted==True:
# Preventing the exception raise if no input is given     
              def password():
                     a=raw_input()
                     b=readingPdf.decrypt(a)
                     if b==1:
                            reading()
                            print('\n\n\nDONE Reading...')
                     else:
                            print"Type correct Password"
                            password()
              password()
# If PDF dosen't have password
if readingPdf.isEncrypted == False:
      reading()
      print('\n\n\nDONE Reading...')
       
       
       
