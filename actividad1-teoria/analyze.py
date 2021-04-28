import PySimpleGUI as sg
import json
import csv



def isSpecial(c):
    '''Se comprueba si el caracter es especial'''

    return c in ["'",'[',']',"\""]



def music_analysis(name):
    '''Se analizan las 20 canciones más populares del artista indicado'''

    try:
        with open("./tracks.csv", "r", encoding = "utf-8") as tracks:
            csv_reader = csv.reader(tracks,delimiter = ',')
            cabecera = next(csv_reader)

            artist_songs = list(filter(lambda song: name in song[5], csv_reader))
            artist_songs = sorted(artist_songs, key = lambda song: int(song[2]), reverse = True)

            data = {}
            data['Canciones'] = []
             
            for i in range(20): #si el artista tiene menos de 20 canciones se guardan las que haya
                try:
                    try:
                        artist = ''.join(c for c in artist_songs[i][5] if (not isSpecial(c)))
                        data['Canciones'].append({
                            'Artistas' : f'{artist}',
                            'Cancion' : f'{artist_songs[i][1]}',
                            'Puntaje' : f'{artist_songs[i][2]}',
                        })
                    except UnicodeEncodeError:
                        sg.PopupQuick("Algunos datos no pudieron guardarse", auto_close = False, background_color = '#D89156', button_color = '#6E402A', text_color = 'black')
                except IndexError:
                    sg.PopupQuick("El artista tenía menos de 20 canciones", auto_close = False, background_color = '#D89156', button_color = '#6E402A', text_color = 'black')
                    break
            if len(data['Canciones']) != 0:
                artist = ''.join(c for c in name if c != ' ').lower()
                with open(f"./{artist}_songs.json", "w", encoding = "utf-8") as file:
                    json.dump(data, file, indent = 4)
                sg.PopupQuick(f"""Se generó el archivo con las 20 canciones de "{name}" más populares!""", auto_close = False, background_color = '#D89156', button_color = '#6E402A', text_color = 'black')
            else:
                sg.PopupQuick(f"""No se encontraron canciones de "{name}".""", auto_close = False, background_color = '#D89156', button_color = '#6E402A', text_color = 'black')                
    except FileNotFoundError:
        sg.PopupQuick("No se encontró la ruta del archivo.", background_color = '#D89156', button_color = '#6E402A', text_color = 'black')



def game_analysis(category):
    '''Se analizan los 20 juegos mejor valorados de la categoria indicada'''

    try:
        with open("./android-games.csv", "r", encoding = "utf-8") as games:
            csv_reader = csv.reader(games, delimiter = ',')
            cabecera = next(csv_reader)
            
            games_category = list(filter(lambda game: category in game[8] ,csv_reader))

            data = {}
            data[f'{category} GAMES'] = []

            for i in range(20): #el dataset está ordenado por puntajes, los primeros 20 son los mejores valorados de cada categoria
                try:
                    data[f'{category} GAMES'].append({
                        'Titulo' : f'{games_category[i][1]}',
                        'Puntaje' : f'{games_category[i][2]}'
                    })
                except UnicodeEncodeError:
                    sg.PopupQuick("Algunos datos no pudieron guardarse", auto_close = False, background_color = '#D89156', button_color = '#6E402A', text_color = 'black')
            
            with open(f"./{category.lower()}_games.json", "w", encoding = "utf-8") as file:
                json.dump(data, file, indent = 4)
            sg.PopupQuick(f"""Se generó el archivo con los 20 juegos "{category.capitalize()}" más descargados!""", auto_close = False, background_color = '#D89156', button_color = '#6E402A', text_color = 'black')
    except FileNotFoundError:
        sg.PopupQuick("No se encontró la ruta del archivo.", background_color = '#D89156', button_color = '#6E402A', text_color = 'black')




if __name__ == '__main__':
    music_analysis(input('Ingresar artista: '))
    game_analysis(input('Ingresar categoria: '))
