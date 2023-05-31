import random
import matplotlib.pyplot as plt

#Listas de equipos de la liga
equipos_local = ["Nacional", "Millonarios", "América de Cali", "Santa Fe", "Junior", "Once Caldas", "Deportivo Cali", "Medellín", "Tolima", "Envigado", "Bucaramanga", "Alianza Petrolera", "Atlético Nacional", "Cúcuta Deportivo", "Patriotas"]


equipos_visitante = ["Millonarios", "Nacional", "Santa Fe", "América de Cali", "Once Caldas", "Junior", "Medellín", "Deportivo Cali", "Envigado", "Tolima", "Alianza Petrolera", "Bucaramanga", "Cúcuta Deportivo", "Atlético Nacional", "Patriotas"]


goles_local = [random.randint(0, 5) for i in range(len(equipos_local))]
goles_visitante = [random.randint(0, 5) for i in range(len(equipos_visitante))]


while True:
    # Imprimimos las opciones del menú que nos piden en el taller
    print("Bienvenido al menú:")
    print("1. Calcular la cantidad de partidos por equipo")
    print("2. Calcular la cantidad de partidos ganados por equipo")
    print("3. Calcular la cantidad de partidos perdidos por equipo")
    print("4. Calcular la cantidad de partidos empatados por equipo")
    print("5. Calcular la cantidad de goles de los equipos locales PLUS graficar")
    print("6. Calcular la cantidad de goles de los equipos visitantes PLUS graficar")
    print("7. Calcular la cantidad total de goles de todos los partidos")
    print("8. Calcular la cantidad de partidos por equipo")
    print("9. Listado de los equipos con sus goles de local y de visitante")
    print("10. Equipo que más goles realizó")
    print("11. Equipo que menos goles recibió")
    print("12. Lea por teclado el nombre del equipo y liste los partidos en lo que ha participado y sus marcadores")
    print("13. Armar la tabla de posiciones y crear una nueva lista con los puntos por equipo")
    print("14. Imprimir la tabla de posiciones de mayor a mejor por puntaje")

    # Le decimos al usuario que seleccione una opción del menú anterior
    opcion = int(input("Por favor, seleccione una opción del menú (1-14): "))

    # Evaluamos la opción seleccionada y ejecutamos el código correspondiente
    if opcion == 1:
        partidos = [("EquipoA", "EquipoB", "2-1"), ("EquipoC", "EquipoA", "0-3"), ("EquipoB", "EquipoD", "3-3"),
                    ("EquipoA", "EquipoD", "1-0"), ("EquipoC", "EquipoB", "2-2"), ("EquipoB", "EquipoA", "0-2"),
                    ("EquipoA", "EquipoC", "1-0"), ("EquipoD", "EquipoB", "1-1"), ("EquipoD", "EquipoA", "0-1"),
                    ("EquipoB", "EquipoC", "1-2")]

        cantidad_partidos = {}

        for partido in partidos:
            equipos = partido[:2]  # Obtenemos los nombres de los equipos de la liga colombiana
            for equipo in equipos:
                cantidad_partidos[equipo] = cantidad_partidos.get(equipo,
                                                                  0) + 1  # Agregamos el partido al equipo correspondiente

        print("Cantidad de partidos por equipo:")
        for equipo, cantidad in cantidad_partidos.items():
            print(equipo + ":", cantidad)
    elif opcion == 2:
        partidos_jugados = [("Atlético Nacional", "Independiente Medellín"),
                            ("Deportivo Cali", "Atlético Huila"),
                            ("Junior FC", "Rionegro Águilas"),
                            ("América de Cali", "Deportes Quindío"),
                            ("Millonarios FC", "Atlético Junior"),
                            ("Independiente Santa Fe", "Atlético Bucaramanga"),
                            ("Once Caldas", "Atlético Nacional"),
                            ("Deportivo Pereira", "Jaguares de Córdoba"),
                            ("Atlético Bucaramanga", "Deportivo Cali"),
                            ("Jaguares de Córdoba", "Millonarios FC"),
                            ("Envigado FC", "Alianza Petrolera"),
                            ("La Equidad", "Once Caldas"),
                            ("Alianza Petrolera", "Deportivo Pasto"),
                            ("Patriotas Boyacá", "La Equidad"),
                            ("Boyacá Chicó", "Envigado FC"),
                            ("Deportes Tolima", "Patriotas Boyacá"),
                            ("Deportivo Pasto", "Boyacá Chicó"),
                            ("Cúcuta Deportivo", "Deportes Tolima")]

        partidos_por_equipo = {}
        for partido in partidos_jugados:
            equipo_local, equipo_visitante = partido
            partidos_por_equipo[equipo_local] = partidos_por_equipo.get(equipo_local, 0) + 1
            partidos_por_equipo[equipo_visitante] = partidos_por_equipo.get(equipo_visitante, 0) + 1

        print(partidos_por_equipo)
    elif opcion == 3:
        partidos_perdidos = {}

        for i in range(len(equipos_local)):
            if goles_local[i] < goles_visitante[i]:
                equipo_perdedor = equipos_local[i]
            elif goles_local[i] > goles_visitante[i]:
                equipo_perdedor = equipos_visitante[i]
            else:
                continue

            if equipo_perdedor in partidos_perdidos:
                partidos_perdidos[equipo_perdedor] += 1
            else:
                partidos_perdidos[equipo_perdedor] = 1

        for equipo, perdidos in partidos_perdidos.items():
            print(f"{equipo} perdió {perdidos} partidos")
    elif opcion == 4:
        partidos = [('Equipo A', 'Equipo B', 1, 1), ('Equipo C', 'Equipo A', 0, 0), ('Equipo B', 'Equipo C', 2, 2),
                    ('Equipo A', 'Equipo D', 3, 2), ('Equipo D', 'Equipo B', 1, 1)]

        partidos_empatados = {}

        for partido in partidos:
            equipo_local, equipo_visitante, goles_local, goles_visitante = partido

            # Si el partido es una igualaciòn , aumentamos el contador de empates para los dos equipos
            if goles_local == goles_visitante:
                if equipo_local in partidos_empatados:
                    partidos_empatados[equipo_local] += 1
                else:
                    partidos_empatados[equipo_local] = 1

                if equipo_visitante in partidos_empatados:
                    partidos_empatados[equipo_visitante] += 1
                else:
                    partidos_empatados[equipo_visitante] = 1

        print(partidos_empatados)
    elif opcion == 5:
        goles_por_equipo_local = {}
        for equipo, goles in zip(equipos_local, goles_local):
            if equipo in goles_por_equipo_local:
                goles_por_equipo_local[equipo] += goles
            else:
                goles_por_equipo_local[equipo] = goles

        # Creamos un gráfico de barras para visualizar la cantidad de goles de los equipos locales
        plt.bar(goles_por_equipo_local.keys(), goles_por_equipo_local.values())
        plt.xlabel("Equipo local")
        plt.ylabel("Cantidad de goles")
        plt.title("Goles de los equipos locales")
        plt.show()
    elif opcion == 6:
        goles_por_equipo_visitante = {}
        for equipo, goles in zip(equipos_visitante, goles_visitante):
            if equipo in goles_por_equipo_visitante:
                goles_por_equipo_visitante[equipo] += goles
            else:
                goles_por_equipo_visitante[equipo] = goles

        # Creamos un gráfico de barras para visualizar la cantidad de goles de los equipos visitantes
        plt.bar(goles_por_equipo_visitante.keys(), goles_por_equipo_visitante.values())
        plt.xlabel("Equipo visitante")
        plt.ylabel("Cantidad de goles")
        plt.title("Goles de los equipos visitantes")
        plt.show()
    elif opcion == 7:
        total_goles = sum(goles_local) + sum(goles_visitante)

        # Imprimimos la cantidad total de goles
        print("La cantidad total de goles en la liga es:", total_goles)
    elif opcion == 8:
        equipos = ['América de Cali', 'Atlético Bucaramanga', 'Atlético Nacional', 'Deportes Tolima', 'Deportivo Cali',
                   'Envigado', 'Independiente Medellín', 'Jaguares de Córdoba', 'Junior', 'La Equidad', 'Millonarios',
                   'Once Caldas', 'Patriotas Boyacá', 'Rionegro Águilas', 'Santa Fe', 'Unión Magdalena']

        partidos_por_equipo = {}

        # Recorrer cada equipo
        for equipo in equipos:
            # Inicializar la cantidad de partidos del equipo en 0
            partidos = 0
            # Recorrer cada otro equipo
            for otro_equipo in equipos:
                # Si el equipo es diferente al otro equipo
                if equipo != otro_equipo:
                    # Incrementar la cantidad de partidos del equipo
                    partidos += 1
            # Agregar la cantidad de partidos del equipo al diccionario
            partidos_por_equipo[equipo] = partidos

        # Mostrar la cantidad de partidos por equipo
        for equipo, partidos in partidos_por_equipo.items():
            print(f"{equipo}: {partidos} partidos")
    elif opcion == 9:
        equipos = ['Equipo A', 'Equipo B', 'Equipo C', 'Equipo D']

        # Define una lista de goles de local
        goles_local = [10, 8, 5, 12]

        # Define una lista de goles de visitante
        goles_visitante = [6, 9, 7, 3]

        # Imprime el listado de equipos con sus goles de local y visitante
        for i in range(len(equipos)):
            print(equipos[i] + ': Goles local = ' + str(goles_local[i]) + ', Goles visitante = ' + str(
                goles_visitante[i]))
    elif opcion == 10:
        goles_por_equipo = {}

        partidos = [
            {'equipo_local': 'Millonarios', 'goles_local': 2, 'equipo_visitante': 'Nacional', 'goles_visitante': 1},
            {'equipo_local': 'Junior', 'goles_local': 3, 'equipo_visitante': 'Cali', 'goles_visitante': 0},
            {'equipo_local': 'Cali', 'goles_local': 2, 'equipo_visitante': 'Millonarios', 'goles_visitante': 1},
            {'equipo_local': 'Nacional', 'goles_local': 1, 'equipo_visitante': 'Junior', 'goles_visitante': 2},
            # ...
        ]

        for partido in partidos:
            equipo_local = partido['equipo_local']
            goles_local = partido['goles_local']
            equipo_visitante = partido['equipo_visitante']
            goles_visitante = partido['goles_visitante']

            # Agrega los goles anotados por el equipo local al diccionario
            if equipo_local in goles_por_equipo:
                goles_por_equipo[equipo_local] += goles_local
            else:
                goles_por_equipo[equipo_local] = goles_local

            # Agrega los goles anotados por el equipo visitante al diccionario
            if equipo_visitante in goles_por_equipo:
                goles_por_equipo[equipo_visitante] += goles_visitante
            else:
                goles_por_equipo[equipo_visitante] = goles_visitante

        equipo_mas_goleador = max(goles_por_equipo, key=goles_por_equipo.get)

        print(
            f"El equipo más goleador de la liga colombiana es: {equipo_mas_goleador} con {goles_por_equipo[equipo_mas_goleador]} goles anotados.")
    elif opcion == 11:
        liga_colombiana = [
            {'Nombre del Equipo': 'Equipo A', 'Goles Marcados': 20, 'Goles Recibidos': 10},
            {'Nombre del Equipo': 'Equipo B', 'Goles Marcados': 15, 'Goles Recibidos': 5},
            {'Nombre del Equipo': 'Equipo C', 'Goles Marcados': 25, 'Goles Recibidos': 20},
            {'Nombre del Equipo': 'Equipo D', 'Goles Marcados': 30, 'Goles Recibidos': 15},
        ]

        menos_goles_recibidos = min(liga_colombiana, key=lambda x: x['Goles Recibidos'])

        nombre_equipo = menos_goles_recibidos['Nombre del Equipo']

        print("El equipo que menos goles recibió fue:", nombre_equipo)
    elif opcion == 12:
        # Crear un diccionario con los equipos de la Liga Colombiana y sus partidos
        equipos = {
            "Millonarios": [("Millonarios", 1), ("Junior", 2), ("América", 2)],
            "Nacional": [("Nacional", 0), ("Once Caldas", 1), ("Tolima", 1)],
            "Santa Fe": [("Santa Fe", 1), ("Cali", 1), ("Pereira", 2)],
            "América": [("América", 1), ("Tolima", 1), ("Millonarios", 2)],
            "Junior": [("Junior", 2), ("Millonarios", 0), ("Tolima", 1)],
            "Cali": [("Cali", 0), ("Santa Fe", 1), ("Nacional", 0)],
            "Pereira": [("Pereira", 0), ("Tolima", 1), ("Santa Fe", 2)],
            "Once Caldas": [("Once Caldas", 0), ("Nacional", 1), ("Tolima", 1)],
            "Tolima": [("Tolima", 2), ("América", 1), ("Once Caldas", 1)],
        }

        equipo = input("Ingresa el nombre del equipo: ")

        if equipo in equipos:
            print(f"Partidos de {equipo}:")
            for partido in equipos[equipo]:
                local = partido[0]
                visitante = [x for x in partido if x != local][0]
                resultado_local = partido[1]
                resultado_visitante = [x for x in partido if x != resultado_local][0]
                print(f"{local} {resultado_local} - {resultado_visitante} {visitante}")
        else:
            print(f"No se encontraron partidos para el equipo {equipo}")
    elif opcion == 13:
        resultados = [
            ('Nacional', 'Junior', 2, 1),
            ('Millonarios', 'Santa Fe', 0, 0),
            ('Medellin', 'Cali', 1, 1),
            ('Bucaramanga', 'Tolima', 0, 2),
            ('Once Caldas', 'Envigado', 1, 0),
            ('Patriotas', 'Huila', 2, 0),
            ('Pasto', 'Alianza Petrolera', 1, 1),
            ('Cucuta', 'America', 1, 1),
        ]

        tabla = {}
        for local, visitante, goles_local, goles_visitante in resultados:
            # Actualizar puntos del equipo local
            if local not in tabla:
                tabla[local] = 0
            if goles_local > goles_visitante:
                tabla[local] += 3
            elif goles_local == goles_visitante:
                tabla[local] += 1

            # Actualizar los puntos del equipo visitante
            if visitante not in tabla:
                tabla[visitante] = 0
            if goles_visitante > goles_local:
                tabla[visitante] += 3
            elif goles_local == goles_visitante:
                tabla[visitante] += 1

        # Ordenar la tabla de posiciones
        tabla_ordenada = sorted(tabla.items(), key=lambda x: x[1], reverse=True)

        # Imprimir la tabla de posiciones
        print('Tabla de posiciones:')
        for i, (equipo, puntos) in enumerate(tabla_ordenada):
            print(f'{i + 1}. {equipo}: {puntos} puntos')

        # Crear la lista de puntos por cada equipo
        puntos_por_equipo = [puntos for equipo, puntos in tabla_ordenada]

        # Imprimimos la lista de puntos por equipo
        print('Puntos por equipo:')
        print(puntos_por_equipo)
    elif opcion == 14:
        # Lista de equipos y sus respectivos puntajes
        equipos = ["Equipo A", "Equipo B", "Equipo C", "Equipo D", "Equipo E"]
        puntajes = [12, 10, 8, 6, 4]

        # Ordenar equipos por puntaje en orden
        tabla_posiciones = sorted(zip(equipos, puntajes), key=lambda x: x[1], reverse=True)

        print("Tabla de posiciones:")
        print("--------------------")
        print("| Equipo     | Pts |")
        print("--------------------")
        for equipo, puntos in tabla_posiciones:
            print(f"| {equipo:<10} | {puntos:>3} |")
        print("--------------------")
    else:
        print("Opcion invalida")
