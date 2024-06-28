import pygame
import sys
import math

pygame.init()

window = pygame.display.set_mode((1100, 800))
pygame.display.set_caption("Kaooa Game")

can_move_crow = {
    0: [1, 7],
    1: [0, 4, 2, 7],
    2: [1, 4, 3, 8],
    3: [2, 8],
    4: [1, 2],
    5: [7, 9],
    6: [8, 9],
    7: [0, 1, 5, 9],
    8: [2, 3, 6, 9],
    9: [5, 6, 7, 8]
}


can_jump_vulture = {
    0: [2, 9],
    1: [5, 3],
    2: [6, 0],
    3: [1, 9],
    4: [7, 8],
    5: [1, 8],
    6: [2, 7],
    7: [6, 4],
    8: [5, 4],
    9: [0, 3]
}


width = 700
height = 700

x = 250
y = 50
rad = 17
vel = 5

run = True

# Define circle positions
circles = [
    {"center": (x, y), "radius": rad},                  # point 0
    {"center": (x, y + 200), "radius": rad},            # point 1
    {"center": (x, y + 350), "radius": rad},            # point 2
    {"center": (x, y + 550), "radius": rad},            # point 3
    {"center": (x - 225, y + 275), "radius": rad},      # point 4
    {"center": (x + 300, y + 100), "radius": rad},      # point 5
    {"center": (x + 300, y + 450), "radius": rad},      # point 6
    {"center": (x + 125, y + 165), "radius": rad},      # point 7
    {"center": (x + 125, y + 400), "radius": rad},      # point 8
    {"center": (x + 200, y + 275), "radius": rad},      # point 9
]

# Lines connecting circles
connections = [
    (0, 1),
    (1, 2),
    (2, 3),
    (1, 4),
    (2, 4),
    (7, 1),
    (8, 2),
    (7, 9),
    (8, 9),
    (0, 7),
    (3, 8),
    (5, 7),
    (5, 9),
    (6, 9),
    (6, 8),
]

# ... (previous code)

# Number of crows and vultures
num_crows = 7
num_vultures = 1

# Font settings
font = pygame.font.Font(None, 36)

# Initial turn
current_turn = "Crow"  # You can set it to "Crow" if you want crows to start first

# Set to keep track of clicked buttons
# clicked_buttons = set()
vulture_buttons = set()
crow_buttons = set()
crow_killed = 0
vulture_go_set = set()
crow_go_set = set()
vulture_jump_set = set()

# def vulture_selection(pos):
#     print('hello')
#     events_list = pygame.event.get()
#     for event in events_list:
#         if event.type == pygame.QUIT:
#             run = False
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             mouse_x, mouse_y = pygame.mouse.get_pos()
#             for i, circle in enumerate(circles):
#                 center_x, center_y = circle["center"]
#                 radius = circle["radius"]
#                 distance = math.sqrt((mouse_x - center_x)**2 + (mouse_y - center_y)**2)

#                 # Check if the button is not clicked already
#                 if distance <= radius and i not in crow_buttons and i in can_move_crow[pos]:
#                     vulture_buttons.remove(pos)
#                     vulture_buttons.add(i)


last_clicked_vulture = None          # DEFAULT
last_clicked_crow = None
is_vul_dep = False
fl = 0

fl1 = 0
error_flag=0
invalid_vulture_circle=0
vulture_selects_wrong=0
crow_not_deploy=0
crow_pos_occu=0
all_crows=0

while run:
    # global var error_flag
    # global last_clicked_vulture=None
    pygame.time.delay(100)
    # if current_turn=="Crow":
    #     if crow_killed>=4:
    #         print('Vulture Wins')
    #         # display message that Vulture has won and end game
    # else:
    #     checker=0
    #     for adj_pos in can_move_crow[last_clicked_vulture]:
    #         if adj_pos not in crow_buttons:
    #             checker=1
    #             break
    #         else:
    #             for elem in can_move_crow[adj_pos]:
    #                 if elem not in crow_buttons and elem in can_jump_vulture[last_clicked_vulture]:
    #                     checker=1
    #                     break
    #     if checker==0:
    #         print("Crow Wins")
    #         # display message that Crow has won and end game

    events_list = pygame.event.get()
    for event in events_list:
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            error_flag=1
            for i, circle in enumerate(circles):
                center_x, center_y = circle["center"]
                radius = circle["radius"]
                distance = math.sqrt((mouse_x - center_x)
                                     ** 2 + (mouse_y - center_y)**2)

                # Check if the button is not clicked already
                if distance <= radius:
                    error_flag=0
                    if current_turn == "Crow":
                        invalid_vulture_circle=0
                        vulture_selects_wrong=0
                        if i not in crow_buttons and i not in vulture_buttons and num_crows==0 and fl1!=2:
                            all_crows=1
                        else:
                            all_crows=0
                        
                        if last_clicked_crow!=None and i !=last_clicked_crow and fl1==2 and (i not in can_move_crow[last_clicked_crow] or (i in crow_buttons or i in vulture_buttons)):
                            crow_pos_occu=1
                        else:
                            crow_pos_occu=0
                        if i not in crow_buttons and i not in vulture_buttons and num_crows>0 and last_clicked_crow == None:
                            # print(f"Button {i+1} clicked!")
                            num_crows = num_crows-1
                            crow_buttons.add(i)
                            crow_not_deploy=0
                            current_turn = "Vulture"
                        elif i == last_clicked_crow and num_crows==0:
                            last_clicked_crow = None
                            fl1 = 0
                            crow_go_set.clear()
                        elif i in crow_buttons and  last_clicked_crow==None:
                            # print('hi')
                            if num_crows==0:
                                last_clicked_crow = i
                                fl1 = 2
                                for elem in can_move_crow[last_clicked_crow]:
                                    if elem not in vulture_buttons and elem not in crow_buttons:
                                        crow_go_set.add(elem)
                            else:
                                crow_not_deploy=1
                        elif fl1 == 2 and i not in crow_buttons and i not in vulture_buttons and num_crows==0:
                            if i in can_move_crow[last_clicked_crow]:
                                crow_buttons.remove(last_clicked_crow)
                                crow_buttons.add(i)
                                last_clicked_crow = None
                                # fl1=1
                                crow_go_set.clear()
                                current_turn = "Vulture"
                            # code for possible options of crow
                    else:
                        crow_not_deploy=0
                        crow_pos_occu=0
                        all_crows=0
                        if i not in vulture_buttons and fl!=2 and num_vultures==0:
                            invalid_vulture_circle=1
                        else:
                            invalid_vulture_circle=0
                        if fl==2 and i not in vulture_go_set and i not in vulture_jump_set and i not in vulture_buttons:
                            vulture_selects_wrong=1
                        else:
                            vulture_selects_wrong=0
                        if i not in vulture_buttons and i not in crow_buttons and len(vulture_buttons) < 1:
                            # print(f"Button {i+1} bro clicked!")
                            num_vultures = num_vultures-1
                            fl = 1
                            vulture_buttons.add(i)
                            is_vul_dep = True
                            current_turn = "Crow"
                        elif i == last_clicked_vulture:
                            last_clicked_vulture = None
                            fl = 1
                            vulture_go_set.clear()
                            vulture_jump_set.clear()
                        elif i in vulture_buttons:
                            fl = 2
                            last_clicked_vulture = i
                            vl_fl=0
                            for elem in can_move_crow[last_clicked_vulture]:
                                if elem not in crow_buttons:
                                    vulture_go_set.add(elem)
                                else:
                                    for elem1 in can_move_crow[elem]:
                                        if elem1 not in vulture_buttons and elem1 not in crow_buttons and elem1 in can_jump_vulture[last_clicked_vulture]:
                                            vulture_jump_set.add(elem1)
                                            vl_fl=1
                            if vl_fl==1:
                                vulture_go_set.clear()
                                            
                        elif fl == 2 and i in can_move_crow[last_clicked_vulture]:
                            # if i in can_move_crow[last_clicked_vulture]:
                            if i in vulture_go_set:
                                vulture_buttons.remove(last_clicked_vulture)
                                vulture_buttons.add(i)
                                fl = 1
                                vulture_go_set.clear()
                                vulture_jump_set.clear()
                                current_turn = "Crow"
                        elif fl == 2:
                            if i in vulture_jump_set:
                                # print('j')
                                for elem1 in can_move_crow[i]:
                                    # print('k')
                                    if elem1 in crow_buttons and elem1 in can_move_crow[last_clicked_vulture]:
                                        # print('l')
                                        crow_buttons.remove(elem1)
                                        vulture_buttons.remove(
                                            last_clicked_vulture)
                                        vulture_buttons.add(i)
                                        fl = 1
                                        crow_killed += 1
                                        vulture_go_set.clear()
                                        vulture_jump_set.clear()
                                        current_turn = "Crow"

                            # if i in can_move_crow[last_clicked_vulture]:
                            #     for elem in can_move_crow[i]:
                            #         if elem not in crow_buttons and elem not in vulture_buttons:
                            #             if elem in can_jump_vulture[last_clicked_vulture]:
                            #                 vulture_buttons.remove(last_clicked_vulture)
                            #                 vulture_buttons.add(elem)
                            #                 fl=1
                            #                 crow_buttons.remove(i)
                            #                 crow_killed+=1
                            #                 current_turn="Crow"
                            # code for possible moves of vulture

                    # Mark the button as clicked
                    # if current_turn=='Crow':
                    #     crow_buttons.add(i)
                    # else:
                    #     vulture_buttons.add(i)
                    # Switch turn
                    # current_turn = "Crow" if current_turn == "Vulture" else "Vulture"
                # else:
                #     error_flag=1
                #     error_text=font.render(f"Please make a valid move!!", True, (255, 0 ,0))
                #     window.blit(error_text, (width - 450, 60))
            
                
                    

    # print(last_clicked_vulture)
    window.fill((0, 0, 0))

    # Draw clickable circular buttons
    for i, circle in enumerate(circles):
        center_x, center_y = circle["center"]
        radius = circle["radius"]

        # Change button color based on click and turn
        if i in vulture_buttons and fl == 1:
            color = (0, 0, 128)
        elif i in vulture_buttons and fl == 2:
            color = (128, 128, 128)
        elif i in vulture_go_set:
            # Grey color for last clicked vulture button
            color = (0, 100, 0)
        elif i in vulture_jump_set:
            color = (128, 0, 0)
        elif i == last_clicked_crow:
            color = (128, 128, 128)
        elif i in crow_go_set:  
            # Grey color for last clicked vulture button
            color = (0, 100, 0)
        elif i in crow_buttons:
            color = (153, 153, 0)
        else:
            color =  (0,0,0)

        pygame.draw.circle(window, color, circle["center"], radius)

        # Draw a red circular border for unclicked buttons
        if i not in vulture_buttons and i not in crow_buttons:
            pygame.draw.circle(window, (128, 0, 0),
                               circle["center"], radius, 2)

    # Draw lines connecting circles
    for connection in connections:
        pygame.draw.line(
            window,
            (128, 0, 0),
            circles[connection[0]]["center"],
            circles[connection[1]]["center"],
            2,
        )

    if current_turn == "Crow":
        if crow_killed >= 4:
            # print('Vulture Wins')
            # Display message that Vulture has won and end the game
            win_text = font.render("Vulture Wins!", True, (255, 255, 255))
            win_rect = win_text.get_rect(center=(width // 2, height // 2))
            window.blit(win_text, win_rect)
            pygame.display.flip()
            pygame.time.delay(2000)  # Pause for 2 seconds to show the message
            run = False
            break
    else:
        # if last_clicked_vulture != None:
        if last_clicked_vulture != None:
            checker = 0
            for adj_pos in can_move_crow[last_clicked_vulture]:
                if adj_pos not in crow_buttons:
                    checker = 1
                    break
                else:
                    for elem in can_move_crow[adj_pos]:
                        if elem not in crow_buttons and elem in can_jump_vulture[last_clicked_vulture]:
                            checker = 1
                            break
            if checker == 0:
                # print("Crow Wins")
                # Display message that Crow has won and end the game
                win_text = font.render("Crow Wins!", True, (255, 255, 255))
                win_rect = win_text.get_rect(center=(width // 2, height // 2))
                window.blit(win_text, win_rect)
                pygame.display.flip()
                # Pause for 2 seconds to show the message
                pygame.time.delay(2000)
                run = False
                break
    

    # Display number of crows and vultures
    crow_text = font.render(f"Crows Left to be deployed: {num_crows}", True, (255, 255, 255))
    vulture_text = font.render(
        f"Crows Killed: {crow_killed}", True, (255, 255, 255))

    # Display current turn at the bottom middle
    turn_text = font.render(f"{current_turn} Turn", True, (255, 255, 255))
    turn_rect = turn_text.get_rect(center=(width // 2, height - 30))
    
    # killed_info=font.render(f"Crows Killed: {crow_killed}",True, (255,255,255))
    if error_flag == 1:
        crow_not_deploy=0
        invalid_vulture_circle=0
        vulture_selects_wrong=0
        crow_pos_occu=0
        all_crows=0
        error_text=font.render(f"Please make a valid move!!", True, (255, 0 ,0))
        window.blit(error_text, (width - 250, height-100))
        # window.blit()
    if crow_not_deploy == 1:
        error_text=font.render(f"All Crows not deployed yet!!", True, (255, 0 ,0))
        window.blit(error_text, (width - 250, height-100))
    if invalid_vulture_circle == 1:
        error_text=font.render(f"You need to select the Vulture Position!!", True, (255, 0 ,0))
        window.blit(error_text, (width - 250, height-100))
    if vulture_selects_wrong == 1:
        error_text=font.render(f"Select only from Red / Green positions!!", True, (255, 0 ,0))
        window.blit(error_text, (width - 250, height-100))
    if crow_pos_occu== 1:
        error_text=font.render(f"Crow can only move on adjacent unoccupied positions!!", True, (255, 0 ,0))
        window.blit(error_text, (width - 250, height-100))
    if all_crows== 1:
        error_text=font.render(f"All Crows Deployed!!", True, (255, 0 ,0))
        window.blit(error_text, (width - 250, height-100))
    
    window.blit(crow_text, (width - 150, 20))
    window.blit(vulture_text, (width - 150, 60))
    window.blit(turn_text, turn_rect)
    pygame.display.flip()
    pygame.display.update()

pygame.quit()
sys.exit()
