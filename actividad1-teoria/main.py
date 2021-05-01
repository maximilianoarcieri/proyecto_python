import PySimpleGUI as sg
import analyze as an



games_categories = ['ALL','ACTION','ADVENTURE','ARCADE','BOARD','CARD','CASINO','CASUAL','EDUCATIONAL','MUSIC','PUZZLE','RACING','ROLE PLAYING','SIMULATION','SPORTS','STRATEGY','TRIVIA','WORD']

def create_layout():

    layout = [[sg.Text('Datos disponibles \npara analizar', font = '_ 20', relief = sg.RELIEF_RIDGE, justification = 'center', background_color = '#6E402A')],
            [sg.Text('', background_color = '#D89156')],
            [sg.Button('Canciones de Spotify', size = (16,1), button_color = '#6E402A'), sg.Input('ALL', size = (12,1), key = 'artist')],
            [sg.Button('Juegos de Play Store', size = (16,1), button_color = '#6E402A'), sg.Combo(games_categories, size = (12,1), key = 'game_option')],
            [sg.Button('Salir', size = (6,1), button_color = '#6E402A')]]
    return sg.Window('Actividad 1 x Python Plus - TEORIA', layout, background_color = '#D89156', margins = (75,50), finalize = True)



def main():
    window = create_layout()
    
    while True:    
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == 'Salir':
            break

        elif event == 'Canciones de Spotify':
            if values.get('artist') != '':
                an.music_analysis(values.get('artist'))
            else:
                sg.PopupQuick('Ingrese un valor válido', background_color = '#D89156', button_color = '#6E402A')

        elif event == 'Juegos de Play Store':
            if values.get('game_option') in games_categories:
                an.game_analysis(values.get('game_option'))
            else:
                sg.PopupQuick('Ingrese un valor válido', background_color = '#D89156', button_color = '#6E402A')

    window.close()




if __name__ == "__main__":
    main()