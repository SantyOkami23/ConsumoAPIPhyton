from API import datos_abiertos
from UI import interfaz

interfaz.menu_principal()
lim_registros = interfaz.opciones(1)
nom_departamento = interfaz.opciones(2)

datos_retornados = datos_abiertos.consultar_datos(lim_registros, nom_departamento)
interfaz.mostrar_resultados(datos_retornados, lim_registros)
