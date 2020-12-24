from typing import List
from .anki import make_client, Note, Client, IdEntity
from .host import listen, read_clipboard

template = {
    'text': 'Front',
    'img': '',
    'audio': ''
}


def fill_note_from_template(note: Note, text: str = None, audio: str = None, img: str = None):
    if text:
        field = template['text']
        note.fields[field] = text


def select_entity(label, entities: List[IdEntity]):
    print(label)
    for i, entity in enumerate(entities):
        print('[%i] %s' % (i + 1, entity.name))

    entity = None
    while entity is None:
        try:
            answer = int(input())
            entity = entities[answer - 1]
        except KeyError:
            pass
        except ValueError:
            pass
    return entity


def select_deck(client: Client) -> IdEntity:
    return select_entity('Select a deck', client.get_decks())


def select_model(client: Client) -> IdEntity:
    return select_entity('Select a model', client.get_models())


def build_template(client: Client, model_name: str):
    fields = client.get_model_names(model_name)
    entities = [IdEntity(name=e, id=e) for e in fields]
    field = select_entity('Select the text field', entities)
    template["text"] = field.id


def add_note(client: Client, note: Note):
    fill_note_from_template(note, text=read_clipboard())
    client.add_note(note)
    note.fields = {}


if __name__ == "__main__":
    note = Note()
    client = make_client("http://localhost:8765")
    print('Anki visual novel util')
    print()
    deck = select_deck(client)
    print('Selected deck: "%s"' % (deck.name,))
    print()
    note.deck_name = deck.name

    model = select_model(client)
    print('Selected model: "%s"' % (model.name,))
    note.model_name = model.name

    build_template(client, model.name)
    listen(add_note)
    while True:
        command = input().lower()
        if command == '`':
            add_note(client, note)
