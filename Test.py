import json
import xml.sax
import csv


def parse_json():
    with open('daily_json.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
        for valute in data['Valute']:
            val = data['Valute'][valute]
            print(val['Name'] + ', ' + str(val['Previous']) + ', ' + str(val['Value']))


class CurrencyHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ''
        self.name = ''
        self.current = ''

    def startElement(self, tag, attributes):
        self.CurrentData = tag

    def endElement(self, tag):
        if self.CurrentData == 'Name':
            print(self.name)
        if self.CurrentData == 'Value':
            print(self.current)
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == 'Name':
            self.name = content
        if self.CurrentData == 'Value':
            self.current = str(content)


def parse_xml():
    with open('daily_utf8.xml', encoding='utf-8') as xml_file:
        parser = xml.sax.make_parser()
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)
        Handler = CurrencyHandler()
        parser.setContentHandler(Handler)
        parser.parse(xml_file)


def parse_csv():
    with open('ABBREV.csv', mode='r', encoding='utf-8') as csv_file:
        print('Калорийность пищевых продуктов и кол - во белков, жиров и углеводов на 100 г.')
        data = []
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        for row in csv_reader:
            print(f"{row['Shrt_Desc']}: {row['Energ_Kcal']} ккал, {row['Protein_(g)']} белка, "
                  f"{row['Carbohydrt_(g)']} углеводов, {row['Lipid_Tot_(g)']} жира")
        print('Стоит учесть, что при значениях <0.5 грамма на 100 грамм продукта производят округление к 0 граммов')

# Расскоментируйте функции для теста их работы
#parse_csv()
#parse_xml()
#parse_json()
