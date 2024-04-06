from .ingestor_interface import IngestorInterface
from .text_ingestor import TextIngestor
import subprocess
import os


class PDFIngestor(IngestorInterface):
    """PDF Ingestor.

    Args:
        IngestorInterface (_type_): Parent class
    """

    file_type = ".pdf"

    @classmethod
    def parse(cls, path):
        """Parse PDF file

        Args:
            path (str): File path

        Returns:
            list: List of quotes from pdf file
        """

        tmp_text_file = "./tmp_pdf_to_text.txt"
        call = subprocess.call(['pdftotext', '-layout', path, tmp_text_file])
        quotes = TextIngestor.parse(tmp_text_file)
        os.remove(tmp_text_file)
        return quotes
