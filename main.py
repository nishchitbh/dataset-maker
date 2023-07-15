import pygame
import json

window_width = 800
window_height = 600
units_per_division = 5  # Number of units per grid division
grid_size = 10 * units_per_division  # Adjusted grid size based on units per division

pygame.init()
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Dataset Maker")

origin_x = window_width // 2  # X-coordinate of the origin
origin_y = window_height // 2  # Y-coordinate of the origin

clicked_points = {}  # Dictionary to store the clicked points
color_options = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "magenta": (255, 0, 255),
    "cyan": (0, 255, 255)
}
current_color = "red"  # Currently selected color

font = pygame.font.Font(None, 16)  # Font for the scale

running = True
clock = pygame.time.Clock()

# Load clicked points from the JSON file if it exists
try:
    with open("dataset.json", "r") as file:
        clicked_points = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    clicked_points = {}

def draw_scale():
    scale_text = "One smallest division = {} units along both axes".format(units_per_division)
    scale_surface = font.render(scale_text, True, (0, 0, 0))
    scale_rect = scale_surface.get_rect(bottomleft=(grid_size, window_height - grid_size))
    window.blit(scale_surface, scale_rect)

def adjust_grid_size():
    global grid_size
    grid_size = 5 * units_per_division

while running:
    clock.tick(60)  # Limit frame rate to 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button clicked
                # Get the mouse position
                mouse_pos = pygame.mouse.get_pos()

                # Check if the grid area was clicked
                if mouse_pos[0] <= window_width - grid_size and mouse_pos[1] <= window_height - grid_size:
                    # Adjust the coordinates to start from the origin
                    adjusted_x = (mouse_pos[0] - origin_x) // units_per_division
                    adjusted_y = (origin_y - mouse_pos[1]) // units_per_division

                    # Check if the clicked point is already highlighted
                    if hovered_point:
                        if current_color in clicked_points and hovered_point in clicked_points[current_color]:
                            # Remove the point from clicked_points
                            clicked_points[current_color].remove(hovered_point)
                            # Delete the color key if it has no points left
                            if not clicked_points[current_color]:
                                del clicked_points[current_color]
                            # Remove the point from the JSON file
                            with open("dataset.json", "w") as file:
                                json.dump(clicked_points, file)
                        hovered_point = None
                    else:
                        # Save the adjusted coordinates with the selected color
                        if current_color not in clicked_points:
                            clicked_points[current_color] = []
                        clicked_points[current_color].append([adjusted_x, adjusted_y])
                        # Write the clicked points to the JSON file
                        with open("dataset.json", "w") as file:
                            json.dump(clicked_points, file)

                # Check if the color options area was clicked
                elif window_height - grid_size <= mouse_pos[1] <= window_height:
                    color_index = (mouse_pos[0] // grid_size) % len(color_options)
                    current_color = list(color_options.keys())[color_index]

    # Get the mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Check if the mouse is hovering over a clicked point
    hovered_point = None
    for color, points in clicked_points.items():
        for point in points:
            screen_x = origin_x + point[0] * units_per_division
            screen_y = origin_y - point[1] * units_per_division
            if screen_x - 3 <= mouse_pos[0] <= screen_x + 3 and screen_y - 3 <= mouse_pos[1] <= screen_y + 3:
                hovered_point = point
                break
        if hovered_point:
            break

    # Clear the screen
    window.fill((255, 255, 255))

    # Draw vertical grid lines
    for x in range(0, window_width, grid_size):
        pygame.draw.line(window, (200, 200, 200), (x, 0), (x, window_height - grid_size))

    # Draw horizontal grid lines
    for y in range(0, window_height - grid_size, grid_size):
        pygame.draw.line(window, (200, 200, 200), (0, y), (window_width, y))

    # Draw the origin point
    pygame.draw.circle(window, (255, 0, 0), (origin_x, origin_y), 5)

    # Draw the x and y axes
    pygame.draw.line(window, (0, 0, 255), (0, origin_y), (window_width, origin_y))
    pygame.draw.line(window, (0, 0, 255), (origin_x, 0), (origin_x, window_height - grid_size))

    # Draw circles at the clicked points with selected colors
    for color, points in clicked_points.items():
        for point in points:
            screen_x = origin_x + point[0] * units_per_division
            screen_y = origin_y - point[1] * units_per_division
            if point == hovered_point:
                # Highlight the hovered point with a larger circle
                pygame.draw.circle(window, color_options[color], (screen_x, screen_y), 5)
            else:
                pygame.draw.circle(window, color_options[color], (screen_x, screen_y), 3)

    # Draw the color options
    for i, (color, rgb) in enumerate(color_options.items()):
        rect = pygame.Rect(i * grid_size, window_height - grid_size, grid_size, grid_size)
        pygame.draw.rect(window, rgb, rect)

        # Draw a border around the currently selected color
        if color == current_color:
            pygame.draw.rect(window, (0, 0, 0), rect, 3)

    draw_scale()  # Call draw_scale to display the scale

    pygame.display.flip()

pygame.quit()
