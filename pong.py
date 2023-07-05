import pygame, sys, random

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
    ball.x += ball_speed_x
    ball.y +=ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_y *= -1

    #player score
    if ball.left <= 0:
        pygame.mixer.Sound.play(score_sound)
        player_score +=1
        score_time =pygame.time.get_tics()

    #opponent score
    if ball.right >= screen_width:
        pygame.mixer.Sound.play(score_sound)
        oponent_score += 1
        score_time =pygame.time.get_tics()

    if ball.colliderect(player) and ball_speed_x > 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.right -player.left) < 10:
            ball:speed_x *= -1
        elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
         elif abs(ball.top - player.bottom) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1

       if ball.colliderect(oponent) and ball_speed_x < 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.left -oponent.right) < 10:
            ball:speed_x *= -1
        elif abs(ball.bottom - oponent.top) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1
         elif abs(ball.top - oponent.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1 

def player_animation():
    player.y <= player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_animation():
    if opponent.top < ball.y
        opponent.y += opponent_speed
    if opponent.bottom > ball.y:
        opponent.y -= opponent_speed

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_start():
    global ball_speed_x, ball_speed_y, score_time

    current_time = pygame.time.get_tics()
    ball.center = (screen_width/2, screen_height/2)

    if current_time - score_time < 700:
        number_three = game_font.render("3", false, white)
        screen.blit(number_three, (screen_width/2 - 10, screen_height/2 + 20))
    if 700 < current_time - score_time < 1400:
        number_number = game_font.render("2", false, white)
        screen.blit(number_number, (screen_width/2 - 10, screen_height/2 + 20))
    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render("2", false, white)
        screen.blit(number_one, (screen_width/2 - 10, screen_height/2 + 20))
    
