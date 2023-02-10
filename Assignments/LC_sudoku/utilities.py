import pygame
import PySimpleGUI as sg

def set_time(sec):
    seconds = sec % 60
    minutes = sec // 60
    current_time = str(minutes) + ":" + (str(seconds) if seconds > 9 else "0" + str(seconds))
    return current_time

def get_key(key):
    switcher = {
        pygame.K_1: 1,
        pygame.K_2: 2,
        pygame.K_3: 3,
        pygame.K_4: 4,
        pygame.K_5: 5,
        pygame.K_6: 6,
        pygame.K_7: 7,
        pygame.K_8: 8,
        pygame.K_9: 9,
    }
    return switcher.get(key, None)

def display_messageBox(body, title):
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Some text on Row 1')],
                [sg.Text('Enter something on Row 2'), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        print('You entered ', values[0])

    window.close()

if __name__=='__main__':
    
    display_messageBox("hello world",'title')
