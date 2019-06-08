import random
import xlsxwriter
#Algoritmo recursivo de una busqueda binaria

def busquedaBinariaRecursivo(arreglo,inicio,n,dato):

    mitad = int((inicio + n)/2)
    datoMitad = arreglo[mitad]
    if(inicio>n):
        return 0

    if(dato == datoMitad):
        return 1

    if(dato < datoMitad):
        return 1+busquedaBinariaRecursivo(arreglo,inicio,mitad-1,dato)

    if(dato > datoMitad):
        return 1+busquedaBinariaRecursivo(arreglo,mitad+1,n,dato)

#Arreglos de distintas posiciones
arreglo1024 = []
arreglo2048 = []
arreglo4096 = []
arreglo8192 = []
arreglo16384 = []

#Metodo para generar un arreglo random mandando el tamaño de este, sin repeticiones
def generarArregloRandom(n):
    lista = []
    r1 = random.randint(1, 100000)
    lista.append(r1)
    while (len(lista) != n):
        r1 = random.randint(1, 100000)
        if r1 not in lista:
            lista.append(r1)
    return lista

arreglo1024 = generarArregloRandom(1024)
arreglo2048 = generarArregloRandom(2048)
arreglo4096 = generarArregloRandom(4096)
arreglo8192 = generarArregloRandom(8192)
arreglo16384 = generarArregloRandom(16384)

arreglo1024.sort()
arreglo2048.sort()
arreglo4096.sort()
arreglo8192.sort()
arreglo16384.sort()


dato = int(input(".::Búsqueda binaria::.\nIngrese dato a buscar: "))
print("Tamaño arreglo   |   N° operaciones\n    1024         |      "+str(busquedaBinariaRecursivo(arreglo1024,0,1024,dato)))
print("    2048         |      "+str(busquedaBinariaRecursivo(arreglo2048,0,2048,dato)))
print("    4096         |      "+str(busquedaBinariaRecursivo(arreglo4096,0,4096,dato)))
print("    8192         |      "+str(busquedaBinariaRecursivo(arreglo8192,0,8192,dato)))
print("    16384        |      "+str(busquedaBinariaRecursivo(arreglo16384,0,16384,dato)))
cantidadNuevoArray = int(input("Ingrese una cantidad para el tamaño de un nuevo arreglo y revisar su n° de operaciones con el dato "+str(dato)+" (0 si no es necesario): "))
while(cantidadNuevoArray > 0):
    arregloNuevo = generarArregloRandom(cantidadNuevoArray)
    arregloNuevo.sort();
    print("    "+str(cantidadNuevoArray)+"         |      " + str(busquedaBinariaRecursivo(arregloNuevo, 0, cantidadNuevoArray, dato)))
    cantidadNuevoArray = int(input("Ingrese nuevo valor para comparar (0 para continuar): "))

arregloOperaciones = [busquedaBinariaRecursivo(arreglo1024,0,1024,dato),busquedaBinariaRecursivo(arreglo2048,0,2048,dato),busquedaBinariaRecursivo(arreglo4096,0,4096,dato),busquedaBinariaRecursivo(arreglo8192,0,8192,dato),busquedaBinariaRecursivo(arreglo16384,0,16384,dato)]
arregloNumeroOperaciones = [1024,2048,4096,8192,16384]
workbook = xlsxwriter.Workbook('Datos de arreglos.xlsx')
worksheet = workbook.add_worksheet('Operaciones')
row = 0
col = 0
for item in arregloNumeroOperaciones:
    worksheet.write(row, col, item)
    row += 1
row = 0
col = 1
for item in arregloOperaciones:
    worksheet.write(row, col, item)
    row +=1
worksheet.write(18,1,'El análisis de este gráfico es que al aumentar al doble el tamaño del array, la cantidad de veces que se tendrá que volver a producir la recursión aumentará en uno, en caso de que no se encuentre el valor en el array')
worksheet.write(19,1,'En el caso en que se encuentre el valor, la gráfica variará en esos array con una cantidad menor de operaciones, mientras que en los que no se encuentre seguirá con el aumento en 1.')
chart = workbook.add_chart({'type': 'line'})
chart.add_series({
    'values': '=Operaciones!$B$1:$B$5',
})
chart.set_y_axis({'log_base': 10})
chart.set_y_axis({'min': 10, 'max': 15})
worksheet.insert_chart('C1', chart)
workbook.close()

