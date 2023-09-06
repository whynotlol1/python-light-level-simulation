import pygame
import math


def main():
    BOUNDS = [500, 500]
    pygame.init()
    screen = pygame.display.set_mode((BOUNDS[0], BOUNDS[1]))
    pygame.display.set_caption("Light level simulation")

    surface_area: list[list[float]] = [[0.0 for _ in range(BOUNDS[0])] for _ in range(BOUNDS[1])]  # [0.0 - 1.0] range

    light_source = {
        "position": {
            "x": 50,
            "y": 50
        },
        "power": 0.1,  # float. [0.1 - 1.0] range
        "speed": 10
    }

    running = True
    while running:

        radius1 = 100 * light_source["power"]
        radius2 = 300 * light_source["power"]
        radius3 = 500 * light_source["power"]
        radius4 = 700 * light_source["power"]

        for x in range(len(surface_area)):
            for y in range(len(surface_area[0])):
                if math.sqrt((x - light_source["position"]["x"]) ** 2 + (y - light_source["position"]["y"]) ** 2) <= radius1:
                    surface_area[x][y] = 1.0
                elif radius2 >= math.sqrt((x - light_source["position"]["x"]) ** 2 + (y - light_source["position"]["y"]) ** 2) > radius1:
                    surface_area[x][y] = 0.75
                elif radius3 >= math.sqrt((x - light_source["position"]["x"]) ** 2 + (y - light_source["position"]["y"]) ** 2) > radius2:
                    surface_area[x][y] = 0.5
                elif radius4 >= math.sqrt((x - light_source["position"]["x"]) ** 2 + (y - light_source["position"]["y"]) ** 2) > radius3:
                    surface_area[x][y] = 0.25
                else:
                    surface_area[x][y] = 0.0

        screen.fill((0, 0, 0))

        for x_pos in range(len(surface_area)):
            for y_pos in range(len(surface_area[0])):
                color = (0, 0, 0)
                match surface_area[x_pos][y_pos]:
                    case 0.0:
                        color = (0, 0, 0)
                    case 0.25:
                        color = (102, 102, 0)
                    case 0.5:
                        color = (153, 153, 0)
                    case 0.75:
                        color = (204, 204, 0)
                    case 1.0:
                        color = (255, 255, 0)

                pygame.draw.rect(screen, color, (x_pos, y_pos, x_pos + 1, y_pos + 1))
        pygame.display.update()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and light_source["position"]["y"] < len(surface_area[0]):
            light_source["position"]["y"] -= light_source["speed"]
        elif keys[pygame.K_DOWN] and light_source["position"]["y"] > 0:
            light_source["position"]["y"] += light_source["speed"]
        elif keys[pygame.K_LEFT] and light_source["position"]["x"] > 0:
            light_source["position"]["x"] -= light_source["speed"]
        elif keys[pygame.K_RIGHT] and light_source["position"]["x"] < len(surface_area):
            light_source["position"]["x"] += light_source["speed"]
        elif keys[pygame.K_EQUALS] and light_source["power"] < 1:
            light_source["power"] += 0.1
        elif keys[pygame.K_MINUS] and light_source["power"] > 0.1:
            light_source["power"] -= 0.1
        elif keys[pygame.K_ESCAPE]:
            pygame.quit()
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False


if __name__ == "__main__":
    main()
