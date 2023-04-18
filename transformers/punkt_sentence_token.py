from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters


class PunktSentenceToken:
    abbrev_list = []

    def text_sentences_tokens(self, text):
        """
        RECEBE UM TEXTO E O DIVIDE EM TOKENS DE SENTENÇAS
        :param text:
        :return: list de sentenças
        """
        abbrev_types_list = self.get_abbrev_types()
        abbrev_letters_list = self.get_abbrev_letters()
        abbrev_portuguese = self.get_abbrev_portuguese()
        numbers_list = list(range(1, 100))
        numbers_list = [str(value) for value in numbers_list]
        self.add_value_list_abbrev(numbers_list)
        self.add_value_list_abbrev(abbrev_types_list)
        self.add_value_list_abbrev(abbrev_letters_list)
        self.add_value_list_abbrev(abbrev_portuguese)
        punkt_params = PunktParameters()
        punkt_params.abbrev_types = set(self.abbrev_list)
        tokenizer = PunktSentenceTokenizer(punkt_params)
        tokens = tokenizer.tokenize(text)
        sentences_list = []
        for token in tokens:
            sentences_list.append(token)
        return sentences_list

    def adjust_first_character(self, sentence):
        """
        AJUSTAR A SENTENÇA PARA O MUSS FAZER A SIMPLIFICAÇÃO. EVITAR SITUAÇÕES COMO: “Penal.
        :param sentence:
        :return: List com a primeira posição com o caracter matche e a sentença
        """
        matches = ['"', '“', "'", "(", "-", ":"]
        adjusted_sentence = []
        exists = False

        for match in matches:
            if match == sentence[0]:
                character = sentence[0]
                new_sentence = sentence.replace(character, "", 1)
                adjusted_sentence.append(sentence[0])
                adjusted_sentence.append(new_sentence)
                exists = True
                break

        if exists is False:
            adjusted_sentence.append("")
            adjusted_sentence.append(sentence)

        return adjusted_sentence

    def add_value_list_abbrev(self, abbrev_list):
        """
        ADICIONA AO LIST DE ABREVIAÇÕES UMA NOVA LISTA DE ABREVIAÇÕES
        :param abbrev_list:
        """
        for value in abbrev_list:
            self.abbrev_list.append(value)

    def get_abbrev_types(self):
        """
        RETORNA AS ABREVIAÇÕES MAIS USADAS EM TEXTOS JURÍDICOS
        :return: list de Abreviações
        """
        return ['art', 'fl', 'fls', 'rel', 'des', 'nr', 'n', 'ex', 'min', 'agr', 'inc', 'doc', 'i', 'ii',
                'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x', 'xi', 'xii', 'xiii', 'xiv', 'xv', 'xvi'
                'xvii', 'xviii', 'xix', 'xx']

    def get_abbrev_letters(self):
        """
        RETORNA AS ABREVIAÇÕES CASO APAREÇA DESSA FORMA NO TEXTO (d., b. etc)
        :return: list de Abreviações
        """
        return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                't', 'u', 'v', 'x', 'z', 'k']

    def get_abbrev_portuguese(self):
        """
        RETORNA AS ABREVIAÇÕES MAIS COMUNS DA LÍNGUA PORTUGUESA
        :return: list de Abreviações
        """
        return ['aa', 'abr', 'abrev', 'ac', 'acad', 'adj', 'adm', 'aeron', 'ago', 'agric', 'al', 'alf',
         'álg', 'alm', 'alt', 'alv', 'am', 'anat', 'ap', 'arc', 'aritm', 'arq', 'arquit', 'art',
         'ass', 'assemb', 'assist', 'assoc', 'astr', 'át', 'atm', 'atte', 'aum', 'aut', 'aux', 'av',
         'bar', 'bibl', 'bibliog', 'bibliot', 'biofís', 'biogr', 'biol', 'bioq', 'bisp', 'bo',
         'bomb', 'bot', 'br', 'brig', 'brit', 'btl', 'buroc', 'cap', 'caps', 'cel', 'cia', 'ciênc',
         'círc', 'cit', 'clim', 'col', 'com', 'comte', 'comp', 'compl', 'cons', 'const', 'constr',
         'contab', 'cos', 'cp', 'créd', 'cron', 'cx', 'drs', 'da', 'dc', 'dd', 'dec', 'demog',
         'dep', 'deps', 'desen', 'desc', 'dez', 'dic', 'dipl', 'docs', 'Dr', 'dra', 'ee', 'ec',
         'ecf', 'ed', 'edif', 'educ', 'eg', 'elem', 'eletr', 'eletrôn', 'EM', 'em', 'Emb', 'embr',
         'eng', 'enol', 'Esc', 'esp', 'equit', 'er', 'est', 'etc', 'ex', 'fáb', 'fac', 'farm',
         'fed', 'fenôm', 'fev', 'ff', 'filos', 'fin', 'fisc', 'folc', 'for', 'form', 'fot', 'fr',
         'fss', 'fund', 'gen', 'gar', 'geneal', 'geo', 'ger', 'germ', 'gloss', 'gm', 'gov', 'gp',
         'gr', 'gráf', 'grav', 'hebr', 'her', 'herd', 'hidr', 'hig', 'hip', 'hist', 'humor', 'igr',
         'ib', 'id', 'imigr', 'impr', 'índ', 'ind', 'inform', 'jan', 'jorn', 'jr', 'jud', 'jul',
         'jun', 'jur', 'jurisp', 'just', 'lib', 'lab', 'lanç', 'larg', 'lat', 'ltda', 'leg',
         'legisl', 'mun', 'mai', 'maj', 'maiúsc', 'mal', 'mar', 'mark', 'mat', 'mec', 'med', 'méd',
         'vet', 'memo', 'mens', 'metal', 'met', 'mil', 'miner', 'mit', 'mm', 'mme', 'mob', 'mod',
         'moed', 'mon', 'mons', 'mor', 'morf', 'mus', 'mús', 'nº', 'nac', 'náut', 'naz', 'neol',
         'ns', 'sr', 'sra', 'nt', 'num', 'núm', 'ob', 'obs', 'ocid', 'odont', 'of', 'oft', 'olig',
         'ópt', 'orig', 'ord', 'org', 'ort', 'out', 'patol', 'pág', 'pag', 'pe', 'pb', 'pc', 'pç',
         'pça', 'pal', 'pals', 'par', 'pat', 'pd', 'perf', 'ex', 'abrev', 'pg', 'phd', 'pl', 'pm',
         'poét', 'pol', 'polít', 'port', 'pp', 'pq', 'pr', 'pres', 'proc', 'prod', 'prof', 'profs',
         'pron', 'os', 'psic', 'psicol', 'pt', 'qg', 'quart', 'quest', 'quím', 'quinz', 'ref', 'rg',
         'relat', 'relig', 'rem', 'rep', 'report', 'res', 'ret', 'rev', 'rod', 'rus', 'sec', 'séc',
         'sécs', 'sem', 'serv', 'set', 'exa', 'exo', 'símb', 'sra', 'sro', 'soc', 'soc', 'sr',
         'sub', 'suc', 'surr', 'tb', 'téc', 'tel', 'tem', 'teol', 'terap', 'tes', 'tip', 'tít',
         'topog', 'trad', 'transp', 'trig', 'trim', 'trop', 'tur', 'un', 'unif', 'univ', 'univers',
         'urb', 'urban', 'urol', 'urug', 'us', 'util', 'utilit', 'utop', 'va', 'voc', 'vol', 'vols',
         'vs', 'vulg', 'wc', 'xenof', 'zool']
