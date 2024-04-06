from .ingestor_interface import IngestorInterface
from .csv_ingestor import CSVIngestor
from .docx_ingestor import DocxIngestor
from .pdf_ingestor import PDFIngestor
from .text_ingestor import TextIngestor
from pathlib import Path


class Ingestor(IngestorInterface):
    """Ingestor.

    Args:
        IngestorInterface (_type_): Parent class
    """

    allow_extensions = [".csv", ".docx", ".pdf", ".txt"]

    @classmethod
    def parse(cls, path: str):
        """Parse file by path

        Args:
            path (str): File path

        Returns:
            list: List of quotes
        """

        if not cls.can_ingest(path):
            raise ValueError("Unsupported file extension:")

        try:
            file_extension = Path(path).suffix

            if file_extension == CSVIngestor.file_type:
                return CSVIngestor.parse(path)
            if file_extension == DocxIngestor.file_type:
                return DocxIngestor.parse(path)
            if file_extension == PDFIngestor.file_type:
                return PDFIngestor.parse(path)
            if file_extension == TextIngestor.file_type:
                return TextIngestor.parse(path)
        except Exception as error:
            raise Exception(f"Error parsing file '{path}': {error}")
