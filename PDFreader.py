import sys
import PyPDF2
import re
import os

def check_if_PDF(file_list):

    pattern = r'*.pdf'

    r = re.compile('.*pdf')
    onlyPDF_list = list(filter(r.match, file_list))  # Read Note below
    print(onlyPDF_list)
    return onlyPDF_list



def package_num_finder(pdfFile):

    dir = 'D:\\Python\PDFInPOSTreader\pdfy\{}'.format(pdfFile)

    try:
        f = open(dir, 'rb')
    except OSError:
        print("Could not open/read file:", dir)
        sys.exit()

    pdf_reader = PyPDF2.PdfFileReader(f)
    #no_pages = pdf_reader.numPages
    # print(no_pages)
    page_one = pdf_reader.getPage(0)
    page_text = page_one.extractText()
    text = page_text
    # print(text)
    no_package_patter = r'\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d'
    package_num = re.search(no_package_patter, text)
    # print(package_no.group())
    final_num = package_num.group()
    f.close()
    return final_num





pdf_list = os.listdir('D:\\Python\PDFInPOSTreader\pdfy')
print(pdf_list)
only_pdf_list = check_if_PDF(pdf_list)
all_packages = []

for i in only_pdf_list:
    pack_no = package_num_finder(i)
    all_packages.append(pack_no)

print('InPost package numbers: ' + str(all_packages))



