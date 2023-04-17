"""
@Author: Alexandre
CLASSE PARA TRADUÇÃO VIA GOOGLE CLOUD API
"""

from ementa_file import EmentaFile
from scripts.ementas.punkt_sentence_token import PunktSentenceToken


class Generate:
    dataset_path = ""
    sentence_path = ""

    def __init__(self, dataset_path, sentence_path):
        self.dataset_path = dataset_path
        self.sentence_path = sentence_path

    def gen_files_ementas(self):
        """
        GERA OS ARQUIVOS *.br e *.pt
        """
        dataset = self.dataset_path
        ementas = EmentaFile.ementas_files_list(dataset)

        punkt_sentence_token = PunktSentenceToken()
        path = self.sentence_path

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

    def gen_10574_ementas_stf(self):
        """
        GERA OS ARQUIVOS *.br e *.pt COM UM SEQUENCIAL (ESQUEMA ARQUIVOS DATASET STF)
        """

        dataset = self.dataset_path
        ementas = EmentaFile.ementas_list(dataset)

        punkt_sentence_token = PunktSentenceToken()
        cont_ementa = 1

        for ementa in ementas:
            # Gera o arquivo da ementa inteira em pt_br
            with open(self.sentence_path + '/ementa_' + str(cont_ementa) + '.br', 'w') as file_br:
                file_br.write(ementa)

            # Separa a ementa em tokens de sentenças
            sentence_list = punkt_sentence_token.text_sentences_tokens(ementa)
            sentences = ""
            for sentence in sentence_list:
                # Sentence PT
                sentences = sentences + (sentence + "\n")

            ementa_file = self.sentence_path + '/ementa_' + str(cont_ementa) + '.pt'
            with open(ementa_file, 'w') as file_pt:
                file_pt.write(sentences)
            print(f'### TOKENIZAÇÃO => Ementa: {cont_ementa} ###')
            cont_ementa = cont_ementa + 1
