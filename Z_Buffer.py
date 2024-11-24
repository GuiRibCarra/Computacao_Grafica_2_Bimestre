import tkinter as tk
import math

# Configurações de tela
width, height = 500, 500

# Inicialização do Z-buffer com profundidade infinita
zbuffer = [[float('inf') for _ in range(width)] for _ in range(height)]

# Função para projetar um ponto 3D em 2D
def project(x, y, z):
    # Ajuste para centralizar e aproximar os objetos
    fov = 200  # fator de "zoom"
    x_proj = int(width / 2 + fov * x / (z + fov))
    y_proj = int(height / 2 - fov * y / (z + fov))
    return x_proj, y_proj

# Função para desenhar pontos com Z-buffer
def draw_point(canvas, x, y, z, color):
    px, py = project(x, y, z)
    if 0 <= px < width and 0 <= py < height:
        # Verifica e atualiza o Z-buffer
        if z < zbuffer[py][px]:
            zbuffer[py][px] = z  # Atualiza profundidade
            canvas.create_oval(px, py, px+1, py+1, fill=color, outline=color)

# Configuração da janela Tkinter
janela = tk.Tk()
janela.title("Z-buffer com Objetos 3D")
canvas = tk.Canvas(janela, width=width, height=height, bg="white")
canvas.pack()

# Objeto 1 (azul): z = x^2 + y
for x in range(10, 31):
    for y in range(20, 41):
        z = x**2 + y
        draw_point(canvas, x, y, z, "blue")

# Objeto 2 (vermelho): z = 3x - 2y + 5
for x in range(50, 101):
    for y in range(30, 81):
        z = 3 * x - 2 * y + 5
        draw_point(canvas, x, y, z, "red")

# Objeto 3 (amarelo): x = 30 + cos(a) * t, y = 50 + sin(a) * t, z = 10 + t
for t in range(0, 51):
    for a in range(0, 360, 10):  # Variação de 'a' em graus
        a_rad = math.radians(a)  # Converte para radianos
        x = 30 + math.cos(a_rad) * t
        y = 50 + math.sin(a_rad) * t
        z = 10 + t
        draw_point(canvas, x, y, z, "yellow")

# Inicia a janela
janela.mainloop()
