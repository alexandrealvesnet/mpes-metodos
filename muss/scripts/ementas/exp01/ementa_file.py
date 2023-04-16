import json


class EmentaFile:

    @staticmethod
    def ementas_files_list(acordaos_json):
        """
        USADA PARA GERAR OS ARQUIVOS DO DATASET 100 EMENTAS TRF5/STF
        """
        ementas = []
        files = []
        with open(acordaos_json, encoding="utf8") as f:
            acordaos = json.load(f)
            for acordao in acordaos:
                ementa = acordao['ementa']
                file = acordao['file']
                ementas.append(ementa)
                files.append(file)
        return ementas, files
