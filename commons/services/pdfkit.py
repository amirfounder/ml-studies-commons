import pdfkit


DEFAULT_EXE_LOCATION = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

class PdfKit:
    def __init__(self, path: str = DEFAULT_EXE_LOCATION):
        self.configs = pdfkit.configuration(wkhtmltopdf=path)
        self.pdfkit = pdfkit

    def from_file(self, path, *args, **kwargs):
        return self.pdfkit.from_file(path, configuration=self.configs, *args, **kwargs)
