oracionCorrecta = 'El niño juega con su pelota '.split( ) #Aqui se cambia la oracion correcta y la convertimos en lista
def abrirArchivo():
    respuesta=''
    with open('texto.txt','r',encoding='utf-8')as f: #Método para abrir archivo txt, r de read y usar codificacion de caracteres utf-8
        oracionTXT=f.readline().split( ) #leemos el archivo txt y lo convertimos en lista

        for i in oracionCorrecta: #Recorremos la oracion correcta
            for j in oracionTXT: #Recorremos la oracion del archivo de texto
                if i==j: ##Comparamos el primer dato de la lista correcta con todos los de la lista incorrecta
                    respuesta+=j+' ' #Si lo encuentra lo agrega a una cadena más un espacio                    
        print (respuesta)
        
if __name__ == '__main__':
    abrirArchivo()