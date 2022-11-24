import PySimpleGUI as sg

layout = [
    [
        sg.Input(key = '-INPUT-'),
        sg.Spin(['Kilometer to Mile', 'Kilos to pound', 'second to minutos'], key = '-UNITS-'),
        sg.Button('Converter', key = '-CONVERT-')
     ],
    [sg.Text('Output', key = '-OUTPUT-')]
]

window = sg.Window('Coverter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
                match values['-UNITS-']:
                    case 'Kilometer to Mile':
                            output = round(float(input_value) * 0.6214,2)
                            output_string = f'{input_value} km are {output} miles'
                    case 'Kilos to pound':
                            output = round(float(input_value) * 2.20462,2)
                            output_string = f'{input_value} kg are {output} pounds.'
                    case 'second to minutos':
                            output = round(float(input_value) / 60,2)
                            output_string = f'{input_value} seconds area {output} minutes'

                window['-OUTPUT-'].update(output_string)
        else:
                window['-OUTPUT-'].update('Please enter a number')

window.close()
