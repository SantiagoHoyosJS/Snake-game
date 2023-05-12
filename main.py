import pygame as pg
from random import randrange
from tkinter import *
import csv
import random

root = Tk()
root.iconbitmap('snake-icon.ico')
pg.init()
q = Toplevel(root)
q.title("Snake Game")
q.geometry("400x500+450+100")
q.configure(background="black")
q.withdraw()
questions = {'¿Cuál es la diferencia principal entre una lista y una lista doblemente enlazada?':'a',
             '¿Qué es una multilista?':'c','¿Qué es una operación pop en una lista doblemente enlazada?':'c','¿Qué es una lista circular?':'b',
             '¿Cuál es la diferencia entre una lista simple y una lista circular?':'b','¿Qué es una lista doblemente enlazada circular?':'b',
             'Uno de los principales usos de las estructuras de datos tipo pila es:':'b',
             'Una estructura lineal tipo Lista enlazada se puede definir como: ':'a',
             'El valor almacenado en una variable de tipo apuntador es: ':'a',
             'De las siguientes opciones identifique el tipo de lista que cumpla con las siguientes características. Es un tipo de lista lineal en la que cada nodo tiene dos enlaces, uno que apunta al nodo siguiente, y otro que apunta al anterior, adicionalmente el último nodo de la lista apunta al primer nodo.':'a'}
options = {'¿Cuál es la diferencia principal entre una lista y una lista doblemente enlazada?':
['A) Las listas simples solo pueden ser recorridas en una dirección, mientras que las listas doblemente enlazadas pueden ser recorridas en ambas direcciones.',
'B) Las listas doblemente enlazadas tienen un nodo central, mientras que las listas solo tienen nodos en extremos.',
'C) Las listas doblemente enlazadas pueden tener elementos repetidos, mientras que las listas no.',
'D) Las listas doblemente enlazadas son más rápidas que las listas.'],
'¿Qué es una multilista?':
['A) Una estructura de datos en la que cada elemento puede tener múltiples atributos.',
'B) Una estructura de datos en la que cada elemento puede tener múltiples valores.',
'C) Una estructura de datos en la que cada elemento puede estar en múltiples listas.',
'D) Una estructura de datos en la que cada elemento puede tener múltiples punteros.'],
'¿Qué es una operación pop en una lista doblemente enlazada?':
['A) Agregar un elemento al final de la lista.',
'B) Agregar un elemento al principio de la lista.',
'C) Eliminar el último elemento de la lista.',
'D) Eliminar el primer elemento de la lista.'],
'¿Qué es una lista circular?':
['A) Una lista en la que cada elemento tiene dos punteros.',
'B) Una lista en la que el último elemento apunta al primero.',
'C) Una lista en la que el primer elemento apunta al último.',
'D) Una lista en la que cada elemento está conectado a todos los demás elementos.'],
'¿Cuál es la diferencia entre una lista simple y una lista circular?':
['A) En una lista circular, cada elemento tiene dos punteros, mientras que en una lista simple cada elemento tiene solo un puntero.',
'B) En una lista circular, el último elemento apunta al primero, mientras que en una lista simple el último elemento no tiene un puntero.',
'C) En una lista circular, el primer elemento apunta al último, mientras que en una lista simple el primer elemento no tiene un puntero.',
'D) No hay diferencia, una lista circular es lo mismo que una lista simple.'],
'¿Qué es una lista doblemente enlazada circular?':
['A) Una lista en la que cada elemento tiene dos punteros y el último elemento apunta al primero.',
'B) Una lista en la que cada elemento tiene dos punteros y el primer elemento apunta al último.',
'C) Una lista en la que cada elemento tiene cuatro punteros y está conectado a todos los demás elementos.',
'D) Una lista en la que cada elemento tiene un puntero y está conectado a todos los demás elementos.'],
'Uno de los principales usos de las estructuras de datos tipo pila es: ':
[ 'A. Control de problemas matemáticos', 
 'B. tipo Tratamiento de expresiones matemáticas ',  
 'C. Almacenar datos de cualquier',
 'D. Ingresar datos y conservar el orden de llegada'],
 'Una estructura lineal tipo Lista enlazada se puede definir como: ': 
 ['A. Una colección de nodos o elementos en donde cada uno contiene datos y un enlace al siguiente nodo', 
 'B. Es una colección de nodos en donde cada uno tiene un enlace que apunta a cualquier otro nodo',
 'C. Un tipo de dato numérico ordenados secuencialmente unidos por un enlace', 
 'D. Una colección ordenada de elementos secuencialmente'],
 'El valor almacenado en una variable de tipo apuntador es: ':
 ['A.  Una dirección de memoria',
  'B.  Un dato de tipo int',
  'C. El contenido de otra variable de diferente tipo', 
  'D. Un dato de tipo char'],
  'De las siguientes opciones identifique el tipo de lista que cumpla con las siguientes características. Es un tipo de lista lineal en la que cada nodo tiene dos enlaces, uno que apunta al nodo siguiente, y otro que apunta al anterior, adicionalmente el último nodo de la lista apunta al primer nodo.':
  ['A. Lista doblemente enlazada',
 'B. Lista contigua',
 'C. Lista lineal',
 'D. Lista circular']
}


def main():   
    login()

def game(score):
    game_font = pg.font.Font(None, 25)
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
        q.withdraw()
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
                
        screen.fill('grey')
        #check borders and selfeating
        self_eating = pg.Rect.collidelist(snake, segments[:-1]) != -1
        if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
            ranquestion(score)
            #check_ans(question_label, ans)
            snake.center, food.center = get_random_position(), get_random_position()
            length, snake_dir = 1, (0,0)
            segments = [snake.copy()]

        #check food
        if snake.center == food.center:
            food.center = get_random_position()
            length += 1
            score += 1
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
        score_text = str(score)
        score_surface = game_font.render(score_text, True, (255,255,255))
        score_x = 20
        score_y = 20
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        screen.blit(score_surface, score_rect)
        pg.display.flip()
        clock.tick(60)

def ranquestion(score):
    q.deiconify()
    p=getRandomQ()
    # Create a label for the username field
    global question_label; question_label = Label(q, text=p, bg='black', fg='white', wraplength=200)
    question_label.pack(padx=10, pady=10)


    # Create an entry field for answear
    global ans; ans = Entry(q)
    ans.pack(padx=10, pady=10)

    #display options
    for op in options[p]:
        Label(q, text=op, bg='black', fg='white', wraplength=200).pack(padx=5, pady=5)

    #button to send answear
    submit_button = Button(q, text="Responder", command= lambda: check_ans(p,ans.get().lower(),score))
    submit_button.pack(padx=10, pady=10)   
    #return if the question was answeared correctly or not 
    root.mainloop()



def check_ans(question,ans,score):
    if questions[question] == ans:
        print('yes')
        for widget in q.winfo_children():
            widget.destroy()
        game(score)
        return True
    else:
        print('no')
        for widget in q.winfo_children():
            widget.destroy()
        game(0)
        return False

def getRandomQ():
    # Get a random key-value pair from the dictionary
    random_Q, random_A = random.choice(list(questions.items()))
    return random_Q

def check_login(usarname, password):
    with open('credentials.csv', 'r', newline='') as c:
        reader = csv.reader(c)
        for row in reader:
            if row[0] == usarname:
                if row[1] == password:
                    root.withdraw()
                    game(0)
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
    username_label.pack(padx=10, pady=10)

    # Create an entry field for the username
    global username_entry_s; username_entry_s = Entry(top)
    username_entry_s.pack(padx=10, pady=10)

    # Create a label for the password field
    password_label = Label(top, text="Password:", bg='black', fg='white')
    password_label.pack(padx=10, pady=10)

    # Create an entry field for the password
    global password_entry_s; password_entry_s = Entry(top, show="*")
    password_entry_s.pack(padx=10, pady=10)
    # Create a button to submit the login credentials
    submit_button = Button(top, text="Sign up", command= lambda: register(username_entry_s.get(), password_entry_s.get(), top))
    submit_button.pack(padx=10, pady=10)
    username_entry_s.delete(0, END)
    password_entry_s.delete(0, END)

def login():
    # Create a new Tkinter window
    root.title("Snake Game")
    root.geometry("600x600+400+100")
    root.configure(background="black")

    # Create a label for the username field
    username_label = Label(root, text="Username:", bg='black', fg='white')
    username_label.pack(padx=10, pady=10)

    # Create an entry field for the username
    global username_entry_l; username_entry_l = Entry(root)
    username_entry_l.pack(padx=10, pady=10)

    # Create a label for the password field
    password_label = Label(root, text="Password:", bg='black', fg='white')
    password_label.pack(padx=10, pady=10)

    # Create an entry field for the password
    global password_entry_l; password_entry_l = Entry(root, show="*")
    password_entry_l.pack(padx=10, pady=10)

    # Create a button to submit the login credentials
    submit_button = Button(root, text="Login", command= lambda: check_login(username_entry_l.get(), password_entry_l.get()))
    submit_button.pack(padx=10, pady=10)
    

    signup = Button(root, text="Create new account", command=signup_window).pack(padx=10, pady=10)


    # Run the main event loop
    root.mainloop()

if __name__ == "__main__":
    main()    