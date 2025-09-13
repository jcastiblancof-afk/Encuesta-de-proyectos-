# Definimos una clase para representar a cada alumno que responde la encuesta
class Estudiante:
    # Inicializa los atributos básicos del estudiante: nombre, edad y respuestas.
    def __init__(self, nombre, edad, respuestas):
        # Almacena el nombre del estudiante
        self.nombre = nombre
        # Almacena la edad (se recibe como texto y en caso de usarla como entero usariamos int)
        self.edad = edad
        # Almacena la lista de respuestas de este estudiante (una por cada pregunta)
        self.respuestas = respuestas

# la clase principal (clase Encuesta)se encarga de gestionar las preguntas
# almasena las respuestas y los metodos de salida
class Encuesta:
    # Recibe la lista de preguntas
    def __init__(self, preguntas):
        # Lista con las preguntas que se harán en la encuesta
        self.preguntas = preguntas
        # Lista para almacenar objetos "estudiantes"(cada entrada es una respuesta completa)
        self.respuestas = []  

    # esta funcion captura por consola la información de un estudiante y sus respuestas.
    def agregar_respuesta(self):
        # Indica que se va a registrar una nueva respuesta
        print("\n Nueva respuesta ")
        # Pide el nombre del estudiante
        nombre = input("Nombre del estudiante: ")
        # Pide la edad del estudiante
        edad = input("Edad: ")

        # Lista para guardar las respuestas de este estudiante
        respuestas = []
        # Revisa cada pregunta y pide una respuesta 
        for pregunta in self.preguntas:
            respuesta = input(f"{pregunta}: ")
            respuestas.append(respuesta)

        # Crea una instancia de Estudiante con los datos recolectados
        estudiante = Estudiante(nombre, edad, respuestas)
        # Añade el objeto Estudiante a la lista de respuestas de la encuesta
        self.respuestas.append(estudiante)
        # Confirma al usuario que la respuesta fue registrada
        print("\n¡Respuesta registrada!")

    # Muestra en consola todas las respuestas organizadas por estudiante.
    def mostrar_resultados(self):
        print("\n Resultados de la Encuesta ")
        # revisa cada estudiante almacenado en (self.respuestas)
        for est in self.respuestas:
            # muestra el nombre y la edad del estudiante
            print(f"\nNombre: {est.nombre} | Edad: {est.edad}")
            # Revisa las respuestas del estudiante y las muestra junto a la pregunta correspondiente
            for i, resp in enumerate(est.respuestas):
                print(f"  {self.preguntas[i]} -> {resp}")

    # cuenta cuántas veces apareció cada opción.
    def resumen(self):
        print("\n Resumen de preferencias ")
        # Para cada pregunta hacemos un conteo por opción
        for i, pregunta in enumerate(self.preguntas):
            # Diccionario para contar cada respuesta
            conteo = {}
            # Revisamos todas las respuestas de los estudiantes
            for est in self.respuestas:
                opcion = est.respuestas[i]
                conteo[opcion] = conteo.get(opcion, 0) + 1
            # Mostramos el conteo para la pregunta actual
            print(f"\nPregunta: {pregunta}")
            for opcion, cantidad in conteo.items():
                print(f"  {opcion}: {cantidad} respuesta(s)")

# bloque principal 
if __name__ == "__main__":
    # Definimos las preguntas de la encuesta 
    preguntas = [
        "¿Qué tema prefieres para el proyecto?",
        "¿Sabes trabajar en equipo? (Sí/No)",
        "¿Conoces alguna librería de Python?"
    ]

    # Creamos una instancia de Encuesta con la lista de preguntas
    encuesta = Encuesta(preguntas)
    # Mensaje de bienvenida
    print("Bienvenido al programa de Encuesta de Ideas de Proyecto\n")
    # Bucle para ir agregando respuestas hasta que el usuario decida salir
    while True:
        # Llamamos al método (la funcion "agregar_respuesta")para} que capture una nueva respuesta
        encuesta.agregar_respuesta()
        # Pregunta al usuario si desea seguir añadiendo respuestas
        continuar = input("¿Deseas agregar otra respuesta? (s/n): ").lower()
        # Si la respuesta no es "s", se sale del bucle
        if continuar != "s":
            break

    # cuando termina el ingreso de datos, mostramos los resultados y el resumen con las funciones 
    encuesta.mostrar_resultados()
    encuesta.resumen()
