#
#
#
#

print("Loading library's...")


colorama = None
import os
import time
warn = ""
try:
    import colorama
except:
    warn = "Warn >> Could not import colorama, is it installed?"
thef1 = open(f"{os.getcwd()}\\data.sco", "a+")
thef1.close()
thef = open(f"{os.getcwd()}\\data.sco", "r+")
highscore = str(thef.readlines()).replace("[", "").replace("]", "").replace("'", "")
print(highscore)
if highscore == "":
    highscore = "None"

print(f"{colorama.Fore.YELLOW}Defining variables...{colorama.Fore.RESET}")

size = os.get_terminal_size()

columns = size.columns
lines = size.lines

Fore = colorama.Fore

print("-" * int(columns))

grid = [2, 2, 2, 2, 2, 2, 2, 2, 2] # Grid

cwd = os.getcwd()

def check(grid):
    grid = [
    str(grid[0]).replace("1", "X").replace("0", "O").replace("2", " "),
    str(grid[1]).replace("1", "X").replace("0", "O").replace("2", " "),
    str(grid[2]).replace("1", "X").replace("0", "O").replace("2", " "),
    str(grid[3]).replace("1", "X").replace("0", "O").replace("2", " "),
    str(grid[4]).replace("1", "X").replace("0", "O").replace("2", " "),
    str(grid[5]).replace("1", "X").replace("0", "O").replace("2", " "),
    str(grid[6]).replace("1", "X").replace("0", "O").replace("2", " "),
    str(grid[7]).replace("1", "X").replace("0", "O").replace("2", " "),
    str(grid[8]).replace("1", "X").replace("0", "O").replace("2", " ")
    ]

    if grid[0] + grid[1] + grid[2] == "XXX" or grid[0] + grid[1] + grid[2] == "OOO":
        print(str(grid[0]) + str(str(grid[1])) + str(grid[2]))
        return True
    if grid[3] + grid[4] + grid[5] == "XXX" or grid[3] + grid[4] + grid[5] ==  "OOO":
        print(str(grid[3]) + str(str(grid[4])) + str(grid[5]))
        return True
    if grid[6] + grid[7] + grid[8] == "XXX" or grid[6] + grid[7] + grid[8] ==  "OOO":
        print(str(grid[6]) + str(str(grid[7])) + str(grid[8]))
        return True
    if grid[0] + grid[3] + grid[6] == "XXX" or grid[0] + grid[3] + grid[6] ==  "OOO":
        print(str(grid[0]) + str(str(grid[3])) + str(grid[6]))
        return True
    if grid[1] + grid[4] + grid[7] == "XXX" or grid[1] + grid[4] + grid[7] ==  "OOO":
        print(str(grid[1]) + str(str(grid[4])) + str(grid[7]))
        return True
    if grid[2] + grid[5] + grid[8] == "XXX" or grid[2] + grid[5] + grid[8] ==  "OOO":
        print(str(grid[2]) + str(str(grid[5])) + str(grid[8]))
        return True
    if grid[0] + grid[4] + grid[8] == "XXX" or grid[0] + grid[4] + grid[8] ==  "OOO":
        print(str(grid[0]) + str(str(grid[4])) + str(grid[8]))
        return True
    if grid[2] + grid[4] + grid[6] == "XXX" or grid[2] + grid[4] + grid[6] ==  "OOO":
        print(str(grid[2]) + str(str(grid[4])) + str(grid[6]))
        return True
    return False



def printGrid(Grid, Player):
    print(colorama.ansi.clear_screen())
    print(f"{Fore.BLUE}It's {Player}'s turn")
    print(f"{Fore.BLUE}-{Fore.RESET}" * int(columns))
    Grid = [
    str(Grid[0]).replace("1", "X").replace("0", "O").replace("2", " "),
    str(Grid[1]).replace("1", "X").replace("0", "O").replace("2", " "),
    str(Grid[2]).replace("1", "X").replace("0", "O").replace("2", " "),
    str(Grid[3]).replace("1", "X").replace("0", "O").replace("2", " "),
    str(Grid[4]).replace("1", "X").replace("0", "O").replace("2", " "),
    str(Grid[5]).replace("1", "X").replace("0", "O").replace("2", " "),
    str(Grid[6]).replace("1", "X").replace("0", "O").replace("2", " "),
    str(Grid[7]).replace("1", "X").replace("0", "O").replace("2", " "),
    str(Grid[8]).replace("1", "X").replace("0", "O").replace("2", " ")
    ]
    print(f"{Fore.GREEN}[{Grid[0]}]  [{Grid[1]}]  [{Grid[2]}]\n\n[{Grid[3]}]  [{Grid[4]}]  [{Grid[5]}]\n\n[{Grid[6]}]  [{Grid[7]}]  [{Grid[8]}]")

def loop(theVal, grid):
    val = True
    grid = ["2", "2", "2", "2", "2", "2", "2", "2", "2"]
    poi = 0
    while val:
        poi = poi + 1
        grid = turn(0, theVal, grid)
        if "2" not in grid:
            poi = 0
            print(colorama.ansi.clear_screen())
            string = f"{Fore.BLUE}The grid is full\n{Fore.YELLOW}Score: {poi}\n\n\n\n\n{Fore.RESET}"
            for char in string:
                print(char, end='')
                time.sleep(0.09)
            val = False
            break
        if check(grid):
            print(colorama.ansi.clear_screen())
            string = f"{Fore.BLUE}{theVal[0]} has Won!\n{Fore.YELLOW}Score: {poi}\n\n\n\n\n{Fore.RESET}"
            for char in string:
                print(char, end='')
                time.sleep(0.09)
            val = False
            break
        grid = turn(1, theVal, grid)
        poi = poi + 1
        if "2" not in grid:
            poi = 0
            print(colorama.ansi.clear_screen())
            string = f"{Fore.BLUE}The grid is full\n{Fore.YELLOW}Score: {poi}\n\n\n\n\n{Fore.RESET}"
            for char in string:
                print(char, end='')
                time.sleep(0.09)
            val = False
            break
        if check(grid):
            string = f"{Fore.BLUE}{theVal[1]} has Won!\n{Fore.YELLOW}Score: {poi}\n\n\n\n\n{Fore.RESET}"
            for char in string:
                print(char, end='')
                time.sleep(0.09)
            val = False
            break
    
    if highscore == "None":
        thef.close()
        os.remove(f"{os.getcwd()}\\data.sco")
        open(f"{os.getcwd()}\\data.sco", "a+").write(str(poi))
    else:
         if poi > int(highscore):
            thef.close()
            os.remove(f"{os.getcwd()}\\data.sco")
            open(f"{os.getcwd()}\\data.sco", "a+").write(str(poi))
    restart()
        
    
    
    

def turn(player, theVal, Grid, message=""):
    for char in message:
        print(char, end='')
        time.sleep(0.04)
    if message != "": time.sleep(1)
    printGrid(Grid, theVal[player])
    val = input(f"{Fore.BLUE}\n\n> {Fore.RESET}")
    try:
        if val in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if val == "1":
                if Grid[int(val) - 1] == "2":
                    Grid[0] = player
                else: raise ValueError("That's Not Available")

            if val == "2":
                if Grid[int(val) - 1] == "2":
                    Grid[1] = player
                else: raise ValueError("That's Not Available")

            if val == "3":
                if Grid[int(val) - 1] == "2":
                    Grid[2] = player
                else: raise ValueError("That's Not Available")

            if val == "4":
                if Grid[int(val) - 1] == "2":
                    Grid[3] = player
                else: raise ValueError("That's Not Available")

            if val == "5":
                if Grid[int(val) - 1] == "2":
                    Grid[4] = player
                else: raise ValueError("That's Not Available")

            if val == "6":
                if Grid[int(val) - 1] == "2":
                   Grid[5] = player
                else: raise ValueError("That's Not Available")
            if val == "7":
                if Grid[int(val) - 1] == "2":
                    Grid[6] = player
                else: raise ValueError("That's Not Available")

            if val == "8":
                if Grid[int(val) - 1] == "2":
                    Grid[7] = player
                else: raise ValueError("That's Not Available")
            if val == "9":
                if Grid[int(val) - 1] == "2":
                    Grid[8] = player
                else: raise ValueError("That's Not Available")
        else:
            turn(player, theVal, Grid, f"{Fore.GREEN}That didn't work...")
    except ValueError as e:
        turn(player, theVal, Grid, f"{Fore.GREEN}Sorry kid, that's already taken.")
    return Grid

def restart():
    import subprocess
    import sys
    string = f"{Fore.YELLOW}Restart? (y/n){Fore.RESET}"
    for char in string:
        print(char, end='')
        time.sleep(0.05)
    time.sleep(1)
    val = input(f"{Fore.BLUE}\n> {Fore.RESET}")
    if val.lower() == "y":
        thef.close()
        subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
    else:
        if val.lower() == "n" or val.lower() == "":
            exit(0)
        else:
            print(colorama.ansi.clear_screen())
            restart()


def splash(highScore):
    print(colorama.ansi.clear_screen())
    string = f"{warn}\n{Fore.BLUE}Tic Tac Toe"
    for char in string:
        print(char, end='')
        time.sleep(0.05)
    time.sleep(1)
    string = f"\n\n\n\n"
    for char in string:
        print(char, end='')
        time.sleep(0.05)
    print(colorama.ansi.clear_screen())
    print(f"{Fore.BLUE}Tic Tac Toe")
    print(f"{Fore.BLUE}-{Fore.RESET}" * int(columns))
    print(f"{Fore.YELLOW}High Score: {highScore}")
    print(f"{Fore.GREEN}Press [H] + [Enter] for help")
    print(f"{Fore.GREEN}Press [Enter] to start{Fore.RESET}")
    return input(f"{Fore.BLUE}> {Fore.RESET}")

def start():
    print(colorama.ansi.clear_screen())
    print(f"{Fore.BLUE}New Game")
    print(f"{Fore.BLUE}-{Fore.RESET}" * int(columns))
    p1 = input(f"{Fore.YELLOW}Enter Player 1's Name\n{Fore.BLUE}> {Fore.RESET}")
    if p1 == "":    p1 = "Player One"
    print(colorama.ansi.clear_screen())
    print(f"{Fore.BLUE}New Game")
    print(f"{Fore.BLUE}-{Fore.RESET}" * int(columns))
    print(f"{Fore.YELLOW}{p1}")
    p2 = input(f"{Fore.YELLOW}Enter Player 2's Name\n{Fore.BLUE}> {Fore.RESET}")
    if p2 == "":    p2 = "Player Two"
    return [p1, p2]
def awaitForTitleInput(highScore, grid):
    theIn = splash(highScore)
    if len(theIn) != 0:
        if theIn == "wipe_data":
            thef.close()
            os.remove(f"{os.getcwd()}\\data.sco")
            time.sleep(1)
            import subprocess
            import sys
            thef.close()
            subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
        if "exec>>" in theIn:
            thef.close()
            val = theIn.replace("exec>>", "")
            try:
                exec(val)
                print(f"No Error's in {val}")
            except BaseException as e: print("e")
            time.sleep(1)
            import subprocess
            import sys
            thef.close()
            subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
        print(theIn)
        string = f"{Fore.BLUE}How to play:\n[1]  [2]  [3]\n\n[4]  [5]  [6]\n\n[7]  [8]  [9]\n\nEach square has a corresponding number. \nPlace your X/O on a square by typing the squares corresponding number. \nRestarting in 3 seconds!\n\n-APlayerUnnamed\n"
        for char in string:
            print(char, end='')
            time.sleep(0.05)
        import sys
        import subprocess
        time.sleep(1)
        thef.close()
        subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
    else:
        theVal = list(start())
        loop(theVal, grid)
        print(theIn)
        time.sleep(20)

print(colorama.ansi.clear_screen())
print(f"{colorama.Fore.YELLOW}Starting...{colorama.Fore.RESET}")
awaitForTitleInput(highscore, grid)
