
def pdf_to_docx(pdf_file):
    from pdf2docx import Converter

    docx_file = pdf_file.replace("pdf", "docx")
    cv = Converter(pdf_file)

    cv.convert(docx_file, start=0, end=None)
    cv.close()


def docx_to_pdf(docx_file):
    from docx2pdf import convert
    pdf_file = docx_file.replace('.docx', '.pdf')
    convert(docx_file, pdf_file)
    return pdf_file

