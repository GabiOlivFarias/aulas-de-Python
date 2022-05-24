from mrjob.job import MRjob
import re
palavra_regex = re.compile(r'[\w']+')
class QuantidadedePalavras(MRjob):
    def mapper(self, _, linha):
        for p in palavra_regex.findall(linha):
            yield p.lower(), 1

    def reducer(self, p, qtd):
        yield p, sum(qtd)
if _name_ == '_main_':
    QuantidadedePalavra.run()
