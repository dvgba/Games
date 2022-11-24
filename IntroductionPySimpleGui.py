# -- Importing the Library
import PySimpleGUI as sg
# -- Elements & Layout ----
# -- The layout will be a List of lists
layout = [
    [sg.Text('Text', enable_events = True, key = '-TEXT-'),sg.Spin(['item 1', 'item 2'])],      # -- Top Row with a list of selection box
    [sg.Button('Button', key = '-BUTTON1-')],                           # -- Second Row
    [sg.Input(key = '-INPUT-')],                                                       # -- Third Row
    [sg.Text('Test'), sg.Button('Button', key = '-BUTTON2-')]           # -- Fouth Row
]

window = sg.Window('Coverter', layout)

# -- Events -----
# -- An event is triggered by a certain action, closing the window triggers the sg.WIN_CLOSED event
# -- with PySymple every element can trigger an event
# -- a good exemple is a button click triggers another event
# -- The name of that event will be the name, or rather the key, of that button
# -- for exemple here our button is called 'button' and that would be the key and the event name
# -- most common way to name a key is the name in upperCase letters and follow and preceded by dash

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-BUTTON1-':
        window['-TEXT-'].update(values['-INPUT-'])
        # -- window['-TEXT-'].update(visible = False)

    if event == '-BUTTON2-':
        print('Something Else')

    if event == '-TEXT-':
        print('text was pressed')

window.close()

# -- Values  -----
# -- Essentially in PySympleGui, ther a several elements that can contain values, like inputs
# -- These values are stored in one dictionary, called values
# -- You can access that one with the nake of the input element
# -- If an input element does not havea key it getsa number assigned

# -- Update Elements ----
# -- Every element has an update method
# -- It can be used to change text, visibility etc
