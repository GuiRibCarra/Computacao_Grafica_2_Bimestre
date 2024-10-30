import tkinter as tk


# Função para criar o bounding box
def bounding_box(pontos):
    x_min = min(p[0] for p in pontos)
    x_max = max(p[0] for p in pontos)
    y_min = min(p[1] for p in pontos)
    y_max = max(p[1] for p in pontos)
    return (x_min, y_min, x_max, y_max)


# Função recursiva para preencher o polígono (Flood-Fill)
def flood_fill(x, y, canvas, target_cwolor, fill_color):
    current_color = canvas.gettags(canvas.find_closest(x, y))
    if current_color == target_color:
        # Altera a cor do pixel
        canvas.itemconfig(canvas.find_closest(x, y), fill=fill_color)

        # Chama a função recursivamente nas direções vizinhas
        flood_fill(x + 1, y, canvas, target_color, fill_color)
        flood_fill(x - 1, y, canvas, target_color, fill_color)
        flood_fill(x, y + 1, canvas, target_color, fill_color)
        flood_fill(x, y - 1, canvas, target_color)


# Função para desenhar e preencher o polígono
def desenha_poligono(canvas, pontos, fill_color):
    # Desenha o polígono
    poly = canvas.create_polygon(pontos, outline='black', fill='white', tags="poly")

    # Calcula o bounding box
    x_min, y_min, x_max, y_max = bounding_box(pontos)
    canvas.create_rectangle(x_min, y_min, x_max, y_max, outline="blue")

    # Inicia o preenchimento com flood-fill
    # Pegamos um ponto dentro do polígono
    start_x, start_y = pontos[0]
    flood_fill(start_x + 1, start_y + 1, canvas, "poly", fill_color)


# Configuração da janela
janela = tk.Tk()
janela.title("Flood-Fill com Bounding Box")
canvas = tk.Canvas(janela, width=400, height=400)
canvas.pack()

# Pontos do polígono
pontos_poligono = [(50, 50), (300, 100), (250, 300), (100, 250)]

# Desenha e preenche o polígono
desenha_poligono(canvas, pontos_poligono, "red")

# Inicia a janela
janela.mainloop()
