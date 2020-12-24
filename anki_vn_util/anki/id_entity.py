class IdEntity:
    name: str
    id: int

    def __init__(self, id: int, name: str) -> None:
        super().__init__()
        self.id = id
        self.name = name