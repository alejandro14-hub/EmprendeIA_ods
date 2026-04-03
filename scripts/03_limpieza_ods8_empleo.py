"""
EmprendeIA_ods · HackODS UNAM 2026
Script 03 — Limpieza ODS 8 (Empleo)
Correr desde la raíz: python scripts/03_limpieza_ods8_empleo.py
"""
import pandas as pd
from pathlib import Path

D8      = Path("datos/ods8")
OUT_DIR = D8 / "procesados"
OUT_DIR.mkdir(exist_ok=True)

# ── 1. Salario por hora por ocupación 2016-2024 ───────────────
print("📂 Cargando 8.5.1c_sh_es.csv ...")
df_sal = pd.read_csv(D8 / "8.5.1c_sh_es.csv", na_values=["NAN","ND"])
COLS = {
    "Periodo": "año",
    "Sexo|Total_Tipo_de_ocupación|Total":                       "total",
    "Sexo|Total_Tipo_de_ocupación|Directores_y_gerentes":       "directivos",
    "Sexo|Total_Tipo_de_ocupación|Profesionales_científicos_e_intelectuales": "profesionales",
    "Sexo|Total_Tipo_de_ocupación|Técnicos_y_profesionales_de_nivel_medio":   "tecnicos",
    "Sexo|Total_Tipo_de_ocupación|Trabajadores_de_los_servicios_y_vendedores_de_comercios_y_mercados": "servicios",
    "Sexo|Total_Tipo_de_ocupación|Agricultores_y_trabajadores_calificados_agropecuarios,_forestales_y_pesqueros": "agropecuarios",
    "Sexo|Total_Tipo_de_ocupación|Oficiales,_operarios_y_artesanos_de_artes_mecánicas_y_de_otros_oficios": "operarios",
    "Sexo|Total_Tipo_de_ocupación|Operadores_de_instalaciones_y_máquinas_y_ensambladores": "operadores",
    "Sexo|Total_Tipo_de_ocupación|Ocupaciones_elementales":     "elementales",
    "Sexo|Hombres_Tipo_de_ocupación|Total":                     "hombres",
    "Sexo|Mujeres_Tipo_de_ocupación|Total":                     "mujeres",
}
df_sal = df_sal.rename(columns=COLS)
keep = [c for c in COLS.values() if c in df_sal.columns]
df_sal = df_sal[keep].dropna(subset=["total"])
for c in keep[1:]:
    df_sal[c] = pd.to_numeric(df_sal[c], errors="coerce").round(2)
df_sal.to_csv(OUT_DIR / "salario_hora.csv", index=False, encoding="utf-8")
print(f"  ✅ {len(df_sal)} años → datos/ods8/procesados/salario_hora.csv")

# ── 2. Tasa desocupación histórica 1995-2020 ─────────────────
print("📂 Cargando 8.5.2(2)_sh_es.csv ...")
df_des = pd.read_csv(D8 / "8.5.2(2)_sh_es.csv", na_values=["NAN","ND"])
COLS_D = {
    "Periodo":                                  "año",
    "cvegeo":                                   "cvegeo",
    "Entidad_federativa":                       "estado",
    "Sexo|Total_Grupo_de_edad|Total":           "tasa_total",
    "Sexo|Total_Grupo_de_edad|De_15_a_24_años": "tasa_jovenes",
    "Sexo|Hombres_Grupo_de_edad|Total":         "tasa_hombres",
    "Sexo|Mujeres_Grupo_de_edad|Total":         "tasa_mujeres",
}
df_des = df_des.rename(columns=COLS_D)[list(COLS_D.values())]
for c in ["tasa_total","tasa_jovenes","tasa_hombres","tasa_mujeres"]:
    df_des[c] = pd.to_numeric(df_des[c], errors="coerce").round(4)
df_des.to_csv(OUT_DIR / "desocupacion.csv", index=False, encoding="utf-8")
print(f"  ✅ {len(df_des)} registros → datos/ods8/procesados/desocupacion.csv")

# ── 3. Informalidad trimestral 2022-2025 ─────────────────────
print("📂 Cargando Tabulado.csv ...")
df_inf_raw = pd.read_csv(D8 / "Tabulado.csv")
regs, año_actual = [], None
for _, row in df_inf_raw.iterrows():
    p = str(row["Periodo"]).strip()
    if p in ["2022","2023","2024","2025"]:
        año_actual = int(p)
    elif p in ["I","II","III","IV"] and año_actual and pd.notna(row["Total"]):
        regs.append({
            "label":   f"{año_actual}-{p}",
            "año":     año_actual, "trimestre": p,
            "total":   round(float(row["Total"]),   2),
            "hombres": round(float(row["Hombres"]), 2),
            "mujeres": round(float(row["Mujeres"]), 2),
        })
df_inf = pd.DataFrame(regs)
df_inf.to_csv(OUT_DIR / "informalidad_trimestral.csv", index=False, encoding="utf-8")
print(f"  ✅ {len(df_inf)} trimestres → datos/ods8/procesados/informalidad_trimestral.csv")

# ── 4. Desocupación mensual 2024-2026 ─────────────────────────
print("📂 Cargando Tabulado (1).csv ...")
df_d2_raw = pd.read_csv(D8 / "Tabulado (1).csv")
meses, año_actual = [], None
for _, row in df_d2_raw.iterrows():
    p = str(row["Periodo"]).strip()
    if p in ["2024","2025","2026"]:
        año_actual = int(p)
    elif año_actual and pd.notna(row["Total"]) and p not in ["Periodo","nan"]:
        try:
            meses.append({
                "label":   f"{año_actual}-{p}",
                "año":     año_actual, "mes": p,
                "total":   round(float(row["Total"]),   4),
                "hombres": round(float(row["Hombres"]), 4),
                "mujeres": round(float(row["Mujeres"]), 4),
            })
        except (ValueError, TypeError):
            continue
df_d2 = pd.DataFrame(meses)
df_d2.to_csv(OUT_DIR / "desocupacion_mensual.csv", index=False, encoding="utf-8")
print(f"  ✅ {len(df_d2)} meses → datos/ods8/procesados/desocupacion_mensual.csv")

print("\n🎉 ODS 8 completado")
sal24 = df_sal[df_sal["año"]==2024].iloc[0]
brecha = sal24["directivos"] / sal24["elementales"]
print(f"   Salario promedio/hora 2024: ${sal24.total:.2f} MXN")
print(f"   Brecha directivos/elementales: {brecha:.1f}x")
