import os
import random

print("Directorio actual:", os.getcwd())

class Juego:
    def __init__(self, mapa, inicio, fin):
        self.mapa = mapa
        self.inicio = inicio
        self.fin = fin
    
    def mover(self, direccion):
        fila_actual, columna_actual = self.inicio
        
        if direccion == 'arriba':
            fila_actual -= 1
        elif direccion == 'abajo':
            fila_actual += 1
        elif direccion == 'izquierda':
            columna_actual -= 1
        elif direccion == 'derecha':
            columna_actual += 1
        
        if self.mapa[fila_actual][columna_actual] == '#':
            return False
        elif self.mapa[fila_actual][columna_actual] == 'F':
            return True
        
        self.inicio = (fila_actual, columna_actual)
        return False

class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        mapa, inicio, fin = self.leer_mapa_aleatorio(path_a_mapas)
        super().__init__(mapa, inicio, fin)
    
    def leer_mapa_aleatorio(self, path_a_mapas):
        lista_archivos = os.listdir(path_a_mapas)
        nombre_archivo = random.choice(lista_archivos)
        path_completo = os.path.join(path_a_mapas, nombre_archivo)

        with open(path_completo, 'r') as archivo:
            lineas = archivo.readlines()
            dimensiones = lineas[0].strip().split(',')
            filas, columnas = int(dimensiones[0]), int(dimensiones[1])
            mapa = [linea.strip() for linea in lineas[1:filas+1]]
            inicio = tuple(map(int, lineas[filas+1].strip().split(',')))
            fin = tuple(map(int, lineas[filas+2].strip().split(',')))

        return mapa, inicio, fin

if __name__ == "__main__":
    path_a_mapas = r"C:\Users\Los Foneffos\Desktop\mi_juego\map"
    juego = JuegoArchivo(path_a_mapas)
      
    while True:
        print("\nMapa actual:")
        for fila in juego.mapa:
            print(fila)
        
        direccion = input("Ingresa la dirección (arriba/abajo/izquierda/derecha): ")
        if juego.mover(direccion):
            print("¡Has llegado a la meta!")
            break

