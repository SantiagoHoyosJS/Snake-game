import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Load the image that will be used as a tile
tile_image = pygame.image.load('tile.png')

# Get the dimensions of the tile image
tile_width, tile_height = tile_image.get_size()

# Calculate the number of tiles needed to fill the screen
num_tiles_x = screen_width // tile_width + 1
num_tiles_y = screen_height // tile_height + 1

# Tile the image across the screen
for y in range(num_tiles_y):
    for x in range(num_tiles_x):
        screen.blit(tile_image, (x * tile_width, y * tile_height))

# Update the screen
pygame.display.flip()

# Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()