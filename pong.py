import tkinter as tk
import random

# Inicjalizacja okna gry
root = tk.Tk()
root.title("Pong")

# Wymiary okna gry
WIDTH = 400
HEIGHT = 300

# Inicjalizacja canvas
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

# Inicjalizacja paletki gracza 1
paddle1_width = 60
paddle1_height = 10
paddle1_x = (WIDTH - paddle1_width) // 2
paddle1_y = HEIGHT - 20
paddle1 = canvas.create_rectangle(
    paddle1_x, paddle1_y, paddle1_x + paddle1_width, paddle1_y + paddle1_height, fill="blue"
)

# Inicjalizacja paletki gracza 2
paddle2_width = 60
paddle2_height = 10
paddle2_x = (WIDTH - paddle2_width) // 2
paddle2_y = 10
paddle2 = canvas.create_rectangle(
    paddle2_x, paddle2_y, paddle2_x + paddle2_width, paddle2_y + paddle2_height, fill="red"
)

# Inicjalizacja piłki
ball_width = 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = 3
ball_dy = 3
ball = canvas.create_oval(
    ball_x, ball_y, ball_x + ball_width, ball_y + ball_width, fill="green"
)

# Inicjalizacja flagi zakończenia gry
game_over = False

# Inicjalizacja flag do poruszania paletkami
paddle1_move_left = False
paddle1_move_right = False
paddle2_move_left = False
paddle2_move_right = False

# Ruch paletki gracza 1
def move_paddle1():
    global paddle1_move_left, paddle1_move_right, paddle1_x
    if paddle1_move_left and paddle1_x > 0:
        canvas.move(paddle1, -5, 0)
        paddle1_x -= 5
    if paddle1_move_right and paddle1_x + paddle1_width < WIDTH:
        canvas.move(paddle1, 5, 0)
        paddle1_x += 5
    root.after(10, move_paddle1)

# Ruch paletki gracza 2
def move_paddle2():
    global paddle2_move_left, paddle2_move_right, paddle2_x
    if paddle2_move_left and paddle2_x > 0:
        canvas.move(paddle2, -5, 0)
        paddle2_x -= 5
    if paddle2_move_right and paddle2_x + paddle2_width < WIDTH:
        canvas.move(paddle2, 5, 0)
        paddle2_x += 5
    root.after(10, move_paddle2)

# Obsługa zdarzeń przytrzymania klawiszy
def key_pressed(event):
    global paddle1_move_left, paddle1_move_right, paddle2_move_left, paddle2_move_right
    key = event.keysym
    if key == "Left":
        paddle1_move_left = True
    elif key == "Right":
        paddle1_move_right = True
    elif key == "a":
        paddle2_move_left = True
    elif key == "d":
        paddle2_move_right = True

def key_released(event):
    global paddle1_move_left, paddle1_move_right, paddle2_move_left, paddle2_move_right
    key = event.keysym
    if key == "Left":
        paddle1_move_left = False
    elif key == "Right":
        paddle1_move_right = False
    elif key == "a":
        paddle2_move_left = False
    elif key == "d":
        paddle2_move_right = False

# Wyświetlanie komunikatu o zakończeniu gry
def end_game(message):
    global game_over
    game_over = True
    canvas.create_text(
        WIDTH // 2,
        HEIGHT // 2,
        text=message,
        font=("Helvetica", 20),
        fill="white",
        justify=tk.CENTER,
    )

# Aktualizacja pozycji piłki
def update_ball_position():
    global ball_x, ball_y, ball_dx, ball_dy, game_over

    if game_over:
        return

    ball_x += ball_dx
    ball_y += ball_dy

    # Odbicie piłki od krawędzi bocznych
    if ball_x <= 0 or ball_x + ball_width >= WIDTH:
        ball_dx = -ball_dx

    # Odbicie piłki od paletki gracza 1
    if (
        ball_y + ball_width >= paddle1_y
        and ball_x >= paddle1_x
        and ball_x <= paddle1_x + paddle1_width
    ):
        ball_dy = -ball_dy

    # Odbicie piłki od paletki gracza 2
    if (
        ball_y <= paddle2_y + paddle2_height
        and ball_x >= paddle2_x
        and ball_x <= paddle2_x + paddle2_width
    ):
        ball_dy = -ball_dy

    # Sprawdzenie, czy piłka przekroczyła górną lub dolną granicę
    if ball_y <= 0 or ball_y + ball_width >= HEIGHT:
        end_game("Koniec gry")

    canvas.move(ball, ball_dx, ball_dy)
    root.after(10, update_ball_position)

# Przypisanie funkcji do obsługi zdarzeń klawiatury
canvas.bind("<KeyPress>", key_pressed)
canvas.bind("<KeyRelease>", key_released)
canvas.focus_set()

# Uruchomienie gry
update_ball_position()
move_paddle1()
move_paddle2()

root.mainloop()
