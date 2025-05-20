import pygame
import sys
import random

# Inicialización de pygame
pygame.init()
ANCHO, ALTO = 1200, 1000
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("MathQuest - Menú Principal")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (50, 100, 255)
GRIS = (200, 200, 200)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
CYAN = (0, 255, 255)

# Fuente
fuente_titulo = pygame.font.SysFont("comicsansms", 70, bold=True)
fuente_pregunta = pygame.font.SysFont("arial", 50)
fuente_respuesta = pygame.font.SysFont("verdana", 45, italic=True)
fuente_mensaje = pygame.font.SysFont("calibri", 60)
fuente_creditos = pygame.font.SysFont("timesnewroman", 35)
fuente = pygame.font.SysFont("arial", 40)

# Puntos
puntos = 0
puntaje_maximo = 100

# Botones
botones = [
    {"texto": "1. Iniciar Juego", "rect": pygame.Rect(250, 200, 300, 60)},
    {"texto": "2. Créditos - Nombres ", "rect": pygame.Rect(250, 300, 350, 60)},
    {"texto": "3. Salir", "rect": pygame.Rect(250, 400, 300, 60)}
]

def mostrar_puntos():
    texto_puntos = fuente.render("Puntos: " + str(puntos), True, ROJO)
    VENTANA.blit(texto_puntos, (ANCHO - texto_puntos.get_width() - 30, 20))
    if puntos >= puntaje_maximo:
        fin_juego()

def mostrar_mensaje_error(mensaje):
    texto_error = fuente.render(mensaje, True, ROJO)
    VENTANA.blit(texto_error, (ANCHO // 2 - texto_error.get_width() // 2, 500))
    pygame.display.flip()
    pygame.time.delay(2000)

def dibujar_menu():
    VENTANA.fill(BLANCO)
    titulo = fuente_titulo.render("MathQuest", True, ROJO)
    VENTANA.blit(titulo, (ANCHO//2 - titulo.get_width()//2, 80))
    for boton in botones:
        pygame.draw.rect(VENTANA, GRIS, boton["rect"])
        texto_render = fuente.render(boton["texto"], True, BLANCO)
        VENTANA.blit(texto_render, (boton["rect"].x + 20, boton["rect"].y + 10))
    pygame.display.flip()

def mostrar_creditos():
    VENTANA.fill(GRIS)
    creditos = [
        "Desarrollado por:",
        "  - Isaac Cárdenas",
        "  - Neizer Montero",
        "  - Diego Ortega",
        "  - Rai Villavicencio",
        "", "Basado en pygame", "",
        "Juego educativo en Python que combina aventura y",
        "resolución de problemas matemáticos.",
        "", "El objetivo principal del proyecto es mejorar",
        "las habilidades matemáticas de los usuarios",
        "a través de desafíos progresivos y entretenidos.",
        "", " ¡Disfruta!",
    ]
    line_height = 45
    start_y = 60
    for i, linea in enumerate(creditos):
        texto = fuente_creditos.render(linea, True, BLANCO)
        VENTANA.blit(texto, (ANCHO//2 - texto.get_width()//2, start_y + i * line_height))
    y_final = start_y + len(creditos) * line_height + 30
    texto_volver = fuente.render("Presiona cualquier tecla para volver", True, ROJO)
    VENTANA.blit(texto_volver, (ANCHO//2 - texto_volver.get_width()//2, y_final))
    pygame.display.flip()
    esperar_tecla()

def esperar_tecla():
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                esperando = False

def nivel_1():
    global puntos
    VENTANA.fill(BLANCO)
    historia = [
        "Nivel 1: El Bosque Matemágico",
        "Te has perdido entre árboles encantados.",
        "Para abrir el camino",
        "resuelve este acertijo numérico."
    ]
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    operador = random.choice(['+', '-'])
    resultado = a + b if operador == '+' else a - b
    pregunta = "Cuánto es " + str(a) + " " + operador + " " + str(b) + "?"
    respuesta = ""
    escribiendo = True
    while escribiendo:
        VENTANA.fill(BLANCO)
        mostrar_puntos()
        for i, linea in enumerate(historia):
            texto = fuente_mensaje.render(linea, True, AZUL)
            VENTANA.blit(texto, (ANCHO//2 - texto.get_width()//2, 100 + i * 50))
        texto_pregunta = fuente_pregunta.render(pregunta, True, NEGRO)
        VENTANA.blit(texto_pregunta, (ANCHO//2 - texto_pregunta.get_width()//2, 300))
        texto_resp = fuente_respuesta.render("Respuesta: " + respuesta, True, VERDE)
        VENTANA.blit(texto_resp, (ANCHO//2 - texto_resp.get_width()//2, 400))
        pygame.display.flip()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    if respuesta.lstrip('-').isdigit() and int(respuesta) == resultado:
                        puntos += 10
                        return nivel_2()
                    else:
                        mostrar_mensaje_error("Error. Revisa tus cálculos y vuelve a intentarlo.")
                        return nivel_1()
                elif evento.key == pygame.K_BACKSPACE:
                    respuesta = respuesta[:-1]
                elif evento.unicode.isdigit() or evento.unicode == "-":
                    respuesta += evento.unicode

def nivel_2():
    global puntos
    VENTANA.fill(BLANCO)
    historia = [
        "Nivel 2: Multiplicación y División",
        "Has llegado a la Ciudad Numérica",
        "Ayuda resolviendo el reto."
    ]
    operador = random.choice(['*', '/'])
    if operador == '*':
        a = random.randint(2, 10)
        b = random.randint(2, 10)
        resultado = a * b
    else:
        b = random.randint(2, 10)
        resultado = random.randint(2, 10)
        a = b * resultado
    pregunta = "Cuánto es " + str(a) + " " + operador + " " + str(b) + "?"
    respuesta = ""
    escribiendo = True
    while escribiendo:
        VENTANA.fill(BLANCO)
        mostrar_puntos()
        for i, linea in enumerate(historia):
            texto = fuente_mensaje.render(linea, True, AZUL)
            VENTANA.blit(texto, (ANCHO//2 - texto.get_width()//2, 100 + i * 50))
        texto_pregunta = fuente_pregunta.render(pregunta, True, NEGRO)
        VENTANA.blit(texto_pregunta, (ANCHO//2 - texto_pregunta.get_width()//2, 300))
        texto_resp = fuente_respuesta.render("Respuesta: " + respuesta, True, CYAN)
        VENTANA.blit(texto_resp, (ANCHO//2 - texto_resp.get_width()//2, 400))
        pygame.display.flip()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    if respuesta.isdigit() and int(respuesta) == resultado:
                        puntos += 15
                        return nivel_3()
                    else:
                        mostrar_mensaje_error("Cuidado. Revisa bien la operación.")
                        return nivel_2()
                elif evento.key == pygame.K_BACKSPACE:
                    respuesta = respuesta[:-1]
                elif evento.unicode.isdigit():
                    respuesta += evento.unicode

def nivel_3():
    global puntos
    VENTANA.fill(BLANCO)
    historia = [
        "Nivel 3: Lógica básica",
        "El sabio del templo te hace una pregunta..."
    ]
    num = random.randint(1, 100)
    es_par = num % 2 == 0
    pregunta = "El número " + str(num) + " es par? (Si/No)"
    respuesta = ""
    escribiendo = True
    while escribiendo:
        VENTANA.fill(BLANCO)
        mostrar_puntos()
        for i, linea in enumerate(historia):
            texto = fuente_mensaje.render(linea, True, AZUL)
            VENTANA.blit(texto, (ANCHO//2 - texto.get_width()//2, 100 + i * 50))
        texto_pregunta = fuente_pregunta.render(pregunta, True, NEGRO)
        VENTANA.blit(texto_pregunta, (ANCHO//2 - texto_pregunta.get_width()//2, 300))
        texto_resp = fuente_respuesta.render("Respuesta: " + respuesta, True, CYAN)
        VENTANA.blit(texto_resp, (ANCHO//2 - texto_resp.get_width()//2, 400))
        pygame.display.flip()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    if (respuesta.lower() in ['s', 'si'] and es_par) or (respuesta.lower() in ['n', 'no'] and not es_par):
                        puntos += 20
                        if puntos >= puntaje_maximo:
                            return fin_juego()
                        else:
                            return nivel_1()
                    else:
                        mostrar_mensaje_error("Reflexiona. ¿Es par o impar?")
                        return nivel_3()
                elif evento.key == pygame.K_BACKSPACE:
                    respuesta = respuesta[:-1]
                elif evento.unicode.isalpha():
                    respuesta += evento.unicode.lower()

def fin_juego():
    VENTANA.fill(BLANCO)
    mensaje = "¡Has alcanzado el puntaje máximo!"
    texto1 = fuente_titulo.render(mensaje, True, VERDE)
    texto2 = fuente_mensaje.render("Puntaje final: " + str(puntos), True, AZUL)
    centro_y = ALTO // 2
    VENTANA.blit(texto1, (ANCHO // 2 - texto1.get_width() // 2, centro_y - 80))
    VENTANA.blit(texto2, (ANCHO // 2 - texto2.get_width() // 2, centro_y + 40))
    pygame.display.flip()
    pygame.time.delay(4000)

def main():
    while True:
        dibujar_menu()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                for i, boton in enumerate(botones):
                    if boton["rect"].collidepoint(x, y):
                        if i == 0:
                            nivel_1()
                        elif i == 1:
                            mostrar_creditos()
                        elif i == 2:
                            pygame.quit()
                            sys.exit()

if __name__ == "__main__":
    main()
