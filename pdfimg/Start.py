from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import re
def convert(fname):
    pages=None
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    print text 

    # write to .txt
    text_file = open("/Users/Nehsus/Desktop/blazeIT/Final/Chennai_output.txt", "w")
    text = re.sub("\s\s+", " ", text)
    text_file.write("%s" % text)
    text_file.close()

convert("/Users/Nehsus/Desktop/blazeIT/pdfimg/chennai.ocr.pdf")