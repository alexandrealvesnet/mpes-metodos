from generate import Generate

path = '/home/alexandre/Desenvolvimento/mpes-experimentos/muss/scripts/ementas/'

dataset = 'dataset_100_sentencas_TRF5.json'

generate = Generate(path)
generate.gen_files_ementas(dataset, 'TRF5')
