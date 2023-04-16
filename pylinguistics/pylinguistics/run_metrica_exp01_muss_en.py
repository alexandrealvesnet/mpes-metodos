### GERA AS MÉTRICAS DE LEGIBILIDADE COM BASE NOS ARQUIVOS *.br e *.sp Original e Simplificado ###

from metrica_ementa import MetricaEmenta

# EXPERIMENTO 01 - MUSS EN
path = '/home/alexandre/Desenvolvimento/mpes-experimentos/muss/scripts/ementas/sentences/exp01/'
path_stf = path + 'STF'
path_trf5 = path + 'TRF5'

# EMENTAS STF
metrica_ementa = MetricaEmenta(path_stf)
metrica_ementa.generate_metrics_by_ementa("exp01_metricas_ementas_originais_STF.xlsx", "/*.br")
metrica_ementa.generate_metrics_by_ementa("exp01_metricas_ementas_simplificadas_STF.xlsx", "/*.sp")

# EMENTAS TRF5
metrica_ementa = MetricaEmenta(path_trf5)
metrica_ementa.generate_metrics_by_ementa("exp01_metricas_ementas_originais_TRF5.xlsx", "/*.br")
metrica_ementa.generate_metrics_by_ementa("exp01_metricas_ementas_simplificadas_TRF5.xlsx", "/*.sp")

