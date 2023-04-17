from generate import Generate

dataset_path = '/home/alexandre/Desenvolvimento/mpes-experimentos/muss/scripts/ementas/dataset/dataset_100_sentencas_STF.json'
sentence_path = '/home/alexandre/Desenvolvimento/mpes-experimentos/muss/scripts/ementas/sentences/exp02/STF/'

generate = Generate(dataset_path, sentence_path)
generate.gen_files_ementas()
