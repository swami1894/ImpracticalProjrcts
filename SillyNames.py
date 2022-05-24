# Necessary libraries
import tkinter as tk
import random

# tuple of silly first names
first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'BeenieWeenie'",
"Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
'Chewy', 'Chigger", "Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"',
'Mergatroid', '"Mr Peabody"', 'OilCan', 'Oinks', 'Old Scratch',
'Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug',
'Pushmeet','Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
"Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
"Winston 'Jazz Hands'", 'Worms')

# tuple of silly last names
last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
'Hootkins', 'Jefferson', 'Jenkins', 'JingleySchmidt',
'Johnson', 'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
'Stevens', 'Stroganoff', 'SugarGold','Swackhamer', 'Tippins','Turnipseed',
 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax','Weiners', 'Whipkey',
 'Wigglesworth', 'Wimplesnatch', 'Winterkorn', 'Woolysocks')


def generate_persona():

    ''' A simple function that takes user name
    and generates a silly name for the user'''

    name = text_box.get("1.0", "end-1c")   # Accepts the user name

    # User name validation
    if name.strip() == "":
        displaytext.config(text="Please enter a valid name!")
    else:
        persona_first = random.choice(first)
        persona_last = random.choice(last)
        displaytext.config(text="'{} {}' is your silly persona {}!".format(persona_first, persona_last, name))
    return None

WIDTH = 500
HEIGHT = 125

# Creating a tkinter Window
root = tk.Tk()
root.title("Silly Name Generator")

# Getting the size of the screen
SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()

# Determining the center of the window
center_x = int(SCREEN_WIDTH/2 - WIDTH/2)
center_y = int(SCREEN_HEIGHT/2 - HEIGHT/2)

# Setting window size
root.geometry(f'{WIDTH}x{HEIGHT}+{center_x}+{center_y}')

# Opening message
message = tk.Label(root, text="Find your Silly Persona")
message.pack()              # Helps adding the message to the window

# Getting the user name
message1 = tk.Label(root, text="Enter your name to know your Silly Persona")
message1.pack()

# Creates a text box to accept the user name
text_box = tk.Text(root, height=1, width=45)
text_box.pack()

# This is a button that implements the function "generate_persona()"
goButton = tk.Button(root, text="Find", command=generate_persona)
goButton.place(x=195, y=60)

# Quits the GUI
quitButton = tk.Button(root, text="Quit", command=root.destroy)
quitButton.place(x=245, y=60)

# Display any error message or the silly persona if all inputs are valid
displaytext = tk.Label(root, text="")
displaytext.pack(side=tk.BOTTOM)

# Start GUI
root.mainloop()
