# Importing necessary libraries
import tkinter as tk
import re



def generate_etaoin():

    '''The funciton checks the input is empty or not and
    generates a etaoin bar graph.'''

    etaoin_dict = dict()
    user_input = text_box.get("1.0", "end-1c")

    # Remove new line or endline if present
    user_input = user_input.strip()

    # Convert the input to lowercase.
    user_input = user_input.lower()

    # Remove punctuations from the input.
    user_input = user_input.replace("(", "")
    user_input = user_input.replace(")", "")
    user_input = user_input.replace(",", "")
    user_input = user_input.replace(".", "")
    user_input = user_input.replace("?", "")
    user_input = user_input.replace("’", "")
    user_input = user_input.replace("\'", "")
    user_input = user_input.replace("\"", "")
    user_input = user_input.replace(":", "")
    user_input = user_input.replace(";", "")
    user_input = user_input.replace(" ", "")
    user_input = user_input.replace("/", "")
    user_input = user_input.replace("-", "")
    user_input = user_input.replace("=", "")
    user_input = user_input.replace("\\", "")

    # User input validation
    if user_input == "":
        display_text.config(text="Plesae enter a valid sentence.")
    elif bool(re.search('[0-9]', user_input)) == True:
        display_text.config(text = "Please spell out the number(s) in the sentence.")
    elif bool(re.search('[\`\~\!\@\#\$\_\%\^\&\*\{\}\[\]\<\>\|]', user_input)):
        display_text.config(text = "Please do not include special characters like '`~!@#$%^&*{}[]<>|', in the sentence.")
    else:
        for char in user_input:
            try:
                etaoin_dict[char].append(char)
            except Exception as e:
                etaoin_dict[char] = [char]

        out_text="Poor Man’s Bar Chart\n"

        for key, values in sorted(etaoin_dict.items()):
            out_text = f"{out_text}{key}:{values}\n"

        display_text.config(text=out_text)

    return None


# Creating a Tkinter GUI window
frame = tk.Tk()
frame.title("Etaoin (eh-tay-oh-in)")

# Setting window size
WIDTH = 1280
HEIGHT = 720

# Screen size
SCREEN_WIDTH = frame.winfo_screenwidth()
SCREEN_HEIGHT = frame.winfo_screenheight()

# Determining the center of the window
center_x = int(SCREEN_WIDTH/2 - WIDTH/2)
center_y = int(SCREEN_HEIGHT/2 - HEIGHT/2)

# Setting the frame center
frame.geometry(f'{WIDTH}x{HEIGHT}+{center_x}+{center_y}')

# Entereance message
message = tk.Label(frame, text="Enter a sentence to find the etaoin")
message.pack()

# Include a text-box for user input.
text_box = tk.Text(frame, height=10, width=90)
text_box.pack()

# This is a button that implements the function "generate_etaoin()"
goButton = tk.Button(frame, text="Generate", command=generate_etaoin)
goButton.place(x=550, y=200)

# Quits the GUI
quitButton = tk.Button(frame, text="Quit", command=frame.destroy)
quitButton.place(x=650, y=200)

# Display any error message or the silly persona if all inputs are valid
display_text = tk.Label(frame, text="", justify=tk.LEFT)
display_text.place(x=300, y= 350)

# Start GUI
frame.mainloop()
