# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.


from muss.simplify import simplify_sentences
from muss.utils.helpers import read_lines
import glob
import natsort


class SimplifySentence:

    path_muss = ""

    def __init__(self, path):
        self.path_muss = path

    def simplify(self):
        # Agrupa os arquivos tokenizados
        files_pt = []
        for file in glob.glob(self.path_muss + "/*.pt"):
            files_pt.append(file)
        files_pt = natsort.natsorted(files_pt)

        # Realiza a simplificação de cada ementa
        for ementa in files_pt:
            source_sentences = read_lines(ementa)
            pred_sentences = simplify_sentences(source_sentences, model_name='muss_pt_mined')
            file_ms = ementa.replace(".pt", ".ms")
            file_sp = ementa.replace(".pt", ".sp")

            sentences_sp = ""
            sentences_ms = ""
            # c => sentença fonte
            # s => sentença simplificada
            # Remonta a sentença agrupando-as em um arquivo semelhante ao original (*.br)
            for c, s in zip(source_sentences, pred_sentences):
                sentences_sp = sentences_sp + (s + " ")
                sentences_ms = sentences_ms + (s + "\n")

            # Salva a simplificação
            with open(file_sp, 'w') as file_write_sp:
                file_write_sp.write(sentences_sp)

            with open(file_ms, 'w') as file_write_ms:
                file_write_ms.write(sentences_ms)

            print('')
            name_file = file_sp.replace(self.path_muss + "/", "")
            print(f'################# MUSS: {name_file} simplificada! ################# ')
            print('')
