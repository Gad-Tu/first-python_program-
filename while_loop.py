#This program show how to play the game of guessing.
secret_number = 77
guess_count = 0

while guess_count < 3:
    guess = int(input("Enter number: "))
    guess_count += 1
    if guess != secret_number:
        print("Ha ha! you're stuck in my loop.")
    if guess == secret_number:
        print(" well done, muggle! You are free now.")
        break
print("Good byee!")

#car game
car_game = ""
while True:
    car_game = input(">").lower()
    if car_game == "start":
        print(" car started")
    elif car_game == "stopped":
        print("car stopped")
    elif car_game == "helps":
        print("""
        start: to start the car 
        stop: to stop the car 
        quit : to exit the game
        """)
    elif car_game == "quit"
    break
    else:
        print("Hey, we don't understand this.")
