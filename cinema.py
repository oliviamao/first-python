films = {
    "Harry Potter":[3, 5],
    "The Avengers":[18, 5],
    "Interstellar":[15,5],
    "Forrest Gump ":[12,5],
    }

while True:
    
    choice = input("What film would you like to watch?: ").strip().title()

    if choice in films:

        # check user age
        
       age = int(input("How old are you?:" ).strip())
       if age >= films[choice][0]:

           # check enough seats

           num_seats = films[choice][1]

           if num_seats>0:
               films[choice][1] = films[choice][1] - 1
               print("Enjoy the film!")
           else:
               print("Sorry, we are sold out!")
           
       else:
           print("You are too young to see that film!")
           
    else:
        print("We don't have that film...")
        
    
