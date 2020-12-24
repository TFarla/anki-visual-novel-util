class Note:
    deck_name: str
    model_name: str
    fields = {}
    tags = ["anki_vn_util"]

    def __init__(self, deck_name="", model_name="", fields={}, tags=[]) -> None:
        super().__init__()
        self.deck_name = deck_name
        self.model_name = model_name
        self.fields = fields
        self.tags = tags