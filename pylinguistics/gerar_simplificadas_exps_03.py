import glob
import natsort

# path = '/home/alexandre/Desenvolvimento/MussExperiments/results/exp03_100_ementas_sentencas_512_STF'
path = '/home/alexandre/Desenvolvimento/MussExperiments/results/exp03_100_ementas_sentencas_512_TRF5'

files_ts = []
for file in glob.glob(path + "/*.ts"):
    files_ts.append(file)
files_ts = natsort.natsorted(files_ts)

for file_ts in files_ts:

    file_text_ts = ''
    with open(file_ts, 'r', encoding='utf8') as f_ts:
        file_text_ts = f_ts.readlines()

        text = ''
        for line in file_text_ts:
            line = line.replace('\n','')
            line = line.strip()
            text = text + line + ' '
        text = text.strip()
        file_sp = file_ts.replace('.ts','.sp')
        with open(file_sp, 'w') as f_sp:
            f_sp.write(text)