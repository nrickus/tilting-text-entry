#
# Tilting Text Entry on the BBC mirco:bit by Neil Rickus @computingchamps
#
# Program uses the BBC micro:bit's accelerometer to allow the entry of text, which can subsequently scroll across the screen
# View the program in action here - https://www.youtube.com/watch?v=_B7N6C-dkW8
#
# Tilt the micro:bit right to move up through the alphabet, or left to move down through the alphabet
# Spaces for separating letters / words can be found at the start and the end of the alphabet
#
# Press button A when the letter (or space) you want to enter is displayed. A happy face will acknowledge the button press
#
# On your final letter, hold (not press) button A to add the letter, then press button B to finish entering text
# A heart will acknowledge the button press and your text will scroll across the display continuously
#
# Possible enhancements:
# - Tilting the device further left or right increases the speed the letters are displayed
# - Button B can be used to add spaces, with buttons A and B together completing text entry
# - Add audio acknowledgements on button press
# - While text is scrolling, the A / B buttons could slow down / speed up the scrolling rate
# - Allow emojis to be entered
# - The entered text could be sent out via email or Twitter (maybe!)
#
# Let me know what you think! @computingchamps on Twitter
#

import microbit as m

# Abbreviations to save typos, especially on "accelerometer"!
d = m.display
ac = m.accelerometer

# Built in images used to acknowledge button presses
happy = m.Image.HAPPY
heart = m.Image.HEART

# List containing the alphabet in order, plus spaces at the beginning and the end
alphabet = [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
myWord = []

def main():
    while m.button_b.is_pressed() == False:
        # Set the counter to the middle of the alphabet list
        i = int(len(alphabet)/2)
        while m.button_a.is_pressed() == False:
            letterAdded = False
            # If micro:bit is titled right, move up through the alphabet until you reach the end
            if ac.get_x() > 200 and i < (len(alphabet)-1):
                i += 1
                d.show(alphabet[i])
            # If micro:bit is titled left, move down through the alphabet until you reach the start
            elif ac.get_x() < -200 and i > 0:
                i -= 1
                d.show(alphabet[i])
            # If micro:bit is held still, display the current letter (or a dash if they're on the space at the start / end)
            else:
                d.show(alphabet[i])
                if i == 0 or i == (len(alphabet)-1):
                    d.show("-")
            m.sleep(500)
        
        # Acknowledge button A press with a happy face and place the selected letter into the myWord list 
        d.show(happy)
        # Ensures the letter is only added once to the list, even if button A is held down
        while letterAdded == False:
            letterAdded = True
            myWord.append(alphabet[i])
        m.sleep(500)
    
    # Acknowledge button B press with a heart, convert the myWord list to a string and then scroll the text across the screen continuously
    d.show(heart)
    m.sleep(500)
    myString = "".join(str(k) for k in myWord)
    while True:
        d.scroll(myString, 200)
    
main()
