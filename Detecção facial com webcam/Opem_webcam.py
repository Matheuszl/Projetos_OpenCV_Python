import cv2 as cv
import numpy as np


video = cv.VideoCapture(0)

#looping infinito para atualizar o frame da cemara 
while True:
    _, frame = video.read() #nesse momento ele le a captura de video e salva no frame
    cv.imshow("frame",frame) #imshow mostra o frame da camera na tela

    key = cv.waitKey(1)#um milesemo de segundo de atualizaçao da imagem 

    #key 27 = 'ESC' do teclado, serve para  fechar a tela de video
    if key == 27:
        break

video.release()
cv.destroyAllWindows()