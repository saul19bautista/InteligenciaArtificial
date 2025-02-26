def ejecutar():
    datos_temperatura = {
        "mañana": 20,
        "tarde": 25,
        "noche": 18
    }

    def predecir_temperatura(hora):
        return datos_temperatura.get(hora, "Hora no válida") 

    hora = "tarde"
    print(f"La temperatura promedio en la {hora} es: {predecir_temperatura(hora)}°C")

if __name__ == "__main__":
    ejecutar()
