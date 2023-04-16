from generate import Generate

path = '/home/alexandre/Desenvolvimento/mpes-experimentos/muss/scripts/ementas/'

dataset = 'dataset_100_sentencas_STF.json'

generate = Generate(path)
generate.gen_files_ementas(dataset, 'STF')
