from anki_vn_util.anki.id_entity import IdEntity
from anki_vn_util.anki.model import Model
from anki_vn_util.anki.note import Note
from typing import List, Protocol
import requests


class TransferLayer(Protocol):
    def add(self, note: Note) -> None:
        pass

    def decks(self) -> List[IdEntity]:
        pass

    def models(self) -> List[Model]:
        pass

    def model_field_names(self, model_name) -> List[str]:
        pass


class HttpTransferLayer:
    _url = ""

    def __init__(self, url: str) -> None:
        super().__init__()
        self._url = url

    def add(self, note: Note):
        params = {
            "note": {
                "deckName": note.deck_name,
                "modelName": note.model_name,
                "fields": note.fields,
                "options": {
                    "allowDuplicate": False,
                    "duplicateScope": "deck",
                    "duplicateScopeOptions": {
                        "deckName": note.deck_name,
                        "checkChildren": False
                    }
                },
                "tags": [
                    "anki-vn-util"
                ]
            }
        }
        self._do_action("addNote", params)

    def decks(self) -> List[IdEntity]:
        result = self._do_action("deckNamesAndIds")
        return [IdEntity(id=result[key], name=key) for key in result.keys()]

    def models(self) -> List[Model]:
        result = self._do_action("modelNamesAndIds")
        return [IdEntity(id=result[key], name=key) for key in result.keys()]

    def model_field_names(self, model_name) -> List[str]:
        return self._do_action("modelFieldNames", {
            "modelName": model_name
        })

    def _do_action(self, action, params=None):
        payload = {
            "action": action,
            "version": 6
        }
        if not params is None:
            payload["params"] = params

        resp = requests.post(self._url, json=payload).json()
        return resp['result']
