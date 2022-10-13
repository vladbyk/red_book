import re
from django.core.management.base import BaseCommand
from web.models import Red_book

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        list1 = []
        with open('C:\\Users\\user\\PycharmProjects\\pythonProject5\\red_book\\web\\utils\\book.txt', 'r', encoding='utf-8') as f:
            for i in f.read().split('/n'):
                list1.append(i)
        list2 = []
        for i in list1:
            for j in range(0,202):
                list3 = []
                list3.append(re.findall(r'\d{1,3}',i)[j])
                list3.append(re.findall(r'\d{1,3}\s([А-Я][а-я]+ ?-?[А-Я]?[а-я]+ ?-?[А-Я]?[а-я]+)',i)[j])
                list3.append(re.findall(r'[A-Z][a-z]+ ?-?[A-Z]?[a-z]+',i)[j])
                list3.append(re.findall(r'[a-z] ([А-Я][а-я’ўіiѐ]+ ?-?[А-Я]?[а-я’ўiіѐ]+ ?-?[А-Я]?[а-я’ўiіѐ]+)',i)[j])
                list3.append(re.findall(r'[a-z] [А-Я][а-я’ўіiѐ]+ ?-?[А-Я]?[а-я’ўiіѐ]+ ?-?[А-Я]?[а-я’ўiіѐ]+ (I{1,}V?)',i)[j])
                list2.append(list3)
        print(list2)
        for i in list2:
            Red_book(id=i[0],name=i[1],name_L=i[2],name_B=i[3],priority=i[4]).save()
