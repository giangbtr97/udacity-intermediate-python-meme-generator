class QuoteModel:
    """Quote Model."""

    def __init__(self, body, author):
        """Init quote model.

        Args:
            body (str): content of qoute
            author (str): author of qoute
        """

        self.body = body
        self.author = author

    def __repr__(self) -> str:
        """Return

        Returns:
            str: "{self.body} - {self.author}"
        """

        return f"{self.body} - {self.author}"
