from abc import ABC
from pathlib import Path
from models.quote_model import QuoteModel
from typing import List


class IngestorInterface(ABC):
    """Interface for Ingestor.

    Args:
        ABC (_type_): _description_
    """

    allow_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check extensions file can ingest

        Args:
            path (str): File path

        Returns:
            bool: true if can ingest else false
        """

        file_extension = Path(path).suffix
        return file_extension in cls.allow_extensions

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse file

        Args:
            path (str): File path

        Returns:
            List[QuoteModel]: List of quotes
        """

        pass
