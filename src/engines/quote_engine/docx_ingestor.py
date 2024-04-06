from .ingestor_interface import IngestorInterface
from models.quote_model import QuoteModel
from docx import Document


class DocxIngestor(IngestorInterface):
    """Docx Ingestor.

    Args:
        IngestorInterface (_type_): Parent class
    """

    file_type = ".docx"

    @classmethod
    def parse(cls, path):
        """Parse DOCX file

        Args:
            path (str): File path

        Returns:
            list: List of quotes from docx file
        """

        document = Document(path)
        contents = []
        for paragraph in document.paragraphs:
            if paragraph.text:
                contents.append(QuoteModel(*paragraph.text.replace('"', '').split(" - ")))
        return contents
