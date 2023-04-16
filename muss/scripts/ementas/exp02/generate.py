"""
@Author: Alexandre
CLASSE PARA TRADUÇÃO VIA GOOGLE CLOUD API
"""

from ementa_file import EmentaFile
from scripts.ementas.punkt_sentence_token import PunktSentenceToken


class Generate:
    dataset_path = ""
    sentence_path = ""
    root_path = ""

    def __init__(self, path):
        self.root_path = path
        self.dataset_path = self.root_path + 'dataset/'
        self.sentence_path = self.root_path + 'sentences/exp02'

    def gen_files_ementas(self, dataset_json, target):
        """
        GERA OS ARQUIVOS *.br e *.pt
        """
        dataset = self.dataset_path + dataset_json
        ementas = EmentaFile.ementas_files_list(dataset)

        punkt_sentence_token = PunktSentenceToken()

        path = self.sentence_path + '/' + target + '/'

        for ementa in ementas:
            # Gera o arquivo da ementa inteira em pt_br

            texto_ementa = ementa['ementa']
            ementa_file = ementa['file']

            with open(path + ementa_file + '.br', 'w') as file_br:
                file_br.write(texto_ementa)

            # Separa a ementa em tokens de sentenças
            sentence_list = punkt_sentence_token.text_sentences_tokens(texto_ementa)
            sentences = ""
            for sentence in sentence_list:
                # Sentence PT
                sentences = sentences + (sentence + "\n")

            ementa_file = path + ementa_file + '.pt'
            with open(ementa_file, 'w') as file_pt:
                file_pt.write(sentences)
            print(f'### TOKENIZAÇÃO => {ementa_file} ###')
