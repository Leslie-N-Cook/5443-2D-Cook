import pygame
from PIL import Image, ImageDraw, ImageFont
'''
functions in utilities :

    def get_key() :
        switch case function
        creates dictionary of 1-9 values from the keyboard input

     def set_time() : 
        takes in seconds converts to minutes
        returns the current time in (min):(sec) format

    def background_music() :
        plays the background music during game
        pygame.mixer.music.play(-1) tells the music play to contiuously play
        
    def win_sound() : 
        plays a congratulatory sound when game is complete
        pygame.mixer.music.play(0) tells the music to only play once
        
    ## from Griffin ##
    
    def get_font_size() :
    
    def makePopUp() : 
      
'''
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

def set_time(sec):
    seconds = sec % 60
    minutes = sec // 60
    current_time = str(minutes) + ":" + (str(seconds) if seconds > 9 else "0" + str(seconds))
    return current_time

def background_music():
    #load the music from my files
    pygame.mixer.music.load('music/lofi_falling.mp3')
    #set the volume so it doesnt blast anyones ear drums
    pygame.mixer.music.set_volume(.05)
    # tell it to play continuously
    pygame.mixer.music.play(-1)

def win_sound():
    #load the music from my files
    pygame.mixer.music.load('music/congratulations-post-malone.mp3')
    #set the volume so it doesnt blast anyones ear drums
    pygame.mixer.music.set_volume(0.4)
    # tell it to play once
    pygame.mixer.music.play(0)


def get_font_size(text, font_name, pixel_size):
    """This returns the "font size" necessary to fit a letter in an image
    of a given pixel size. Different letters have different widths and
    heights.
    Params:
        text (str) : string to test
        font_name (str) : font to open
        pixel_size (int) : height of image
    Returns:
        font_size (int), font width (int) , font_height (int)
    """
    font_size = 20
    h = 0
    while h < pixel_size:
        font = ImageFont.truetype(font_name, font_size)
        w, h = font.getbbox(text)
        font_size += 2
    return font_size, w, h

def makePopUp(content,**kwargs):

    width = kwargs.get("width", 300)
    height = kwargs.get("height", 300)
    fill_color = kwargs.get("fill_color", "white")
    border_size = kwargs.get("border_size", 5)
    border_color = kwargs.get("border_color", "black")
    border_radius = kwargs.get("border_radius", 7)
    font_size = kwargs.get("font_size", 20)
    font_name = kwargs.get("font_name", "fonts/Futura.ttf")
    image = Image.new("RGBA", (width,height))  # A 0-1

    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle(
        (0, 0, width, height),
        fill=fill_color,
        outline=border_color,
        width=border_size,
        radius=border_radius,
    )
    # # use the tile width and font width to center the letter. Same with the height.
    # # the 1.30 is to shift the letter up a little bit. Not sure what will happen with a different font
    i = 0
    y = border_size
    totFontHeight = 0
    for line in content:
        # if not 'font_size' in line:
        #     line['font_size'] = font_size
        # print(font_size)
        if not 'align' in line:
            align="center"
        
        if not line['align']:
            line['align'] = "left"

        if not 'font_name' in line:
            line['font_name'] = font_name

        #font_size, font_width, font_height = get_font_size(line['text'], line['font_name'], line['font_size'])
        font = ImageFont.truetype(line['font_name'], size=line['font_size'])
        
        if not 'color' in line:
            color = "black"
        else:
            color = line['color']     
        
        x = border_size
        
        if line['align'] == 'center':
            x = ((width // 2) - (line['font_size'] // 2))
            #x = width // 2
        elif line['align'] == 'right':
            x = border_size + width - line['font_size']
        draw.text((x,y),line['text'],font=font,fill=color,align='left')
        y += line['font_size'] + line['font_size'] // 2 + 5
        i += 1

    return image
    
    
## TEST POP UP BY RUNNING python3 utilities.py##
if __name__=='__main__':
    content = [
        {"text":" ",'font_size':20,'align':'left','color':'white'},
        {"text":" ",'font_size':20,'align':'center','color':'white'},
        {"text":" SUDOKU SOLVED! ",'font_size':60,'align':'left','color':'red'},
        {"text":"  ",'font_size':20,'align':'center','color':'white'},
        {"text":"   You Finished in: 15:32   ",'font_size':20,'align':'left','color':'red'},
       
    ]
    image = makePopUp(content,border_size=20,border_color='white',fill_color='black',width=600,height=275)
    image.show()
    image.save(f"popup.png")


