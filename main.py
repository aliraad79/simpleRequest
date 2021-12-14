import PySimpleGUI as sg

sg.theme("DarkAmber")  # Add a touch of color
# All the stuff inside your window.
layout = [
    [sg.Text("Headers")],
    [sg.Text("Add header"), sg.B("+", key="-Add-")],
    [
        sg.Frame(
            "Headers",
            [
                [sg.Text("Key"), sg.Input(key="-KEY-0-"), sg.Text("Value"), sg.Input(key="-VALUE-0-")],
            ],
            key="-Header-",
        )
    ],
    [sg.Button("Send Request")],
]

window = sg.Window("Simple Request", layout)

i = 1
headers = {}

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Cancel":
        break
    elif event == "-Add-":
        window.extend_layout(
            window["-Header-"],
            [
                [
                    sg.Text("Key"),
                    sg.Input(key=f"-KEY-{i}-"),
                    sg.Text("Value"),
                    sg.Input(key=f"-VALUE-{i}-"),
                ]
            ],
        )
        i += 1

    print("You entered ", event, values)

    for key, value in values.items():
        headers[key] = value
        ...

window.close()
