import tkinter as tk
import math

# Configurações da tela e do Z-buffer
width, height = 800, 600
zbuffer = [[float('inf') for _ in range(width)] for _ in range(height)]

# Definindo vértices dos polígonos conforme a imagem
vertices = {
    'verde1': [[0, 0, 80], [0, 40, 80], [20, 40, 80], [20, 0, 80]],
    'verde2': [[0, 40, 80], [20, 40, 80], [20, 40, 0], [0, 40, 0]],
    'azul': [[20, 0, 80], [20, 40, 80], [100, 40, 0], [100, 0, 0]],
    'amarelo': [[0, 0, 80], [20, 0, 80], [20, 0, 0], [0, 0, 0]],
    'vermelho': [[20, 0, 0], [100, 0, 0], [120, 0, 0], [120, 40, 0]],
    'verde3': [[20, 40, 0], [100, 40, 0], [120, 40, 0], [20, 40, 0]],
    'marron': [[100, 0, 0], [120, 0, 0], [120, 40, 0], [100, 40, 0]]
}
colors = {
    'verde1': 'green', 'verde2': 'darkgreen', 'azul': 'blue',
    'amarelo': 'yellow', 'vermelho': 'red', 'verde3': 'green', 'marron': 'brown'
}


# Função para projeção de coordenadas 3D em 2D
def project(x, y, z):
    fov = 200  # Fator de projeção (zoom)
    x_proj = int(width / 2 + fov * x / (z + fov))
    y_proj = int(height / 2 - fov * y / (z + fov))
    return x_proj, y_proj


# Função para desenhar um polígono com Z-buffer
def draw_polygon(canvas, vertices, color):
    projected_points = []
    for x, y, z in vertices:
        px, py = project(x, y, z)
        projected_points.append((px, py, z))

    # Verifica e desenha se estiver mais próximo no Z-buffer
    for i in range(len(projected_points) - 2):
        px1, py1, z1 = projected_points[i]
        px2, py2, z2 = projected_points[i + 1]
        px3, py3, z3 = projected_points[i + 2]

        # Desenha triângulo
        if all(0 <= px < width and 0 <= py < height for px, py, _ in
               [projected_points[i], projected_points[i + 1], projected_points[i + 2]]):
            avg_z = (z1 + z2 + z3) / 3
            if avg_z < min(zbuffer[py1][px1], zbuffer[py2][px2], zbuffer[py3][px3]):
                canvas.create_polygon([px1, py1, px2, py2, px3, py3], fill=color)
                zbuffer[py1][px1] = zbuffer[py2][px2] = zbuffer[py3][px3] = avg_z


# Função para aplicar rotação
def rotate(vertices, angle_x, angle_y, angle_z):
    new_vertices = []
    for x, y, z in vertices:
        # Rotação em X
        y, z = y * math.cos(angle_x) - z * math.sin(angle_x), y * math.sin(angle_x) + z * math.cos(angle_x)
        # Rotação em Y
        x, z = x * math.cos(angle_y) + z * math.sin(angle_y), -x * math.sin(angle_y) + z * math.cos(angle_y)
        # Rotação em Z
        x, y = x * math.cos(angle_z) - y * math.sin(angle_z), x * math.sin(angle_z) + y * math.cos(angle_z)
        new_vertices.append((x, y, z))
    return new_vertices


# Configuração da janela Tkinter
janela = tk.Tk()
janela.title("Superfícies Bilineares com Z-Buffer")
canvas = tk.Canvas(janela, width=width, height=height, bg="white")
canvas.pack()


# Função para renderizar as superfícies com rotação
def render(angle_x=0, angle_y=0, angle_z=0):
    canvas.delete("all")
    for y in range(height):
        for x in range(width):
            zbuffer[y][x] = float('inf')
    for face, verts in vertices.items():
        rotated_verts = rotate(verts, angle_x, angle_y, angle_z)
        draw_polygon(canvas, rotated_verts, colors[face])


# Função para atualizar a rotação e redesenhar
def update_rotation():
    angle_x = math.radians(10)  # Incremento de 10 graus
    angle_y = math.radians(10)
    angle_z = math.radians(10)
    render(angle_x, angle_y, angle_z)
    janela.after(10, update_rotation)


# Inicia a rotação
update_rotation()
janela.mainloop()
