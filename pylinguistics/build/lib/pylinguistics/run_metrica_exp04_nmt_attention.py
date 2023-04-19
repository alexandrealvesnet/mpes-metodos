run_metrica_exp01_muss_en.py### GERA AS MÉTRICAS DE LEGIBILIDADE COM BASE NOS ARQUIVOS *.br e *.sp Original e Simplificado ###

from metrica_ementa import MetricaEmenta

# Experimento 01
metrica_ementa = MetricaEmenta("exp04_100_ementas_sentencas_512_STF")
metrica_ementa.generate_metrics_by_ementa("exp04_metricas_ementas_originais_STF.xlsx", "/*.br")
metrica_ementa.generate_metrics_by_ementa("exp04_metricas_ementas_simplificadas_STF.xlsx", "/*.sp")

