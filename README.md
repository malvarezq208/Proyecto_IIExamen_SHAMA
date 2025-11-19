# 🏆 Premier League – Proyecto II usando Programación Orientada a Objetos (POO).
### Carrera: Big Data
### Curso: Programación II
### Examen II 

---

## 👥 Integrantes del Proyecto.
- **Sharon Obando Gómez** 
- **Marco Alvarez Quirós**

---

## 📝 Descripción del Proyecto.
Este repositorio corresponde al segundo examen del curso **Programación II**. El objetivo del proyecto es aplicar principios de **Programación Orientada a Objetos (POO)** para analizar un dataset de la **Premier League**.

El proyecto contiene:

📥 Cargar datos desde archivos CSV.

🧹 Limpiar y procesar la información (EDA).

📊 Generar visualizaciones utilizando matplotlib.

🧱 Modelar clases representando el dominio (jugadores, equipos, etc.).

📓 Documentar y presentar resultados con notebooks.

🖥️ (Opcional) Crear un dashboard con Streamlit.

---

## 🗂️ Estructura del Repositorio.
Premier_League/
src/
├─ clases/
│ ├─ jugador.py # class Jugador
│ └─ equipo.py # class Equipo
├─ cargaDatos/
│ ├─ cargador_datos.py # clase CargadorDatos
├─ eda/
│ ├─ procesador_eda.py #clase ProcesadorEDA
├─ visualizacion/
│ └─ visualizador.py #clase Visualizador
├── data/ # Archivos CSV
│ └── raw # Archivos CSV en crudo (premier.csv)
│ └── processed # Archivos CSV limpio(premier_clean.csv)
├── notebooks/ # Jupyter notebooks para desarrollo y presentación
│ ├─ 01_EDA.ipynb
│ └─ 02_Visualizacion.ipynb
├─ helpers /
│ └─ utilidades.py # clase utilidades (opcional)
├─ dashboard/ # Streamlit(opcional)
│ ├─ app.py # punto de entrada: `streamlit run dashboard/app.py`
└─ README.md # Documente el proyecto en un markdown

---

## 📦 Librerías Utilizadas (Visual Studio o Pycharm)

- pandas
- numpy
- matplotlib
- seaborn
- os
- streamlit

---

## 🚀 Ejecución del Proyecto

- 1. Clonar el Repositorio.
git clone <URL_DEL_REPO>
cd Premier_League

- 2. Ejecutar la clase de cargador_datos.
src/cargaDatos/cargador_datos.py

- 3. Ejecutar el procesador_eda.
src/eda/procesador_eda.py

- 4. Visualizaciones.
src/visualizacion/visualizador.py

- 5. Abrir el dashboard.
streamlit run dashboard/app.py

---

**Este proyecto es únicamente para fines académicos como parte de nuestro Examen II de Programación - Big Data.**
