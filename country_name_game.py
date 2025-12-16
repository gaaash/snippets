import random
country_names=["Chile","China","Egypt","India","Italy","Japan","Kenya","Libya","Qatar","Spain","Yemen","Benin","Malta","Niger","Sudan","Togo","Samoa","Haiti","Laos","Palau"]

goal = random.choice(country_names)
number_of_empyt_spots= len(goal)-1
q = True
hint = True
empty_spot  = " _ "
number_of_faileds = 0
menu = '''
1> Start game
2> Score
3> Quit

'''
print(menu)

def show_game(hint=False):
    if hint:
    
        print(f"{goal[0]}",f"{goal[1]}",f"{empty_spot}"*(number_of_empyt_spots-1))    

    else:
        print(f"{goal[0]}",f"{empty_spot}"*number_of_empyt_spots)

while q == True:
    
    vorodi = input("> ")
    match vorodi:
        case "1":
            show_game()
            user_input= input("> ")
            if user_input == goal:
                print("Correct")
                q= False
            else:
                print("NOPE, Here is a hint")
                show_game(hint)
        case "2":
            pass
        case "3":
            q=False


        



