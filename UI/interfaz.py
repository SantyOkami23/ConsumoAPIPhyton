
def menu_principal():
    print("|==================================================|")
    print("|    PORTAL DE DATOS ABIERTOS                      |")
    print("|==================================================|")
    print("Proyecto API, casos positivos de Covid-19 en Colombia")
    print ("Por favor ingrese los datos que se piden a continuación, muchas gracias: ")
    print("Números enteros y los nombres de los departamentos con Mayuscula incial y con tilde si se requiere. \n")

#Definimos las dos opciones sobre las cualesse va a mostrar la infomación en pantalla,
# en este caso limite de registros y departamento
def opciones(parametro):
    if parametro == 1:
        lim_registros = int(input("Cantidad de Registros : "))
        return lim_registros
    else:
        nom_departamento = input("Nombre del Departamento: ")
        return nom_departamento

#Imprimimos los datos con un ciclo while, utilizando notación de índice
def mostrar_resultados(datos_retornados, registros):
    print("\n=====================================================================================")
    print("\t\t\t\t\t\t\t\tCASOS DE COVID 19 EN COLOMBIA:\n\n|Ciudad de ubicacion|\tDepartamento|\tEdad|\tTipo|\tEstado|\tPais de procedencia|")
    print("---------------------------------------------------------------------------------------")
    i = 0
    while i < registros:
        tabla_datos = datos_retornados[i]

        #Se establece un caso en el que sale error dado que en algunos no existe pais de procendecia
        if 'pa_s_de_procedencia' not in tabla_datos:
            print("\t|", tabla_datos['ciudad_de_ubicaci_n'], "\t\t\t|",tabla_datos['departamento'], "\t|", tabla_datos['edad'],
                  "\t|", tabla_datos['tipo'], "\t|", tabla_datos['estado'], "\t|", "N/A|")


        #Caso en el que encontramos todos los datos en el portal.
        else:
            print("\t|", tabla_datos['ciudad_de_ubicaci_n'], "\t\t\t|", tabla_datos['departamento'], "\t|", tabla_datos['edad'],
                  "\t|", tabla_datos['tipo'], "\t|", tabla_datos['estado'], "\t|", tabla_datos['pa_s_de_procedencia'],"\t|")

        print("===================================================================================")

        i += 1


