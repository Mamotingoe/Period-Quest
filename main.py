import random
import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the game window
screen = pygame.display.set_mode((800, 600))

# Load the image
player_img = pygame.image.load('player.png')

# Function to draw the player
def player(x, y):
    screen.blit(player_img, (x, y))

# Player position
playerX = 370
playerY = 480

class Player:
    def __init__(self, name, health, hygiene_level, happiness, days_until_next_period):
        self.name = name
        self.health = health
        self.hygiene_level = hygiene_level
        self.happiness = happiness
        self.days_until_next_period = days_until_next_period

    def display_status(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Hygiene Level: {self.hygiene_level}")
        print(f"Happiness: {self.happiness}")
        print(f"Days until next period: {self.days_until_next_period}")

    def manage_period(self):
        self.days_until_next_period -= 1
        if self.days_until_next_period <= 0:
            print("It's your period!")
            self.days_until_next_period = self.menstrual_cycle
            self.health -= random.randint(10, 20)
            self.hygiene_level -= random.randint(5, 10)

    def take_action(self):
        self.health += random.randint(-5, 5)
        self.hygiene_level += random.randint(-5, 5)
        self.happiness += random.randint(-5, 5)

class Quest:
    def __init__(self, name, description, difficulty):
        self.name = name
        self.description = description
        self.difficulty = difficulty

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Difficulty: {self.difficulty}")

# Sample quests
quests = [
    Quest("Hygiene Quest", "Ensure proper hygiene during your period.", "Easy"),
    Quest("Wellness Quest", "Maintain a healthy lifestyle to alleviate menstrual symptoms.", "Medium"),
    Quest("Advocacy Quest", "Advocate for menstrual equity in your community.", "Hard")
]
# Game loop
running = True
while running:
    # Fill the screen with a color
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed, check whether it's right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left arrow key pressed")
            if event.key == pygame.K_RIGHT:
                print("Right arrow key pressed")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Keystroke has been released")

    # Draw the player
    player(playerX, playerY)

    # Update the display
    pygame.display.update()
# Game loop
# player_name = input("Enter your name: ")
# player = Player(player_name, 100, 100, 100, 28)

# Game loop
# running = True
# while running:
    # Fill the screen with a color
   # screen.fill((0, 0, 0))

    #for event in pygame.event.get():
      #  if event.type == pygame.QUIT:
            #running = False


#while True:
    #print("\n---- Period Quest ----")
   # player.display_status()

    # Manage player's period
    player.manage_period()

    # Take player action
    player.take_action()

    # Display available quests
    print("\nAvailable Quests:")
    for i, quest in enumerate(quests, 1):
        print(f"{i}. {quest.name} - {quest.difficulty}")

    # Player selects a quest
    quest_choice = int(input("Choose a quest number (or 0 to continue without quest): "))
    if quest_choice == 0:
        continue

    # Player attempts the selected quest
    selected_quest = quests[quest_choice - 1]
    print(f"\nAttempting {selected_quest.name}...")
    # Logic to handle quest completion or failure

    # Update player's status based on quest outcome
    # Update player's completed quests list

    input("\nPress Enter to continue...")  # Pause for readability
