from .ingestor_interface import IngestorInterface
from models.quote_model import QuoteModel
import pandas


class CSVIngestor(IngestorInterface):
    """CSV Ingestor.

    Args:
        IngestorInterface (_type_): Parent class
    """

    file_type = ".csv"

    @classmethod
    def parse(cls, path):
        """Parse CSV file

        Args:
            path (str): File path

        Returns:
            list: List of quotes from csv file
        """

        csv = pandas.read_csv(path, header=0)
        return [QuoteModel(**row) for i, row in csv.iterrows()]
