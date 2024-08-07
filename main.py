import datetime
import random
import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Period Quest")

# Load the image (ensure you have a 'player.png' in the same directory)
player_img = pygame.image.load('player.png')

class User:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
        self.health = 100
        self.hygiene_level = 100
        self.happiness = 100
        self.cycle_length = 28  # Default cycle length
        self.last_period_start = None
        self.days_until_next_period = random.randint(1, 28)
        self.points = 0
        self.vouchers = 0

    def display_status(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Hygiene Level: {self.hygiene_level}")
        print(f"Happiness: {self.happiness}")
        print(f"Days until next period: {self.days_until_next_period}")
        print(f"Points: {self.points}")
        print(f"Vouchers: {self.vouchers}")

    def manage_period(self):
        self.days_until_next_period -= 1
        if self.days_until_next_period <= 0:
            print("It's your period!")
            self.days_until_next_period = self.cycle_length
            self.health -= random.randint(10, 20)
            self.hygiene_level -= random.randint(5, 10)
            self.points += 10

    def take_action(self):
        self.health += random.randint(-5, 5)
        self.hygiene_level += random.randint(-5, 5)
        self.happiness += random.randint(-5, 5)
        self.health = max(0, min(self.health, 100))
        self.hygiene_level = max(0, min(self.hygiene_level, 100))
        self.happiness = max(0, min(self.happiness, 100))

class Quest:
    def __init__(self, name, description, difficulty):
        self.name = name
        self.description = description
        self.difficulty = difficulty

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Difficulty: {self.difficulty}")

class PeriodQuest:
    def __init__(self):
        self.users = {}
        self.quests = [
            Quest("Hygiene Quest", "Ensure proper hygiene during your period.", "Easy"),
            Quest("Wellness Quest", "Maintain a healthy lifestyle to alleviate menstrual symptoms.", "Medium"),
            Quest("Advocacy Quest", "Advocate for menstrual equity in your community.", "Hard")
        ]
        self.quiz_questions = {
            "What is the average length of a menstrual cycle?": "28 days",
            "What hormone triggers ovulation?": "Luteinizing hormone",
            "What is the name of the lining shed during menstruation?": "Endometrium"
        }

    def add_user(self, name, birth_date):
        user = User(name, birth_date)
        self.users[name] = user
        print(f"Welcome to Period Quest, {name}!")

    def log_period(self, username, start_date):
        user = self.users.get(username)
        if user:
            user.last_period_start = start_date
            print(f"Period logged for {username} starting on {start_date}")
            user.points += 10
        else:
            print("User not found.")

    def predict_next_period(self, username):
        user = self.users.get(username)
        if user and user.last_period_start:
            next_period = user.last_period_start + datetime.timedelta(days=user.cycle_length)
            print(f"{username}'s next period is predicted to start on {next_period}")
        else:
            print("Not enough data to predict next period.")

    def take_quiz(self, username):
        user = self.users.get(username)
        if user:
            question, answer = random.choice(list(self.quiz_questions.items()))
            print(f"Quiz question: {question}")
            user_answer = input("Your answer: ")
            if user_answer.lower() == answer.lower():
                print("Correct! You earned 5 points.")
                user.points += 5
            else:
                print(f"Incorrect. The correct answer is: {answer}")
        else:
            print("User not found.")

    def award_voucher(self, username):
        user = self.users.get(username)
        if user:
            user.vouchers += 1
            user.points -= 100
            print(f"{username} has earned a voucher! Total vouchers: {user.vouchers}")

    def use_voucher(self, username):
        user = self.users.get(username)
        if user and user.vouchers > 0:
            user.vouchers -= 1
            print(f"{username} has used a voucher. Remaining vouchers: {user.vouchers}")
        else:
            print("No vouchers available.")

    def gift_voucher(self, from_username, to_username):
        from_user = self.users.get(from_username)
        to_user = self.users.get(to_username)
        if from_user and to_user and from_user.vouchers > 0:
            from_user.vouchers -= 1
            to_user.vouchers += 1
            print(f"Voucher gifted anonymously from {from_username} to {to_username}")
        else:
            print("Unable to gift voucher.")

    def display_quests(self):
        print("\nAvailable Quests:")
        for i, quest in enumerate(self.quests, 1):
            print(f"{i}. {quest.name} - {quest.difficulty}")

    def attempt_quest(self, username, quest_index):
        user = self.users.get(username)
        if user and 0 <= quest_index < len(self.quests):
            quest = self.quests[quest_index]
            print(f"\nAttempting {quest.name}...")
            success = random.random() < 0.7  # 70% chance of success
            if success:
                print("Quest completed successfully!")
                user.points += 20
                user.happiness += 10
            else:
                print("Quest failed. Better luck next time!")
                user.happiness -= 5
            user.take_action()
        else:
            print("Invalid user or quest selection.")

def player(x, y):
    screen.blit(player_img, (x, y))

def main():
    app = PeriodQuest()

    # Game initialization
    player_name = input("Enter your name: ")
    birth_date = datetime.date(1990, 1, 1)  # You might want to ask for this
    app.add_user(player_name, birth_date)
    user = app.users[player_name]

    # Player position
    playerX = 370
    playerY = 480

    # Game loop
    running = True
    while running:
        # Fill the screen with a color
        screen.fill((255, 255, 255))  # White background

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX -= 5
                if event.key == pygame.K_RIGHT:
                    playerX += 5

        # Draw the player
        player(playerX, playerY)

        # Update the display
        pygame.display.update()

        # Console-based interaction
        print("\n---- Period Quest ----")
        user.display_status()
        user.manage_period()

        app.display_quests()
        quest_choice = int(input("Choose a quest number (or 0 to continue without quest): "))
        if quest_choice != 0:
            app.attempt_quest(player_name, quest_choice - 1)

        # Check if user can get a voucher
        if user.points >= 100:
            app.award_voucher(player_name)

        # Option to take a quiz
        if input("Do you want to take a quiz? (y/n): ").lower() == 'y':
            app.take_quiz(player_name)

        # Option to use or gift a voucher
        if user.vouchers > 0:
            action = input("Do you want to use or gift a voucher? (use/gift/no): ").lower()
            if action == 'use':
                app.use_voucher(player_name)
            elif action == 'gift':
                recipient = input("Enter the name of the recipient: ")
                app.gift_voucher(player_name, recipient)

    pygame.quit()

if __name__ == "__main__":
    main()
