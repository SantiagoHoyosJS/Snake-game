import pygame as pg
from random import randrange
from tkinter import *
import csv

root = Tk()
root.iconbitmap('C:/Users/santi/OneDrive/Escritorio/snake game/snake-icon.ico')


def main():   
    login()
    game()

def game():
    WINDOW = 600
    TILE_SIZE = 50
    RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
    get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)]
    snake = pg.rect.Rect([0,0, TILE_SIZE - 2, TILE_SIZE - 2])
    snake.center = get_random_position()
    length = 1
    segments = [snake.copy()]
    snake_dir = (0,0)
    time, time_step = 0, 150
    food = snake.copy()
    food.center = get_random_position()
    screen = pg.display.set_mode([WINDOW]*2)
    clock = pg.time.Clock()
    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w and dirs[pg.K_w]:
                    snake_dir = (0, -TILE_SIZE)
                    dirs = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1, pg.K_d: 1}
                if event.key == pg.K_s and dirs[pg.K_s]:
                    snake_dir = (0, TILE_SIZE)
                    dirs = {pg.K_w: 0, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
                if event.key == pg.K_a and dirs[pg.K_a]:
                    snake_dir = (-TILE_SIZE, 0)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 0}
                if event.key == pg.K_d and dirs[pg.K_d]:
                    snake_dir = (TILE_SIZE, 0)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 0, pg.K_d: 1}
                
        screen.fill('black')
        #check borders and selfeating
        self_eating = pg.Rect.collidelist(snake, segments[:-1]) != -1
        if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
            snake.center, food.center = get_random_position(), get_random_position()
            length, snake_dir = 1, (0,0)
            segments = [snake.copy()]
        #check food
        if snake.center == food.center:
            food.center = get_random_position()
            length += 1
        #draw food
        pg.draw.rect(screen, 'red', food)
        # draw snake
        [pg.draw.rect(screen, 'green', segment) for segment in segments]
        #move snake
        time_now = pg.time.get_ticks()
        if time_now - time > time_step:
            time = time_now
            snake.move_ip(snake_dir)
            segments.append(snake.copy())
            segments = segments[-length:]
        pg.display.flip()
        clock.tick(60)



def check_login(usarname, password):
    with open('credentials.csv', 'r', newline='') as c:
        reader = csv.reader(c)
        for row in reader:
            if row[0] == usarname:
                if row[1] == password:
                    root.destroy()
                    return
                else:
                    status_label = Label(root, text="Wrong password", bg='black', fg='white')
                    status_label.pack()
                    username_entry_l.delete(0, END)
                    password_entry_l.delete(0, END)
                    return
        status_label = Label(root, text="This username does not exist", bg='black', fg='white')
        status_label.pack()
        username_entry_l.delete(0, END)
        password_entry_l.delete(0, END)
        return

def register(username, password, top):
    with open('credentials.csv', 'r', newline='') as c:
        reader = csv.reader(c)
        for row in reader:
            if username in row:
                status_label = Label(top, text="This username is already taken", bg='black', fg='white')
                status_label.pack()
                username_entry_s.delete(0, END)
                password_entry_s.delete(0, END)
                return
    with open('credentials.csv', 'a', newline='') as c:
        writer = csv.writer(c)
        row = [username, password]
        writer.writerow(row)
    top.destroy()

def signup_window():

    top = Toplevel()
    # Create a new Tkinter window
    top.title("Snake Game")
    top.geometry("600x600+400+100")
    top.configure(background="black")

    # Create a label for the username field
    username_label = Label(top, text="Username:", bg='black', fg='white')
    username_label.pack()

    # Create an entry field for the username
    global username_entry_s; username_entry_s = Entry(top)
    username_entry_s.pack()

    # Create a label for the password field
    password_label = Label(top, text="Password:", bg='black', fg='white')
    password_label.pack()

    # Create an entry field for the password
    global password_entry_s; password_entry_s = Entry(top, show="*")
    password_entry_s.pack()
    # Create a button to submit the login credentials
    submit_button = Button(top, text="Sign up", command= lambda: register(username_entry_s.get(), password_entry_s.get(), top))
    submit_button.pack()
    username_entry_s.delete(0, END)
    password_entry_s.delete(0, END)

def login():
    # Create a new Tkinter window
    root.title("Snake Game")
    root.geometry("600x600+400+100")
    root.configure(background="black")

    # Create a label for the username field
    username_label = Label(root, text="Username:", bg='black', fg='white')
    username_label.pack()

    # Create an entry field for the username
    global username_entry_l; username_entry_l = Entry(root)
    username_entry_l.pack()

    # Create a label for the password field
    password_label = Label(root, text="Password:", bg='black', fg='white')
    password_label.pack()

    # Create an entry field for the password
    global password_entry_l; password_entry_l = Entry(root, show="*")
    password_entry_l.pack()

    # Create a button to submit the login credentials
    submit_button = Button(root, text="Login", command= lambda: check_login(username_entry_l.get(), password_entry_l.get()))
    submit_button.pack()

    signup = Button(root, text="Create new account", command=signup_window).pack()

    # Run the main event loop
    root.mainloop()

if __name__ == "__main__":
    main()    