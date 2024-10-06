import pygame
from sys import exit
import threading
import tkinter as tk
from random import randint

janela = tk.Tk()
janela.title("Menu jogo")
janela.geometry("300x300")

def jogo():
    pygame.init()
    
    pontos = 0
    largura = 720
    altura = 460

    pygame.display.set_caption("Jogo")
    tela = pygame.display.set_mode((largura, altura))

    x_player1 = largura // 2
    y_player1 = altura // 2
    velocidade = 3.0  
    tiros = []

    velocidade_inimigo = 1.0  # 
    y_inimigo = 0
    x_inimigo = randint(0, largura - 30)

    clock = pygame.time.Clock()  

    while True:
        tela.fill((0, 0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                pygame.quit()
                janela.quit()
                exit()

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            x_player1 -= velocidade
        if keys[pygame.K_d]:
            x_player1 += velocidade
        if keys[pygame.K_w]:
            y_player1 -= velocidade
        if keys[pygame.K_s]:
            y_player1 += velocidade

        if keys[pygame.K_e]:
            tiros.append([x_player1 + 10, y_player1])  

        for tiro in tiros:
            tiro[1] -= 10  
            pygame.draw.rect(tela, (255, 0, 0), (tiro[0], tiro[1], 10, 10))  

        x_player1 = max(0, min(x_player1, largura - 30))
        y_player1 = max(0, min(y_player1, altura - 30))

        inimigo = pygame.draw.rect(tela, (0, 255, 0), (x_inimigo, y_inimigo, 30, 30))
        player = pygame.draw.rect(tela, (0, 0, 255), (x_player1, y_player1, 30, 30))  
        
        for tiro in tiros:
            tiro_rect = pygame.Rect(tiro[0], tiro[1], 10, 10)
            if tiro_rect.colliderect(inimigo):
                x_inimigo = randint(0, largura - 30)
                y_inimigo = 0  

        y_inimigo += velocidade_inimigo

        if player.colliderect(inimigo):
            pygame.quit()
            janela.quit()
            exit()

        pygame.display.update()

        clock.tick(60) 

def iniciar_jogo():
    game_thread = threading.Thread(target=jogo)
    game_thread.daemon = True
    game_thread.start()

label = tk.Label(janela, text="Dificuldade fácil:")
label.grid(column=0, row=1)
botao = tk.Button(janela, text="Clique aqui para iniciar", bg="blue", fg="aqua", command=iniciar_jogo)
botao.grid(column=2, row=1)

janela.mainloop()