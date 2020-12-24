from pynput import keyboard


def listen(on_press):
    def on_press(key):
        try:
            if key == keyboard.KeyCode.f12:
                on_press()
        except AttributeError:
            print('special key {0} pressed'.format(
                key))

    # Collect events until released
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
