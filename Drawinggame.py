import pygame
import math

# Set the dimensions of the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Set colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND_COLORS = [(255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Add more colors as desired

def draw_mandala():
    pygame.init()

    # Create the window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Symmetrical Mandala Drawing")

    # Create a drawing surface
    drawing_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    drawing_surface.fill(WHITE)

    # Initialize variables
    is_drawing = False
    last_pos = None

    # Initialize colors
    drawing_color = BLACK
    background_color_index = 0
    background_color = BACKGROUND_COLORS[background_color_index]

    # Initialize patterns
    patterns = [draw_radial_symmetry, draw_kaleidoscope, draw_kaleidoscope_radial_symmetry]
    current_pattern_index = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # Check mouse events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    is_drawing = True
                    last_pos = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    is_drawing = False
            elif event.type == pygame.MOUSEMOTION:
                if is_drawing:
                    current_pos = pygame.mouse.get_pos()
                    patterns[current_pattern_index](drawing_surface, drawing_color, last_pos, current_pos)
                    last_pos = current_pos

            # Check key events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:  # Change drawing color
                    drawing_color = get_next_color(drawing_color)
                elif event.key == pygame.K_b:  # Change background color
                    background_color_index = (background_color_index + 1) % len(BACKGROUND_COLORS)
                    background_color = BACKGROUND_COLORS[background_color_index]
                    drawing_surface.fill(background_color)
                elif event.key == pygame.K_p:  # Change pattern
                    current_pattern_index = (current_pattern_index + 1) % len(patterns)

        # Draw the drawing surface on the window
        window.fill(background_color)
        window.blit(drawing_surface, (0, 0))

        pygame.display.update()

def mirror_pos(position):
    center_x = WINDOW_WIDTH // 2
    center_y = WINDOW_HEIGHT // 2

    mirrored_x = center_x - (position[0] - center_x)
    mirrored_y = position[1]

    return (mirrored_x, mirrored_y)

def get_next_color(current_color):
    colors = [BLACK, (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]  # Add more colors as desired
    current_index = colors.index(current_color)
    next_index = (current_index + 1) % len(colors)
    return colors[next_index]

def draw_kaleidoscope_radial_symmetry(surface, color, start_pos, end_pos):
    for angle in range(0, 360, 30):
        rotated_start = rotate_point(start_pos, angle)
        rotated_end = rotate_point(end_pos, angle)
        pygame.draw.line(surface, color, rotated_start, rotated_end, 2)
        pygame.draw.line(surface, color, mirror_pos(rotated_start), mirror_pos(rotated_end), 2)

def draw_radial_symmetry(surface, color, start_pos, end_pos):
    pygame.draw.line(surface, color, start_pos, end_pos, 2)
    pygame.draw.line(surface, color, mirror_pos(start_pos), mirror_pos(end_pos), 2)

def draw_kaleidoscope(surface, color, start_pos, end_pos):
    for angle in range(0, 360, 30):
        rotated_start = rotate_point(start_pos, angle)
        rotated_end = rotate_point(end_pos, angle)
        pygame.draw.line(surface, color, rotated_start, rotated_end, 2)

def rotate_point(point, angle):
    angle_rad = math.radians(angle)
    x = point[0]
    y = point[1]
    rotated_x = x * math.cos(angle_rad) - y * math.sin(angle_rad)
    rotated_y = x * math.sin(angle_rad) + y * math.cos(angle_rad)
    return (int(rotated_x), int(rotated_y))
def main():
    print("Welcome to the Symmetrical Mandala Drawing Game!")
    draw_mandala()

if __name__ == "__main__":
    main()
