import Pylinguistics as pl
import glob
import natsort

files_br = []
for file in glob.glob("/home/alexandre/Desenvolvimento/tmp" + "/*.br"):
    files_br.append(file)
files_br = natsort.natsorted(files_br)

sum_count_words = 0
for file in files_br:

    with open(file, 'r', encoding='utf8') as file_text:
        ementa = file_text.read()  # lê o arquivo inteiro
        objpl = pl.text(ementa)
        objpl.setLanguage("pt-br")
        json_metrics = objpl.getFeatures()
        print(f"{json_metrics['word_count']}")
    sum_count_words = sum_count_words + json_metrics['word_count']
avg_words_sumaries = (sum_count_words / 100)
print(f'AVG WORD COUNT TRF5: {avg_words_sumaries}')
