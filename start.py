import keyboard, os

pressed = 1
def print_pressed_keys(e):
    global pressed
    if e.name == "f6": #change button
        if pressed == 1:
            pressed = pressed + 1
            print(
                'Отключаем соединение'
                )
            os.system("wmic path win32_networkadapter where index=11 call disable")
        if e.event_type == 'up':
            pressed = 1
            print(
                'Включаем соединение'
                )
            os.system("wmic path win32_networkadapter where index=11 call enable")


keyboard.hook(print_pressed_keys)
keyboard.wait()
