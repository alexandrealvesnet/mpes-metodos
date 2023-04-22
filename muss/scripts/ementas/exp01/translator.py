"""
@Author: Alexandre
CLASSE PARA TRADUÇÃO
"""

from transformers import pipeline
from ementa_file import EmentaFile
from scripts.ementas.punkt_sentence_token import PunktSentenceToken
import glob
import natsort


class Translator:
    client = ""
    path_dataset = ""
    sentence_path = ""

    def __init__(self, path_translator):

        self.path_dataset = '/home/alexandre/Desenvolvimento/mpes-experimentos/muss/scripts/ementas/dataset/'
        self.sentence_path = '/home/alexandre/Desenvolvimento/mpes-experimentos/muss/scripts/ementas/sentences/exp01/' + path_translator

    def opus_model_translate_text(self, sentence, tgt="pt"):
        sentence = sentence.lower()
        retorno = ""
        if tgt == "en":  # English
            pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-mul-en")
            translated = pipe(sentence)
            retorno = translated[0]['translation_text']

        else:  # Portuguese
            pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-en-pt")
            texto = pipe(">>por<<" + sentence)
            retorno = texto[0]['translation_text']
        return retorno

    def gen_files_ementas_sentences_trf5_stf(self, acordaos_json):
        """
        USADA PARA GERAR OS ARQUIVOS APARTIR DO DATASET JSON DAS 100 EMENTAS TRF5/STF
        """
        dataset = self.path_dataset + acordaos_json
        punkt_sentence_token = PunktSentenceToken()
        ementas, files = EmentaFile.ementas_files_list(dataset)
        for ementa, file in zip(ementas, files):
            # Gera o arquivo da ementa inteira em pt_br
            with open(self.sentence_path + '/' + str(file) + '.br', 'w') as file_pt:
                file_pt.write(ementa)

            # Separa a ementa em tokens de sentenças
            sentence_list = punkt_sentence_token.text_sentences_tokens(ementa)
            cont_sentence = 1
            for sentence in sentence_list:
                # Sentence PT
                sentence_pt = self.sentence_path + '/' + file + '.' + str(cont_sentence) + '.pt'

                with open(sentence_pt, 'w') as file_sentence_pt:
                    file_sentence_pt.write(sentence)

                # Sentence EN
                sentence_en = self.sentence_path + '/' + file + '.' + str(cont_sentence) + '.en'
                with open(sentence_en, 'w') as file_sentence_en:
                    new_sentence_list = punkt_sentence_token.adjust_first_character(sentence)
                    character = new_sentence_list[0]
                    new_sentence = new_sentence_list[1]
                    sentence_en_us = self.get_sentence_translate(new_sentence, "en-US")
                    sentence_en_us = character + sentence_en_us
                    file_sentence_en.write(sentence_en_us)
                print(f'### TRADUÇÃO/TOKENIZAÇÃO => Ementa: {file}.{cont_sentence} ###')
                cont_sentence = cont_sentence + 1


    def gen_file_translate_pt(self):
        """
        FAZ O MERGE DAS PARTES E TRADUZ PARA PORTUGUÊS
        """

        # PEGAR O CONJUNTO DE EMENTAS EM UMA LISTA (.br)
        files_br = []
        for file in glob.glob(self.sentence_path + "/*.br"):
            files_br.append(file)
        files_br = natsort.natsorted(files_br)

        root_name_list_final = []
        for file in files_br:
            root_name = file.replace(self.sentence_path + "/", "")
            root_name_list = root_name.split(".")
            root_name_list_final.append(root_name_list[0])
        root_name_list_final = list(set(root_name_list_final))
        root_name_list_final = natsort.natsorted(root_name_list_final)

        # PEGAR A LISTA DE ARQUIVOS SIMPLIFICADOS (.ms)
        files_ms = []
        for file in glob.glob(self.sentence_path + "/*.ms"):
            files_ms.append(file)
        files_ms = natsort.natsorted(files_ms)

        for root_file in root_name_list_final:
            text = ""
            # Evitar condição igual para ementa_1 ementa_11 ementa_10
            root_file = root_file + "."

            for file in files_ms:
                if root_file in file:
                    with open(file, 'r') as file_ms:
                        file_text_ms = file_ms.read()

                        file_text_td = self.get_sentence_translate(file_text_ms, "pt-BR")
                        # strip() equivale ao trim()
                        text = text + file_text_td.strip() + " "
                        file_name_td = file.replace(".ms", ".td")
                        with open(file_name_td, 'w') as file_td:
                            file_td.write(file_text_td)

            with open(self.sentence_path + '/' + root_file + 'simplificada.sp', 'w') as file_sp:
                file_sp.write(text)
                print(f'### {root_file}br simplificada ###')

    def get_sentence_translate(self, sentence, tgt="en-US"):

        if tgt == "en-US":
            tgt = "en"
        else:
            tgt = "pt"
        sentence_en_us = self.opus_model_translate_text(sentence, tgt)
        return sentence_en_us
