from pynput.mouse import Button, Controller
import time
import pyautogui as inp


def find_positions(path, Region=[0, 0, inp.resolution()[0] * 2, inp.resolution()[1] * 2]):
    return inp.locateAllOnScreen(path, confidence = 0.8, region=Region)
   
def solve(position):
    # translation resolution
    top = position.top / 2 + position.height / 4
    left = position.left / 2 + position.width / 4
    inp.click(left, top)
    inp.click(left + 20, top + 30)
    inp.click(left + 160, top + 30)


def find_and_click(path):
    position_button = inp.locateOnScreen(path)
    top = position_button.top / 2 + position_button.height / 4
    left = position_button.left / 2 + position_button.width / 4
    inp.click(left, top)
    
def click_by_position(position):
    top = position.top / 2 + position.height / 4
    left = position.left / 2 + position.width / 4
    inp.click(left, top)
 
def auto_solve(): 
    inp.click(list(map(lambda x: x / 2, inp.resolution())))
    inp.hotkey('ctrl', 'left')
    
    time.sleep(2)  
    while True:
        all_checkboxes = find_positions('references/solvation.png')
        for checkbox in all_checkboxes:
            solve(checkbox)
        time.sleep(1)
            
            
def send_all():
    inp.click(list(map(lambda x: x / 2, inp.resolution())))
    inp.hotkey('ctrl', 'left')
    
    time.sleep(0.5)
    all_tabs = find_positions('references/tab_identifier.png', [0, 0, inp.resolution()[0] * 2, 80])
    first = next(all_tabs)
    click_by_position(first)
    all_tabs_lenght = sum([1 for _ in all_tabs]) + 1
    for i in range(all_tabs_lenght):
        inp.hotkey('command', 'down')
        time.sleep(0.1)
        find_and_click('references/finish_attempt.png')
        if i != all_tabs_lenght - 1:
            inp.hotkey('option', 'command', 'right')
    click_by_position(first)
    for j in range(all_tabs_lenght):
        time.sleep(0.1)
        inp.click(925, 450)
        time.sleep(0.)
        inp.hotkey('command', 'down')
        time.sleep(0.05)
        find_and_click('references/send_all.png')
        inp.click(700, 630)
        if j != all_tabs_lenght - 1:
            inp.hotkey('option', 'command', 'right')

def start_all():
    inp.click(list(map(lambda x: x / 2, inp.resolution())))
    inp.hotkey('ctrl', 'left')
    time.sleep(0.5)
    
    all_tabs = find_positions('references/tab_identifier.png', [0, 0, inp.resolution()[0] * 2, 80])
    click_by_position(next(all_tabs))
    all_tabs_lenght = sum([1 for _ in all_tabs]) + 1
    for i in range(all_tabs_lenght):
        find_and_click('references/start.png')
        inp.hotkey('option', 'command', 'right')
def solve_critical_error():    
    all_tabs = find_positions('references/tab_identifier.png', [0, 0, inp.resolution()[0] * 2, 80])
    click_by_position(next(all_tabs))
    all_tabs_lenght = sum([1 for _ in all_tabs]) + 1
    for i in range(all_tabs_lenght):
        inp.click(925, 450)
        time.sleep(0.05)
        if i != all_tabs_lenght - 1:
            inp.hotkey('option', 'command', 'right')
        
        


welcome = """Programm to run:
1. solve
2. send all
3. start all
4. solve critical error
"""
choise = int(input(welcome))
match choise:
    case 1:
        auto_solve()
    case 2:
        send_all()
    case 3:
        start_all()
        solve_critical_error()
    case 4:
        inp.click(list(map(lambda x: x / 2, inp.resolution())))
        inp.hotkey('ctrl', 'left')
        time.sleep(0.5)
        solve_critical_error()
    case _:
        exit()

