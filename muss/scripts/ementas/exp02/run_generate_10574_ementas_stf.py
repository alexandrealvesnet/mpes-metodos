from generate import Generate

dataset_path = '/home/alexandre/Desenvolvimento/mpes-experimentos/muss/scripts/ementas/exp02/10574_ementas_stf/dataset_10574_ementas_stf.json'
sentence_path = '/home/alexandre/Desenvolvimento/mpes-experimentos/muss/scripts/ementas/exp02/10574_ementas_stf/arquivos/'

generate = Generate(dataset_path, sentence_path)
generate.gen_10574_ementas_stf()
