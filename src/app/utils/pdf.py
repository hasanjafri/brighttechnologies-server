import io
import os
import json
 
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
 
def extract_text_by_page(pdf_path):
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, 
                                      caching=True,
                                      check_extractable=True):
            resource_manager = PDFResourceManager()
            fake_file_handle = io.StringIO()
            converter = TextConverter(resource_manager, fake_file_handle)
            page_interpreter = PDFPageInterpreter(resource_manager, converter)
            page_interpreter.process_page(page)
 
            text = fake_file_handle.getvalue()
            yield text
 
            # close open handles
            converter.close()
            fake_file_handle.close()
 
def extract_text(pdf_path):
    for page in extract_text_by_page(pdf_path):
        print(page)
        print()

def export_as_json(pdf_path, json_path):
    filename = os.path.splitext(os.path.basename(pdf_path))[0]
    data = {'Filename': filename}
    data['Pages'] = []
 
    counter = 1
    for page in extract_text_by_page(pdf_path):
        text = page
        page = {'Page_{}'.format(counter): text}
        data['Pages'].append(page)
        counter += 1
 
    with open(json_path, 'w') as fh:
        json.dump(data, fh)
 
if __name__ == '__main__':
    pdf_path = './job.pdf'
    json_path = './job.json'
    export_as_json(pdf_path, json_path)
    #print(extract_text('./job.pdf'))
    #with open("Output.txt", "w") as text_file:
        #text_file.write(extract_text('./job.pdf'))