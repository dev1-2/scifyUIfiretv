import pygame
import sys
import time
import random
import threading
import math  # Standard math module

# Initialize pygame
pygame.init()

# Set up the display
screen_info = pygame.display.Info()
WIDTH, HEIGHT = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("System Initialization")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 100, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Fonts
small_font = pygame.font.SysFont('consolas', 16)
medium_font = pygame.font.SysFont('consolas', 24)
large_font = pygame.font.SysFont('consolas', 36)

# System messages
system_messages = [
    "Initializing system core...",
    "Loading neural network modules...",
    "Connecting to quantum database...",
    "Establishing secure connection...",
    "Verifying system integrity...",
    "Loading AI subsystems...",
    "Scanning network topology...",
    "Analyzing available resources...",
    "Initializing holographic interface...",
    "Calibrating quantum processors...",
    "Loading encryption protocols...",
    "Establishing satellite uplink...",
    "Synchronizing with global network...",
    "Initializing defense systems...",
    "Loading user profiles...",
    "Scanning for security threats...",
    "Initializing virtual environment...",
    "Loading language modules...",
    "Establishing neural interface...",
    "Analyzing system compatibility...",
    "Verifying network security...",
    "Loading advanced algorithms...",
    "Initializing quantum encryption...",
    "Scanning for hardware conflicts...",
    "Establishing secure protocols...",
    "Loading system drivers...",
    "Initializing memory management...",
    "Scanning for system vulnerabilities...",
    "Loading interface protocols...",
    "Initializing system diagnostics..."
]

# Progress variables
displayed_messages = []
progress = 0
start_time = time.time()
total_runtime = 600  # 10 minutes in seconds

# Hexagon grid for background
hexagons = []
for x in range(0, WIDTH + 100, 100):
    for y in range(0, HEIGHT + 100, 100):
        if (x // 100) % 2 == 0:
            hexagons.append((x, y))
        else:
            hexagons.append((x, y + 50))

# Function to draw a hexagon
def draw_hexagon(surface, color, center, size):
    points = []
    for i in range(6):
        angle_deg = 60 * i - 30
        angle_rad = math.pi / 180 * angle_deg
        point = (center[0] + size * math.cos(angle_rad),
                 center[1] + size * math.sin(angle_rad))
        points.append(point)
    pygame.draw.polygon(surface, color, points, 1)

# Function to add a new message
def add_message():
    global displayed_messages, running
    if system_messages and running:
        message = system_messages.pop(random.randint(0, len(system_messages)-1))
        displayed_messages.append({"text": message, "time": time.time()})
        if running:  # Check again to avoid creating threads after shutdown
            threading.Timer(random.uniform(1.0, 3.0), add_message).start()

# Main loop
running = True
clock = pygame.time.Clock()

# Start adding messages
threading.Timer(2.0, add_message).start()

try:
    while running:
        current_time = time.time()
        elapsed_time = current_time - start_time
        
        # Calculate progress
        progress = min(elapsed_time / total_runtime, 1.0)
        
        # Check if we've reached the end
        if elapsed_time >= total_runtime:
            # Show failure message and exit after a delay
            screen.fill(BLACK)
            
            # Draw red warning hexagons
            for center in hexagons:
                draw_hexagon(screen, RED, center, 40)
            
            fail_text1 = large_font.render("SYSTEM INITIALIZATION FAILED", True, RED)
            fail_text2 = medium_font.render("Network incompatibility detected", True, RED)
            fail_text3 = medium_font.render("System shutdown initiated...", True, RED)
            
            screen.blit(fail_text1, (WIDTH//2 - fail_text1.get_width()//2, HEIGHT//2 - 50))
            screen.blit(fail_text2, (WIDTH//2 - fail_text2.get_width()//2, HEIGHT//2 + 20))
            screen.blit(fail_text3, (WIDTH//2 - fail_text3.get_width()//2, HEIGHT//2 + 60))
            
            pygame.display.flip()
            time.sleep(5)
            running = False
            break
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # Clear the screen
        screen.fill(BLACK)
        
        # Draw hexagon grid
        for center in hexagons:
            color_intensity = int(100 + 155 * (0.5 + math.sin(current_time + center[0] * 0.01) * 0.5))
            color = (0, color_intensity // 3, color_intensity)
            draw_hexagon(screen, color, center, 40)
        
        # Draw title
        title = large_font.render("ADVANCED SYSTEM INITIALIZATION", True, BLUE)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 50))
        
        # Draw progress bar
        bar_width = WIDTH - 200
        pygame.draw.rect(screen, WHITE, (100, HEIGHT - 100, bar_width, 30), 1)
        pygame.draw.rect(screen, BLUE, (100, HEIGHT - 100, int(bar_width * progress), 30))
        
        # Draw progress percentage
        progress_text = medium_font.render(f"{int(progress * 100)}%", True, WHITE)
        screen.blit(progress_text, (WIDTH//2 - progress_text.get_width()//2, HEIGHT - 95))
        
        # Draw system messages
        y_offset = 150
        for i, msg in enumerate(displayed_messages[-15:]):  # Show only the last 15 messages
            age = current_time - msg["time"]
            if age < 5:  # Messages fade after 5 seconds
                alpha = 255 if age < 3 else int(255 * (5 - age) / 2)
                text_surface = small_font.render(msg["text"], True, (0, min(255, int(200 + 55 * math.sin(current_time * 2))), 0))
                text_surface.set_alpha(alpha)
                screen.blit(text_surface, (150, y_offset))
                y_offset += 25
        
        # Draw time elapsed
        time_text = medium_font.render(f"Time Elapsed: {int(elapsed_time // 60):02d}:{int(elapsed_time % 60):02d}", True, WHITE)
        screen.blit(time_text, (WIDTH - time_text.get_width() - 50, 50))
        
        # Update the display
        pygame.display.flip()
        
        # Cap the frame rate
        clock.tick(30)
finally:
    # Make sure running is set to False to stop any new threads
    running = False
    # Quit pygame
    pygame.quit()
    sys.exit()
