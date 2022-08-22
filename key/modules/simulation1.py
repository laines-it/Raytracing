import random
from tkinter import *
from PIL import Image, ImageTk
from time import time
from math import floor

# Workspace
root = Tk()
root.resizable(False, False)
img = Image.open("bg1.png")
bg = ImageTk.PhotoImage(img)
c = Canvas(root, width=bg.width() + 10, height=bg.height() + 10)
c.pack(expand=True, fill=BOTH)
c.create_image(10, 10, image=bg, anchor=NW)
lang = "eng"

# Consts
key_size = bg.width() / 25.6
keyspace = key_size // 10
words_need = 10
keyboard_x = bg.width() // 5
keyboard_y = bg.height() // 2
text_x = bg.width() // 2
text_y = keyboard_y // 2
bar_x = keyboard_x
bar_y = text_y // 3
bar_len = key_size * 17.6 / words_need
bar = c.create_rectangle(0, 0, 0, 0)

# Auxiliary lists and vars
ended = False
starting_time = time()
previous_chars = 0
text_all = ''
average_word_length = 0
words = []
error_text = []
right_text = []
keys_created = []
indexes_keys = []
all_words = 0
words_count = 0
text = ''
shifted = False
not_letters = ["BackSpace", "Tab", "Return", "Caps_Lock", "Shift_L",
               "Shift_R", "Control_L", "Win_L", "Alt_L", "Alt_R", "Control_R"]

# Keyboards
lang_eng = [["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "BackSpace"],
            ["Tab", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]", "Return"],
            ["Caps_Lock", "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'"],
            ["Shift_L", "z", "x", "c", "v", "b", "n", "m", ",", ".", "/", "Shift_R"],
            ["Ctrl", "Win", "Alt", "space", "Alt", "Fn", "List", "Ctrl"]]
lang_eng_shift = [["~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "BackSpace"],
                  ["Tab", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "{", "}", "Return"],
                  ["Caps_Lock", "A", "S", "D", "F", "G", "H", "J", "K", "L", ":", '""'],
                  ["Shift_L", "Z", "X", "C", "V", "B", "N", "M", "<", ">", "?", "Shift_R"],
                  ["Ctrl", "Win", "Alt", "space", "Alt", "Fn", "List", "Ctrl"]]
lang_rus = [["ё", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "BackSpace"],
            ["Tab", "й", "ц", "у", "к", "е", "н", "г", "ш", "щ", "з", "х", "ъ", "Return"],
            ["Caps_Lock", "ф", "ы", "в", "а", "п", "р", "о", "л", "д", "ж", "э"],
            ["Shift_L", "я", "ч", "с", "м", "и", "т", "ь", "б", "ю", ".", "Shift_R"],
            ["Ctrl", "Win", "Alt", "space", "Alt", "Fn", "List", "Ctrl"]]


def create_keyboard():
    # This method creates a visual keyboard uses create_key()
    # Only English is available

    global keys_created
    global indexes_keys
    keys_created = []
    indexes_keys = []
    if shifted:
        my_language = lang_eng_shift
    else:
        my_language = lang_eng
    for hor in range(5):
        k = 0
        dop = 0
        for vert in my_language[hor]:
            if hor == 0 and vert == "BackSpace":
                create_key("BackSpace",
                           keyboard_x + (key_size + keyspace) * k,
                           keyboard_y + (key_size + keyspace) * hor,
                           keyboard_x + (key_size + keyspace) * k + key_size * 3,
                           keyboard_y + (key_size + keyspace) * hor + key_size,
                           radius=20,
                           fill="white")
            elif hor == 1 and vert == "Tab":
                dop += key_size / 2
                create_key(vert,
                           keyboard_x + (key_size + keyspace) * k,
                           keyboard_y + (key_size + keyspace) * hor,
                           keyboard_x + (key_size + keyspace) * k + key_size + dop,
                           keyboard_y + (key_size + keyspace) * hor + key_size,
                           radius=20, fill="white")
            elif hor == 1 and vert == "Return":
                create_key("Enter",
                           keyboard_x + (key_size + keyspace) * k + dop,
                           keyboard_y + (key_size + keyspace) * hor,
                           keyboard_x + (key_size + keyspace) * k + key_size * 1.5 + dop,
                           keyboard_y + (key_size + keyspace) * hor + (key_size * 2 + keyspace),
                           radius=20,
                           fill="white")
            elif hor == 2 and vert == "Caps_Lock":
                dop += key_size
                create_key("Caps",
                           keyboard_x + (key_size + keyspace) * k,
                           keyboard_y + (key_size + keyspace) * hor,
                           keyboard_x + (key_size + keyspace) * k + key_size + dop,
                           keyboard_y + (key_size + keyspace) * hor + key_size,
                           radius=20,
                           fill="white")
            elif hor == 3 and vert == "Shift_L":
                dop += key_size * 1.5
                create_key(vert,
                           keyboard_x + (key_size + keyspace) * k,
                           keyboard_y + (key_size + keyspace) * hor,
                           keyboard_x + (key_size + keyspace) * k + key_size + dop,
                           keyboard_y + (key_size + keyspace) * hor + key_size,
                           radius=20,
                           fill="white")

            elif hor == 3 and vert == "Shift_R":
                create_key(vert,
                           keyboard_x + (key_size + keyspace) * k + dop,
                           keyboard_y + (key_size + keyspace) * hor,
                           keyboard_x + (key_size + keyspace) * k + key_size * 2.5 + dop,
                           keyboard_y + (key_size + keyspace) * hor + key_size,
                           radius=20,
                           fill="white")
                dop += 75
            elif hor == 4 and vert == "space":
                dop += key_size * 7.5
                create_key("space",
                           keyboard_x + (key_size + keyspace) * k,
                           keyboard_y + (key_size + keyspace) * hor,
                           keyboard_x + (key_size + keyspace) * k + key_size + dop,
                           keyboard_y + (key_size + keyspace) * hor + key_size,
                           radius=20,
                           fill="white")

            else:
                create_key(vert,
                           keyboard_x + (key_size + keyspace) * k + dop,
                           keyboard_y + (key_size + keyspace) * hor,
                           keyboard_x + (key_size + keyspace) * k + key_size + dop,
                           keyboard_y + (key_size + keyspace) * hor + key_size,
                           radius=20,
                           fill="white")
            k += 1


def create_key(key, x1, y1, x2, y2, radius=25, **kwargs):
    # This method creates a visual keyboard button with symbol on it
    points = [x1 + radius, y1,
              x1 + radius, y1,
              x2 - radius, y1,
              x2 - radius, y1,
              x2, y1,
              x2, y1 + radius,
              x2, y1 + radius,
              x2, y2 - radius,
              x2, y2 - radius,
              x2, y2,
              x2 - radius, y2,
              x2 - radius, y2,
              x1 + radius, y2,
              x1 + radius, y2,
              x1, y2,
              x1, y2 - radius,
              x1, y2 - radius,
              x1, y1 + radius,
              x1, y1 + radius,
              x1, y1]
    key_button = c.create_polygon(points, **kwargs, smooth=True)
    c.create_text((x2 + x1) // 2, (y2 + y1) // 2, text=key, fill="black", font="Times 20")
    keys_created.append(key_button)
    indexes_keys.append(key)


def change_color(thing, rgb):
    # This func change color according "rgb" argument
    return c.itemconfig(thing, fill=color_rgb(rgb))


def color_rgb(rgb):
    # This func helps previous func to perceive RGB
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'


def change_color_letter(current_letter, current_text, right, key):
    # This method changes a text's letters according is a user type key right
    if right:
        green_text = current_text[:current_letter + 1] + ' ' * (len(current_text) - current_letter - 1)
        right_text.append(c.create_text(text_x, text_y, text=green_text, font="Courier 40", fill="lawn green"))
    else:
        if key == 'space':
            red_text = error_now * '  ' + '_' + ' ' * (len(current_text) - current_letter)
        else:
            red_text = error_now * '  ' + key + ' ' * (len(current_text) - current_letter)

        error_text.append(c.create_text(text_x, text_y + 40, text=red_text, font="Courier 40", fill="red"))


''' 
Colors meanings:
    Green = right key
    Yellow = service key
    Red = wrong key
'''


def on_key_press(event):
    # This method processes key pressing
    pressed_key = event.keysym
    global key_now
    global text
    global shifted
    global words_count
    global textview
    global errors
    global error_now
    global previous_chars
    global speed_textview
    global words_textview
    global char_textview

    if pressed_key == 'Shift_L' or pressed_key == 'Shift_R':
        shifted = True
        create_keyboard()
    if pressed_key == 'Caps_Lock':
        if shifted:
            shifted = False
        else:
            shifted = True
        create_keyboard()
    for i in range(len(indexes_keys)):
        if pressed_key == indexes_keys[i]:
            # Finding pressed key in all keys list
            if (text[key_now] == pressed_key or (pressed_key == 'space' and text[key_now] == ' ')) and error_now <= 0:
                # if pressed key was right
                if pressed_key == 'space':
                    # word ended
                    words_count += 1
                    update_bar(words_count)
                    # Displaying number of typed words
                    words_text = str(words_count) + ' words'
                    c.delete(words_textview)
                    words_textview = c.create_text(text_x + 530, text_y - 100, text=words_text, font="Courier 30")
                change_color(keys_created[i], (0, 255, 0))
                change_color_letter(key_now, text, True, pressed_key)
                if key_now + 1 < len(text):
                    key_now += 1
                    # Displaying typing speed
                    speed_text = str(floor(((key_now + previous_chars) / average_word_length) / ((time() - starting_time) / 60))) + ' wpm'
                    c.delete(speed_textview)
                    speed_textview = c.create_text(text_x, text_y + 100, text=speed_text, font="Courier 40")
                else:
                    # text on screen changes
                    c.delete(textview)
                    for past_word in right_text:
                        c.delete(past_word)
                    previous_chars += key_now
                    key_now = 0
                    text = create_text(lang)
                    textview = c.create_text(text_x, text_y, text=text, font="Courier 40")
                    if not ended:
                        # Displaying typing speed
                        speed_text = str(floor(((key_now + previous_chars) / average_word_length) / ((time() - starting_time) / 60))) + ' wpm'
                        c.delete(speed_textview)
                        speed_textview = c.create_text(text_x, text_y + 100, text=speed_text, font="Courier 40")
                # Displaying number of typed words
                char_text = str(key_now + previous_chars) + ' characters'
                c.delete(char_textview)
                char_textview = c.create_text(text_x + 470, text_y - 60, text=char_text, font="Courier 30")
            elif pressed_key not in not_letters:
                # if key was wrong
                change_color(keys_created[i], (255, 0, 0))
                errors += 1
                error_now += 1
                change_color_letter(key_now, text, False, pressed_key)
            elif pressed_key == "BackSpace" and error_now > 0:
                # if key is BackSpace (it is a special key)
                change_color(keys_created[i], (0, 255, 0))
                c.delete(error_text[error_now - 1])
                error_text.pop(error_now - 1)
                error_now -= 1
            else:
                # if key is service
                change_color(keys_created[i], (255, 255, 0))


def on_key_release(event):
    # This method processes key releasing
    global key_now
    if event.keysym == 'Shift_L' or event.keysym == 'Shift_R':
        global shifted
        shifted = False
        create_keyboard()
    for i in range(len(indexes_keys)):
        if event.keysym == indexes_keys[i]:
            change_color(keys_created[i], (255, 255, 255))


# Reading 3000 english words from file
ws = open("words_en.txt", "r")
while True:
    w = ws.readline()
    if not w:
        break
    else:
        words.append(w.strip())
ws.close()


def create_text(voc):
    # This func randomly creates a on-screen text taking few words from words list
    global all_words
    global text
    global text_all
    global average_word_length
    global speed_textview
    global ended
    if all_words >= words_need:
        ended = True
        if voc == "eng":
            # Displaying final time
            final_text = "Overall time - " + str(floor(time() - starting_time) // 60) + ':' + str(floor(time() - starting_time) % 60)
            c.create_text(text_x + 390, text_y - 20, text=final_text, font="Courier 30")
            # Displaying average word length
            final_text = 'Average word length - ' + str(average_word_length)
            c.create_text(text_x + 350, text_y + 20, text=final_text, font="Courier 30")
            # Displaying average typing speed
            final_text = 'Average typing speed - ' + str(floor(((key_now + previous_chars) / average_word_length) / ((time() - starting_time) / 60))) + ' wpm'
            c.delete(speed_textview)
            c.create_text(text_x + 270, text_y + 60, text=final_text, font="Courier 30")
    else:
        text = ''
        for i in range(random.randint(1, 4)):
            all_words += 1
            one_word = random.choice(words)
            if random.random() > 0:
                one_word.upper()
            text += one_word + ' '
            if all_words > words_need:
                break
        text_all += text
        average_word_length = floor((len(text_all) - (all_words - 1)) / all_words)
        return text


def update_bar(words_completed):
    # This method updating progress bar
    global bar
    c.delete(bar)
    bar = c.create_rectangle(bar_x, bar_y, bar_x + words_completed * bar_len, 20, fill="green")


# Final setup
create_keyboard()
text = create_text(lang)
update_bar(0)
key_now = 0
errors = 0
error_now = 0
textview = c.create_text(text_x, text_y, text=text, font="Courier 40")
speed_textview = c.create_text(text_x, text_y + 100, text='0 wpm', font="Courier 40")
words_textview = c.create_text(text_x + 530, text_y - 100, text='0 words', font="Courier 30")
char_textview = c.create_text(text_x + 490, text_y - 60, text='0 characters', font="Courier 30")

# Binds
root.bind('<KeyPress>', on_key_press)
root.bind('<KeyRelease>', on_key_release)

# Loops
root.update()
root.mainloop()
