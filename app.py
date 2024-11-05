import streamlit as st
import random
import math

# Generar ejercicios aleatorios de dinámica de rotación
def generar_ejercicio():
    masa = random.randint(1, 10)  # Masa en kg
    radio = random.randint(1, 5)  # Radio en m
    aceleracion_angular = round(random.uniform(0.1, 5.0), 2)  # Aceleración angular en rad/s²
    torque_correcto = masa * (radio ** 2) * aceleracion_angular
    return {
        "masa": masa,
        "radio": radio,
        "aceleracion_angular": aceleracion_angular,
        "torque_correcto": torque_correcto
    }

# Función para mostrar un ejercicio y obtener respuesta
def mostrar_ejercicio():
    st.write("## Ejercicio de Dinámica de Rotación")

    ejercicio = generar_ejercicio()
    st.write(
        f"Una rueda de masa {ejercicio['masa']} kg y radio {ejercicio['radio']} m "
        f"gira con una aceleración angular de {ej
