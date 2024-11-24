import tkinter as tk
import math

# Configurações de tela
width, height = 600, 400
num_rotations = 36  # Número de fatias na rotação (quanto maior, mais suave o objeto)

# Inicialização do Z-buffer com profundidade infinita
zbuffer = [[float('inf') for _ in range(width)] for _ in range(height)]
perfil = []  # Armazena os pontos do perfil desenhado pelo usuário

# Função para projetar um ponto 3D em 2D
def project(x, y, z):
    fov = 200  # fator de "zoom"
    x_proj = int(width / 2 + fov * x / (z + fov))
    y_proj = int(height / 2 - fov * y / (z + fov))
    return x_proj, y_proj

# Função para desenhar pontos com Z-buffer
def draw_point(canvas, x, y, z, color="black"):
    px, py = project(x, y, z)
    if 0 <= px < width and 0 <= py < height:
        if z < zbuffer[py][px]:
            zbuffer[py][px] = z  # Atualiza profundidade
            canvas.create_oval(px, py, px+1, py+1, fill=color, outline=color)

# Função para rotacionar e desenhar o perfil em 3D
def render_3d(canvas):
    for i in range(num_rotations):
        angle = 2 * math.pi * i / num_rotations
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)

        for x, y in perfil:
            x_rot = x * cos_a
            z_rot = x * sin_a
            draw_point(canvas, x_rot, y, z_rot)

# Função para salvar o perfil desenhado pelo usuário
def on_click(event):
    perfil.append((event.x - width / 4, height / 2 - event.y))
    canvas.create_oval(event.x, event.y, event.x+1, event.y+1, fill="blue")

# Função para limpar e renderizar o objeto 3D
def on_render():
    canvas.delete("all")
    for y in range(height):
        for x in range(width):
            zbuffer[y][x] = float('inf')
    render_3d(canvas)

# Configuração da janela Tkinter
janela = tk.Tk()
janela.title("Varredura Rotacional 3D")
canvas = tk.Canvas(janela, width=width, height=height, bg="white")
canvas.pack()

# Instruções e eventos
canvas.bind("<Button-1>", on_click)
render_button = tk.Button(janela, text="Renderizar 3D", command=on_render)
render_button.pack()

janela.mainloop()
