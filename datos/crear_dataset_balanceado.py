"""
Script para crear un dataset balanceado (75/25) usando sobremuestreo (oversample)
para el proyecto de predicción de deserción escolar.

Autor: Sistema de Predicción de Deserción Escolar
Fecha: 22 de octubre de 2025
"""

import pandas as pd
from sklearn.utils import resample

# ═══════════════════════════════════════════════════════════════════════════
# CONFIGURACIÓN
# ═══════════════════════════════════════════════════════════════════════════

# Ruta del archivo original (Excel)
FILE_PATH = "/Users/alexandervargas/Downloads/student dropout.csv"

# Nombre del archivo de salida
OUTPUT_FILENAME = "datos_finales_75_25.csv"

# Tamaños deseados (proporción 75/25 de un total de 5000 registros)
N_SAMPLES_MAJORITY = 3750  # 75% de 5000 (Dropped_Out = False)
N_SAMPLES_MINORITY = 1250  # 25% de 5000 (Dropped_Out = True)

# Semilla aleatoria para reproducibilidad
RANDOM_STATE = 42

# ═══════════════════════════════════════════════════════════════════════════
# EJECUCIÓN
# ═══════════════════════════════════════════════════════════════════════════

print("🔄 Iniciando proceso de balanceo de datos...")
print(f"📂 Archivo fuente: {FILE_PATH}")
print(f"📊 Proporción objetivo: 75% No Desertor / 25% Desertor")
print(f"📈 Total registros objetivo: {N_SAMPLES_MAJORITY + N_SAMPLES_MINORITY}")
print("-" * 70)

# --- 1. Cargar los datos ---
try:
    print("\n🔍 Cargando archivo Excel...")
    df = pd.read_excel(FILE_PATH)
    print(f"✅ Archivo cargado con éxito: {len(df)} registros")
    
    # Mostrar distribución original
    print("\n📊 Distribución ORIGINAL:")
    print(df['Dropped_Out'].value_counts())
    print(df['Dropped_Out'].value_counts(normalize=True).apply(lambda x: f"{x*100:.2f}%"))
    
except FileNotFoundError:
    print(f"❌ Error: No se pudo encontrar el archivo '{FILE_PATH}'.")
    print("   Verifica que la ruta sea correcta.")
    exit(1)
except Exception as e:
    print(f"❌ Error al cargar el archivo: {e}")
    exit(1)

# --- 2. Separar las clases ---
print("\n🔄 Separando clases...")
df_majority = df[df['Dropped_Out'] == False]  # No desertores
df_minority = df[df['Dropped_Out'] == True]   # Desertores

print(f"   • No Desertores (False): {len(df_majority)} registros")
print(f"   • Desertores (True): {len(df_minority)} registros")

# --- 3. Aplicar Sobremuestreo (Oversample) ---
print(f"\n🔄 Aplicando sobremuestreo...")
print(f"   • Objetivo No Desertores: {N_SAMPLES_MAJORITY} registros")
print(f"   • Objetivo Desertores: {N_SAMPLES_MINORITY} registros")

df_majority_oversampled = resample(
    df_majority, 
    replace=True,                      # Permite repetir registros
    n_samples=N_SAMPLES_MAJORITY,      # Cantidad deseada
    random_state=RANDOM_STATE          # Reproducibilidad
)

df_minority_oversampled = resample(
    df_minority, 
    replace=True, 
    n_samples=N_SAMPLES_MINORITY, 
    random_state=RANDOM_STATE
)

print("✅ Sobremuestreo completado")

# --- 4. Combinar y Mezclar ---
print("\n🔄 Combinando y mezclando datos...")
df_oversampled = pd.concat([df_majority_oversampled, df_minority_oversampled])

# Mezclar aleatoriamente el dataset
df_final = df_oversampled.sample(frac=1, random_state=RANDOM_STATE).reset_index(drop=True)

print(f"✅ Dataset final creado: {len(df_final)} registros")

# --- 5. Verificar distribución final ---
print("\n📊 Distribución FINAL:")
value_counts = df_final['Dropped_Out'].value_counts()
print(value_counts)
proportions = df_final['Dropped_Out'].value_counts(normalize=True)
print(f"\nProporción:")
print(f"   • False (No Desertor): {proportions[False]*100:.2f}%")
print(f"   • True (Desertor): {proportions[True]*100:.2f}%")

# --- 6. Guardar el archivo ---
print(f"\n💾 Guardando archivo '{OUTPUT_FILENAME}'...")
df_final.to_csv(OUTPUT_FILENAME, index=False)

print("\n" + "═" * 70)
print("🎉 ¡ÉXITO!")
print("═" * 70)
print(f"✅ Archivo '{OUTPUT_FILENAME}' creado exitosamente")
print(f"📍 Ubicación: {OUTPUT_FILENAME}")
print(f"📊 Total de registros: {len(df_final)}")
print(f"📈 Proporción: {proportions[False]*100:.1f}% No Desertor / {proportions[True]*100:.1f}% Desertor")
print("\n💡 Puedes usar este archivo en tus modelos de machine learning")
print("   modificando la variable DATA_PATH en modelo_desercion_nuevo.py")
print("═" * 70)
