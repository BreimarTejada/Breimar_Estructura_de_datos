import pygame
import sys

# Configuración inicial
pygame.init()
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Torres de Hanoi - Juego")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
YELLOW = (255, 255, 50)
BLUE = (50, 50, 255)
ORANGE = (255, 165, 0)

# Torres (coordenadas centradas)
towers = [200, 400, 600]
tower_names = ["A", "B", "C"]

# Discos iniciales (ahora solo 5, del más grande "5" al más pequeño "1")
def iniciar_discos():
    discos = []
    for i, color in enumerate([RED, GREEN, YELLOW, BLUE, ORANGE]):
        discos.append({
            "color": color,
            "width": 160 - i * 20,
            "height": 20,
            "x": towers[0] - (160 - i * 20) // 2,
            "y": 430 - i * 20,
            "tower": 0,
            "name": str(5 - i)  # Solo 5 discos
        })
    return discos

discos = iniciar_discos()
selected_disk = None
movements = []
move_count = 0  # Contador de movimientos

def draw_towers_and_disks():
    screen.fill(WHITE)

    # Dibujar base
    pygame.draw.rect(screen, BLACK, (120, 450, 560, 20))

    # Dibujar torres con nombres
    for i, x in enumerate(towers):
        pygame.draw.rect(screen, BLACK, (x, 250, 20, 200))
        font = pygame.font.Font(None, 30)
        text = font.render(tower_names[i], True, BLACK)
        screen.blit(text, (x + 8, 470))  # Etiqueta debajo de la torre

    # Dibujar discos con números
    for disco in discos:
        pygame.draw.rect(screen, disco["color"], (disco["x"], disco["y"], disco["width"], disco["height"]))
        font = pygame.font.Font(None, 20)
        text = font.render(disco["name"], True, BLACK)
        screen.blit(text, (disco["x"] + disco["width"] // 2 - 10, disco["y"] + 2))  # Número centrado

    # Dibujar cuadro de movimientos
    pygame.draw.rect(screen, BLACK, (600, 50, 180, 140))
    font = pygame.font.Font(None, 20)
    screen.blit(font.render("Movimientos:", True, WHITE), (610, 60))
    screen.blit(font.render(f"Total: {move_count}", True, WHITE), (610, 80))  # Siempre visible

    for i, move in enumerate(movements[-5:]):
        screen.blit(font.render(move, True, WHITE), (610, 100 + i * 20))  # Últimos 5 movimientos

    # Dibujar botón "Reiniciar"
    pygame.draw.rect(screen, BLACK, (600, 200, 100, 40))
    screen.blit(font.render("Reiniciar", True, WHITE), (615, 210))

    pygame.display.update()

def animate_move(disco, target_x, target_y, dest_tower, origen_tower, speed=0.4):
    """Animación rápida sin perder control manual"""
    global move_count
    move_count += 1  # Contador de movimientos siempre visible
    while abs(disco["x"] - target_x) > 2 or abs(disco["y"] - target_y) > 2:
        pygame.time.delay(5)
        disco["x"] += (target_x - disco["x"]) * speed
        disco["y"] += (target_y - disco["y"]) * speed
        draw_towers_and_disks()

    # Registrar movimiento en cuadro de movimientos
    movements.append(f"{disco['name']}: {tower_names[origen_tower]} → {tower_names[dest_tower]}")

def resolver_hanoi(n, origen, destino, auxiliar):
    """Ejecutar solución recursiva paso a paso con animación rápida"""
    if n == 1:
        mover_disco(origen, destino, auto=True)
        return
    resolver_hanoi(n - 1, origen, auxiliar, destino)
    mover_disco(origen, destino, auto=True)
    resolver_hanoi(n - 1, auxiliar, destino, origen)

def mover_disco(origen, destino, auto=False):
    """Mueve el disco superior de una torre a otra respetando las reglas"""
    tower_discs = [d for d in discos if d["tower"] == origen]
    if tower_discs:
        disco = tower_discs[-1]
        tower_dest_discs = [d for d in discos if d["tower"] == destino]
        if not tower_dest_discs or tower_dest_discs[-1]["width"] > disco["width"]:  # Validación de tamaño
            target_x = towers[destino] - disco["width"] // 2
            target_y = 430 - len(tower_dest_discs) * 20
            speed = 0.6 if auto else 0.2
            animate_move(disco, target_x, target_y, destino, origen, speed)
            disco["tower"] = destino

def reiniciar_juego():
    """Restablece los discos y borra movimientos"""
    global discos, movements, move_count
    discos = iniciar_discos()
    movements = []
    move_count = 0  # Resetear el contador de movimientos

# Bucle principal
running = True
while running:
    draw_towers_and_disks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 600 <= x <= 700 and 200 <= y <= 240:  # Botón "Reiniciar"
                reiniciar_juego()
            else:
                for disco in reversed(discos):
                    tower_discs = [d for d in discos if d["tower"] == disco["tower"]]
                    if disco == tower_discs[-1]:
                        if disco["x"] <= x <= disco["x"] + disco["width"] and disco["y"] <= y <= disco["y"] + disco["height"]:
                            selected_disk = disco
                            break

        elif event.type == pygame.MOUSEBUTTONUP:
            if selected_disk:
                x, y = event.pos
                for i, tower_x in enumerate(towers):
                    if abs(x - tower_x) < 50:
                        tower_discs = [d for d in discos if d["tower"] == i]
                        smaller_disks = [d for d in tower_discs if d["width"] < selected_disk["width"]]

                        if not tower_discs or not smaller_disks:
                            target_x = tower_x - selected_disk["width"] // 2
                            target_y = 430 - len(tower_discs) * 20
                            animate_move(selected_disk, target_x, target_y, i, selected_disk["tower"], 0.2)  
                            selected_disk["tower"] = i

                selected_disk = None

        elif event.type == pygame.KEYDOWN:  # Presionar "R" para resolver automáticamente con animación rápida
            if event.key == pygame.K_r:
                resolver_hanoi(5, 0, 2, 1)

pygame.quit()
sys.exit()