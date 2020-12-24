from anki_vn_util.anki.id_entity import IdEntity
from anki_vn_util.anki.model import Model
from typing import List
from anki_vn_util.anki.note import Note
from .transfer_layer import HttpTransferLayer, TransferLayer


def make_client(url: str):
    transport = HttpTransferLayer(url)
    return Client(transport)


class Client:
    _transport_layer: TransferLayer = None

    def __init__(self, transport_layer: TransferLayer) -> None:
        super().__init__()
        self._transport_layer = transport_layer

    def add_note(self, note: Note):
        self._transport_layer.add(note)

    def get_decks(self) -> List[IdEntity]:
        decks = self._transport_layer.decks()
        return decks
    
    def get_models(self) -> List[Model]:
        models = self._transport_layer.models()
        return models
    
    def get_model_names(self, model_name: str) -> List[str]:
        fields = self._transport_layer.model_field_names(model_name)
        return fields
