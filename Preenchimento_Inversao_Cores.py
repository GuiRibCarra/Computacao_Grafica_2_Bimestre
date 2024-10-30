import tkinter as tk


# Função para criar o bounding box
def bounding_box(pontos):
    x_min = min(p[0] for p in pontos)
    x_max = max(p[0] for p in pontos)
    y_min = min(p[1] for p in pontos)
    y_max = max(p[1] for p in pontos)
    return (x_min, y_min, x_max, y_max)


# Função para inverter a cor
def inverte_cor(cor):
    r = 255 - int(cor[1:3], 16)
    g = 255 - int(cor[3:5], 16)
    b = 255 - int(cor[5:7], 16)
    return f'#{r:02x}{g:02x}{b:02x}'


# Função para desenhar e inverter a cor do polígono
def desenha_e_inverte_poligono(canvas, pontos, cor_poligono):
    # Desenha o polígono
    poly = canvas.create_polygon(pontos, outline='black', fill=cor_poligono, tags="poly")

    # Calcula o bounding box
    x_min, y_min, x_max, y_max = bounding_box(pontos)
    canvas.create_rectangle(x_min, y_min, x_max, y_max, outline="blue")

    # Inicia a inversão de cor dentro do bounding box
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            # Verifica se o ponto está dentro do polígono
            if canvas.find_overlapping(x, y, x, y) and "poly" in canvas.gettags(canvas.find_closest(x, y)):
                # Inverte a cor do pixel
                cor_atual = canvas.itemcget(poly, "fill")
                cor_invertida = inverte_cor(cor_atual)
                canvas.itemconfig(poly, fill=cor_invertida)


# Configuração da janela
janela = tk.Tk()
janela.title("Inversão de Cor com Bounding Box")
canvas = tk.Canvas(janela, width=400, height=400)
canvas.pack()

# Pontos do polígono
pontos_poligono = [(50, 50), (300, 100), (250, 300), (100, 250)]

# Desenha e inverte a cor do polígono
desenha_e_inverte_poligono(canvas, pontos_poligono, "#ff0000")

# Inicia a janela
janela.mainloop()
