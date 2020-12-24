import pyperclip


def read_clipboard() -> str:
    return pyperclip.paste()
