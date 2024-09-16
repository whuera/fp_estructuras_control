def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)

def gestionar_notas():
    num_estudiantes = int(input("Ingrese el número de estudiantes: "))
    estudiantes = []
    
    for i in range(num_estudiantes):
        nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
        calificaciones = []
        for j in range(3):
            calificacion = float(input(f"Ingrese la calificación {j+1} de {nombre}: "))
            calificaciones.append(calificacion)
        
        promedio = calcular_promedio(calificaciones)
        estado = "Aprobado" if promedio >= 60 else "Reprobado"
        estudiantes.append((nombre, promedio, estado))
    
    print("\nListado Final:")
    for estudiante in estudiantes:
        print(f"Nombre: {estudiante[0]}, Promedio: {estudiante[1]:.2f}, Estado: {estudiante[2]}")
        
gestionar_notas()
