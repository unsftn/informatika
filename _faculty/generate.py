#!/usr/bin/python
# -*- coding: utf8 -*-

import codecs

clanovi = [
    {"title": u"Aleksandar Kaplar", "path": "AleksandarKaplar", "zvanje": "TA"},
    {"title": u"Aleksandar Kovačević", "path": "AleksandarKovacevic", "zvanje": "assistant"},
    {"title": u"Danijel Venus", "path": "DanijelVenus", "zvanje": "TA"},
    {"title": u"Dragan Ivanović", "path": "DraganIvanovic", "zvanje": "assistant"},
    {"title": u"Dragana Čalija", "path": "DraganaCalija", "zvanje": "TA"},
    {"title": u"Dušan Okanović", "path": "DusanOkanovic", "zvanje": "assistant"},
    {"title": u"Goran Savić", "path": "GoranSavic", "zvanje": "assistant"},
    {"title": u"Goran Sladić", "path": "GoranSladic", "zvanje": "assistant"},
    {"title": u"Igor Cverdelj-Fogaraši", "path": "IgorCverdeljFogarasi", "zvanje": "TA"},
    {"title": u"Igor Dejanović", "path": "IgorDejanovic", "zvanje": "assistant"},
    {"title": u"Igor Zečević", "path": "IgorZecevic", "zvanje": "TA"},
    {"title": u"Ivan Nejgebauer", "path": "IvanNejgebauer", "zvanje": "lecturer"},
    {"title": u"Jelena Slivka", "path": "JelenaSlivka", "zvanje": "assistant"},
    {"title": u"Marko Jocić", "path": "MarkoJocic", "zvanje": "TA"},
    {"title": u"Marko Marković", "path": "MarkoMarkovic", "zvanje": "PhD"},
    {"title": u"Milan Kerac", "path": "MilanKerac", "zvanje": "lecturer"},
    {"title": u"Milan Segedinac", "path": "MilanSegedinac", "zvanje": "assistant"},
    {"title": u"Milorad Filipović", "path": "MiloradFilipovic", "zvanje": "TA"},
    {"title": u"Miloš Beočanin", "path": "MilosBeocanin", "zvanje": "TA"},
    {"title": u"Miloš Simić", "path": "MilosSimic", "zvanje": "TA"},
    {"title": u"Miroslav Zarić", "path": "MiroslavZaric", "zvanje": "assistant"},
    {"title": u"Nikola Luburić", "path": "Nikola Luburic", "zvanje": "TA"},
    {"title": u"Nikola Nikolić", "path": "NikolaNikolic", "zvanje": "TA"},
    {"title": u"Petar Bjeljac", "path": "PetarBjeljac", "zvanje": "TA"},
    {"title": u"Renata Vaderna", "path": "RenataVaderna", "zvanje": "TA"},
    {"title": u"Robert Molnar", "path": "RobertMolnar", "zvanje": "TA"},
    {"title": u"Sebastijan Kaplar", "path": "SebastijanKaplar", "zvanje": "TA"},
    {"title": u"Siniša Nikolić", "path": "SinisaNikolic", "zvanje": "TA"},
    {"title": u"Stevan Gostojić", "path": "StevanGostojic", "zvanje": "assistant"},
    {"title": u"Valentin Penca", "path": "ValentinPenca", "zvanje": "assistant"},
    {"title": u"Vuk Malbaša", "path": "VukMalbasa", "zvanje": "assistant"},
    {"title": u"Željko Ivković", "path": "ZeljkoIvkovic", "zvanje": "TA"},
    {"title": u"Željko Vuković", "path": "ZeljkoVukovic", "zvanje": "TA"},
    {"title": u"Zoran Vojnović", "path": "ZoranVojnovic", "zvanje": "TA"},
    {"title": u"Đorđe Obradović", "path": "DjordjeObradovic", "zvanje": "assistant"},
]

template = u"""
---
layout: faculty
title: %s
collection: faculty
path: %s
name: %s
zvanje: %s
email: xxx@uns.ac.rs
phone: +381 21 485 xxxx
office: TMD xxx
photo: 
---

Bio: TODO

### Selected Publications

TODO
"""

for c in clanovi:
    with codecs.open(c["path"] + ".md", "w", encoding="utf-8") as fajl:
        print c["title"]
        string = template % (c["title"], c["path"], c["path"], c["zvanje"])
        fajl.write(string)

        
