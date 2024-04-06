from .ingestor_interface import IngestorInterface
from models.quote_model import QuoteModel


class TextIngestor(IngestorInterface):
    """Text Ingestor.

    Args:
        IngestorInterface (_type_): Parent class
    """

    file_type = ".txt"

    @classmethod
    def parse(cls, path):
        """Text Ingestor.

        Args:
            path (str): File path

        Returns:
            list: List of quotes from text file
        """

        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
        return [QuoteModel(*quote.strip().split(" - ")) for quote in lines]
