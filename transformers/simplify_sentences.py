from transformers import AutoTokenizer
from transformers import EncoderDecoderModel
from punkt_sentence_token import PunktSentenceToken
import glob
import natsort


class SimplifySentence:

    path_project = ''
    path_files = ''
    path_generate_files = ''
    trained_model = None
    tokenizer = None
    punkt_sentence = None

    def __init__(self, path_project, path_files):
        self.path_project = path_project
        self.path_files = path_files
        destino = self.path_files.split('/')
        destino = destino[-1]
        self.path_generate_files = self.path_files.replace(destino,  'GERADAS/' + destino + '/')

        saved_model = self.path_project + '/checkpoint-9000'

        model_name = 'alfaneo/bertimbaulaw-base-portuguese-cased'
        model = EncoderDecoderModel.from_encoder_decoder_pretrained(model_name, model_name)

        self.trained_model = EncoderDecoderModel.from_pretrained(saved_model)
        self.tokenizer = AutoTokenizer.from_pretrained(saved_model)

        self.trained_model.config.decoder_start_token_id = self.tokenizer.cls_token_id
        self.trained_model.config.eos_token_id = self.tokenizer.sep_token_id
        self.trained_model.config.pad_token_id = self.tokenizer.pad_token_id
        self.trained_model.config.vocab_size = model.config.encoder.vocab_size

        self.punkt_sentence = PunktSentenceToken()

    def simplify(self):
        # Realizar a simplificação
        extension = ".pt"
        files_sentences = self.get_files_sentences()
        for file in files_sentences:
            with open(file, 'r') as f:
                lines_ementa = f.readlines()

                sentences_ts = ''
                for line in lines_ementa:
                    line = line.replace("\n", "")
                    inputs = self.get_tokenizer(line)
                    output = self.get_output(inputs)

                    text = self.tokenizer.batch_decode(output, skip_special_tokens=True)
                    result = self.punkt_sentence.text_sentences_tokens(text[0])
                    sentences_ts = sentences_ts + result[0] + "\n"

                file_ts = file.replace(extension, ".ts")
                name_file = file_ts.split('/')
                name_file = name_file[-1]
                file_ts = self.path_generate_files + name_file

                with open(file_ts, 'w') as fw:
                    fw.write(sentences_ts)

        # Gerar arquivos simplificados (.sp)
        files_ts = []
        for file in glob.glob(self.path_generate_files + "*.ts"):
            files_ts.append(file)
        files_ts = natsort.natsorted(files_ts)

        for file_ts in files_ts:

            with open(file_ts, 'r', encoding='utf8') as f_ts:
                file_text_ts = f_ts.readlines()

                text = ''
                for line in file_text_ts:
                    line = line.replace('\n', '')
                    line = line.strip()
                    text = text + line + ' '
                text = text.strip()
                file_sp = file_ts.replace('.ts', '.sp')
                with open(file_sp, 'w') as f_sp:
                    f_sp.write(text)

    def get_tokenizer(self, input_text):
        return self.tokenizer([input_text], padding='max_length', max_length=512, truncation=False, return_tensors='pt')

    def get_output(self, inputs):
        return self.trained_model.generate(inputs['input_ids'],
                                                max_length=512,
                                                min_length=30,
                                                num_beams=3,
                                                length_penalty=0.8,
                                                temperature=1.0,
                                                early_stopping=True,
                                                top_k=50,
                                                do_sample=False)

    def get_files_sentences(self):
        files_sentences = []

        pathname = "{}/*{}".format(
            self.path_files,
            ".pt")

        for file in glob.glob(pathname):
            files_sentences.append(file)
        files_sentences = natsort.natsorted(files_sentences)

        return files_sentences
