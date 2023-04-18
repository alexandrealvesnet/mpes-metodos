from simplify_sentences import SimplifySentence

path_project = '/home/alexandre/Desenvolvimento/mpes-experimentos/transformers'
path_files = path_project + '/ementas/TRF5'

simplify_sentences = SimplifySentence(path_project, path_files)
simplify_sentences.simplify()
