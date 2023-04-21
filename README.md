# Simplificação automática de textos jurídicos em português usando aprendizagem de máquina

Repositório de código da Dissertação apresentada ao programa de Mestrado em Engenharia de Software do Centro de Estudos e Sistemas Avançados do Recife – CESAR School, como requisito para a obtenção do título de Mestre em Engenharia de Software.

## Autor

* **Alexandre Marcolino Alves** ([ama2@cesar.school](mailto:ama2@cesar.school)).
* [Dissertação/Artigo](http://link-dissertacao-artigo).

## Problema

O problema ocorre no judiciário brasileiro, através da produção de textos necessários aos processos, os quais usam vocabulários complexos e jargões técnicos do meio jurídico que dificulta a leitura e o entendimento desse conteúdo, e desse modo cria uma barreira na comunicação entre o judiciário e a população.

## Objetivo

Realizar a simplificação automática de textos jurídicos escritos em língua portuguesa, utilizando algoritmos de aprendizagem de máquina, a fim de oferecer maior legibilidade aos textos existentes, bem como escalar a produção de textos simplificados. 

## Textos utilizados

Os textos usados nesse trabalho foram as ementas existentes nos acórdãos do Supremo Tribunal Federal (STF), através do dataset [RulingBR (FEIJÓ, 2021)](https://www.lume.ufrgs.br/handle/10183/230669), bem como as ementas dos julgamentos do Tribunal Regional Federal da 5ª região (TRF5) disponíveis na aplicação [Julia - Busca Fácil](https://julia.trf5.jus.br/julia/entrar).  

## Experimentos

 Ao todo quatro experimentos foram usados na pesquisa, os quais exploraram os algoritmos/modelos considerados "Estado da Arte" em Processameno de Linguagem Natural. As seções abaixo explicarão como reproduzir cada experimento de acordo com as configurações dos ambientes utilizados e propósitos desse trabalho. 

## Experimento 01 - MUSS com modelo pré-treinado em língua inglesa e camadas de tradução.

Esse experimento usou o [Mutilingual Unsipervised Sentence Simplification By Mining Paraphrases (MUSS)](https://arxiv.org/abs/2005.00352) que é um modelo de aprendizagem não supervisionada, criado pelo Facebook, utilizado para simplificação de textos, multilíngue, que usa um modelo pré-treinado sobre paráfrases obtidas através de um processo de mineração de dados na web, e tem como objetivo realizar a simplificação de sentenças.

O experimento usou os scripts já disponíveis no modelo, bem como criou e/ou ajustou scripts necessários ao processo de Identificação de Sentenças, Criação dos Arquivos, Tradução das sentenças (Inglês/Português e vice-versa) e Simplificação das Ementas.   

### Experimento 01 - Instalação

Para a instalação do experimento 01 foi utilizada uma máquina virtual, por meio do uso do Virtual Box 6.1.38, Ubuntu 22.04.1 64x, Python 3.10.6 com 16GB de RAM. Abaixo temos o processo de instalação e configuração do MUSS que também servirá para o experimento 02:   
```
git@github.com:alexandrealvesnet/mpes-experimentos.git
cd mpes-experimentos/muss
```
No diretório "muss" é necessário obter o [diretorio "resources"](https://drive.google.com/file/d/1vnmO9X9zphNur0XWhcnUxGeLOBj8o8Li/view?usp=sharing), que contém as biliotecas, bem como os modelos pré-treinados usados pelos experimentos 01 e 02, conforme imagem abaixo:

![This is an image](assets/images/resources_muss.png)

Após isso, vamos configurar o ambiente virtual do Python para instalação das dependências necessárias a esses experimentos. Isso poderá ser feito de dois modos: o primeiro pode ser feito usando o editor de código PyCharm para abrir o projeto MUSS (diretório mpes-experimentos/muss) e  configurar o interpretador Python, já o segundo utiliza a [documentação oficial](https://docs.python.org/3/tutorial/venv.html) para isso. Com o ambiente virtual devidamente configurado vamos ao processo de instalação no diretório:  
```
cd muss/
pip install -e .  # Instala as dependências previstas no arquivo "requirements.txt"
python -m spacy download pt_core_news_md # Instala o modelo spacy requerido para português 
python -m en_core_web_md # Instala o modelo spacy requerido para inglês 
```

Além das dependências padrão já existentes no projeto MUSS (requirements.txt), foram adicionadas as seguintes utilizadas no processo de simplificação/tradução: natsort, tensorboardX e transformers. A primeira usada na listagem dos arquivos de forma ordenada, a segunda por recomendação do tensorflow e a terceira utilizada pelos modelos de tradução "inglês/português" e "português/inglês".

### Experimento 01 - Simplificação das ementas

Primeiramente vamos conhecer os arquivos criados nesse processo:

* **mpes-experimentos/muss/scripts/ementas/punkt_sentence_token.py:** Classe criada para a indentificação das sentenças em uma ementa e tratamento das abraviações comuns tanto na língua portuguesa quanto no meio jurídico;
* 

## How to use
Some scripts might still contain a few bugs, if you notice anything wrong, feel free to open an issue or submit a Pull Request.

### Simplify sentences from a file using pretrained models

First, download the template of the desired language in the folder `resources/models`. Pretrained models should be downloaded automatically, but you can also find them here:

[muss_en_wikilarge_mined](https://dl.fbaipublicfiles.com/muss/muss_en_wikilarge_mined.tar.gz)  
[muss_en_mined](https://dl.fbaipublicfiles.com/muss/muss_en_mined.tar.gz)  
[muss_fr_mined](https://dl.fbaipublicfiles.com/muss/muss_fr_mined.tar.gz)  
[muss_es_mined](https://dl.fbaipublicfiles.com/muss/muss_es_mined.tar.gz)  
[muss_pt_mined](https://drive.google.com/uc?export=download&id=1QcSHDjTtsBYSX95NvL_gefrQ2IkzpH-4) 

Then run the command:
```python
python scripts/simplify.py FILE_PATH_TO_SIMPLIFY --model-name MODEL_NAME

# English
python scripts/simplify.py scripts/examples.en --model-name muss_en_wikilarge_mined
# French
python scripts/simplify.py scripts/examples.fr --model-name muss_fr_mined
# Spanish
python scripts/simplify.py scripts/examples.es --model-name muss_es_mined
# Portuguese
python scripts/simplify.py scripts/examples.pt --model-name muss_pt_mined
``` 

### Mine the data
If you are going to add a new language to this project, in folder `resources/models/language_models/wikipedia` donwload the files of the target language from https://huggingface.co/edugp/kenlm/tree/main/wikipedia. These language models are used to filter high quality sentences in the paraphrase mining phase.

To run paraphrase mining run the command below:

```python
python scripts/mine_sequences.py
```

### Train the model
```python
python scripts/train_model.py NAME_OF_DATASET --language LANGUAGE
```

### Evaluate simplifications
Please head over to [EASSE](https://github.com/feralvam/easse/) for Sentence Simplification evaluation.


## License

The MUSS license is CC-BY-NC. See the [LICENSE](LICENSE) file for more details.

## Authors

* **Louis Martin** ([louismartincs@gmail.com](mailto:louismartincs@gmail.com))
* **Raphael Assis** ([contato.raphael.assis@gmail.com](mailto:contato.raphael.assis@gmail.com))


## Citation

If you use MUSS in your research, please cite [MUSS: Multilingual Unsupervised Sentence Simplification by Mining Paraphrases](https://arxiv.org/abs/2005.00352)

```
@article{martin2021muss,
  title={MUSS: Multilingual Unsupervised Sentence Simplification by Mining Paraphrases},
  author={Martin, Louis and Fan, Angela and de la Clergerie, {\'E}ric and Bordes, Antoine and Sagot, Beno{\^\i}t},
  journal={arXiv preprint arXiv:2005.00352},
  year={2021}
}
```
