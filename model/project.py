__author__ = 'Maxim.Rumyantsev'
# -*- coding: utf-8 -*-

from sys import maxsize
import string

class Project:

    def __init__(self,
                 name=None,
                 #header=None,
                 #footer=None,
                 id=None):
        self.name=name
        #self.header=header
        #self.footer=footer
        self.id=id

    #отображение наших списков в консоли, смотреть можно через debug
    def __repr__(self):
        #return "%s__:__%s__:__%s__:__%s" % (self.id,self.name,self.header,self.footer )
        return "%s:%s" % (self.id,self.name)

    # сравнение по смыслу а не по физическому расположению объектов
    def __eq__(self, other):
        # в случае если идендификатор не определен он не учитывался при сравнении
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    # вычисляем по группе ключ используемый для сравнения
    # если у группы есть id то берем его  а если его нет то возвращается большое число maxsize (максимальное целое число)
    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize