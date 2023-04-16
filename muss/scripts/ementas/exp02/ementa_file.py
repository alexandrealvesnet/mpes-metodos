import json


class EmentaFile:
    @staticmethod
    def ementas_files_list(ementas_json):
        list_ementas = []
        with open(ementas_json, encoding="utf8") as f:
            ementas = json.load(f)
            for ementa in ementas:

                obj_ementa = {
                    "ementa": ementa['ementa'],
                    "file": ementa['file']
                }
                list_ementas.append(obj_ementa)
        return list_ementas
