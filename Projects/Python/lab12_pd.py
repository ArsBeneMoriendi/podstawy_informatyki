import random
import PySimpleGUI as psg

psg.theme("DarkBlack")
font = ("Lucida Console", 13)

layout = [[psg.Text("     ____       _       __  __      _____ ", text_color='red', font=font), ],
          [psg.Text(" U  / ___| UU  / \\  UU |  \\/  | UU | ____| U ", text_color='yellow', font=font), ],
          [psg.Text("  \\| |  _ /  \\/ _ \\/  \\| |\\/| |/  \\|  _|  / ", text_color='lime', font=font), ],
          [psg.Text("   | |_| |   / ___ \\   | |  | |    | |___ ", text_color='cyan', font=font), ],
          [psg.Text("    \\____|  /_/   \\_\\  |_|  |_|    |_____| ", text_color='blue', font=font), ],
          [psg.Text("    _||||_   \\\\   //   _||  ||_   _//   \\\\_ ", text_color='violet', font=font), ],
          [psg.Text("   (__)(__) (__) (__) (__)  (__) (__)   (__) ", text_color='white', font=font), ],
          [psg.Text(" \nGuess the number drawn from 1 to 100:", text_color='white', font=("Times New Roman", 20)), ],
          [psg.Text(" \nEnter your guess here and press enter:", text_color='white', font=("Times New Roman", 14)), ],
          [psg.InputText(key="key", do_not_clear=False)],
          [psg.Text("")]]

window = psg.Window("Game", layout, finalize=True)
window["key"].bind("<Return>", "_Enter")

random_num = random.randrange(1, 100)

def checking():
    try:
        while True:
            event, values = window.read()
            input_num = int(values["key"])
            if input_num != random_num:
                if input_num < random_num:
                    psg.popup_auto_close(f"The clue number is higher than the entered one. Keep guessing.",
                                         text_color='red', title="Higher")
                elif input_num > random_num:
                    psg.popup_auto_close(f"The clue number is lower than the entered one. Keep guessing.",
                                         text_color='red', title="Lower")
            elif input_num == random_num:
                psg.popup_no_buttons(f"Congratulations! The clue number was {random_num}.\nYou've guessed it!",
                                     text_color='lime', title="Number guessed")
            else:
                break
    except ValueError:
        psg.popup_auto_close(f"You need to enter an integer number", text_color='white')
        checking()


checking()

window.close()
