#!/usr/bin/python
# -*- coding: utf8 -*-

import codecs

kursevi = [
    {"title": u"Information Security", "path": "IB", "curriculum": "SIT", "code": "SIxxxx", "people": u'"Goran Sladić", "Aleksandar Nikolić"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"Domain-Specific Languages", "path": "JSD", "curriculum": "E2, SIIT", "code": "SIxxxx", "people": u'"Igor Dejanović", "Željko Vuković"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"Software Configuration Management", "path": "UKS", "curriculum": "E2, SIIT", "code": "SIxxxx", "people": u'"Igor Dejanović", "Željko Vuković"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"Introduction to Programming (GRID)", "path": "OPG", "curriculum": "GRID", "code": "SIxxxx", "people": u'"Vuk Malbaša"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"Fundamentals of Information Systems and Software Engineering", "path": "OISISI", "curriculum": "E2", "code": "SIxxxx", "people": u'"Branko Perišić", "Petar Bjeljac"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"Operating Systems", "path": "OS", "curriculum": "SIIT", "code": "SIxxxx", "people": u'"Goran Savić"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"Web Design (ANI)", "path": "WDA", "curriculum": "ANI", "code": "SIxxxx", "people": u'"Dušan Okanović"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"Web Design (GRID)", "path": "WDG", "curriculum": "GRID", "code": "SIxxxx", "people": u'"Dušan Okanović"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"Numerical Algorithms and Numerical Software", "path": "NANSI", "curriculum": "E2, SIIT", "code": "SIxxxx", "people": u'"Aleksandar Kovačević", "Marko Jocić"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"Web Programming", "path": "WP", "curriculum": "E2, SIIT", "code": "SIxxxx", "people": u'"Milan Vidaković", "Valentin Penca"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"Software Specification and Modeling", "path": "SIMS", "curriculum": "SIIT", "code": "SIxxxx", "people": u'"Gordana Milosavljević", "Sebastijan Kaplar", "Miloš Simić"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"Software Specification and Modeling", "path": "SIMSE2", "curriculum": "E2", "code": "SIxxxx", "people": u'"Branko Perišić", "Petar Bjeljac"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"E-Payment Systems", "path": "SEP", "curriculum": "E2, SIIT", "code": "SIxxxx", "people": u'"Goran Sladić", "Nikola Luburić"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"Data Mining", "path": "SIAP", "curriculum": "E2, SIIT", "code": "SIxxxx", "people": u'"Aleksandar Kovačević", "Jelena Slivka"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"Document Management Systems", "path": "UDD", "curriculum": "E2, SIIT", "code": "SIxxxx", "people": u'"Dragan Ivanović", "Renata Vaderna"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"Methodologies for Rapid Software Development", "path": "MBRS", "curriculum": "E2, SIIT", "code": "SIxxxx", "people": u'"Gordana Milosavljević", "Željko Ivković"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"Protection and Recovery of Software Systems", "path": "ZOSS", "curriculum": "E2, SIIT", "code": "SIxxxx", "people": u'"Branko Perišić", "Petar Bjeljac"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"Software Standardization ang Quality", "path": "SKS", "curriculum": "E2, SIIT", "code": "SIxxxx", "people": u'"Branko Perišić", "Petar Bjeljac"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"XML and Web Services", "path": "XWS", "curriculum": "E2, SIIT", "code": "SIxxxx", "people": u'"Branko Milosavljević", "Stevan Gostojić", "Milan Segedinac", "Jelena Slivka", "Igor Cverdelj-Fogaraši"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"Security in E-Business Systems", "path": "BSEP", "curriculum": "E2", "code": "SIxxxx", "people": u'"Goran Sladić", "Nikola Luburić"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"Distributed Artificial Intelligence and Intelligent Agents", "path": "DVIIA", "curriculum": "E2", "code": "SIxxxx", "people": u'"Milan Vidaković", "Nikola Luburić"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"Introduction to Computing", "path": "OR", "curriculum": "BIO", "code": "SIxxxx", "people": u'"Stevan Gostojić", "Vuk Malbaša"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"Computing in Practice", "path": "RP", "curriculum": "GI", "code": "GI100", "people": u'"Valentin Penca", "Siniša Nikolić"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"Introduction to Information Technologies in Geomatics", "path": "UITG", "curriculum": "GEO", "code": "GI111", "people": u'"Dušan Okanović", "Jelena Slivka"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"Web Design", "path": "WDS", "curriculum": "SIT", "code": "ISIT2D", "people": u'"Miroslav Zarić"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"Internet Software Architectures", "path": "ISA", "curriculum": "E2, SIIT", "code": "RI41", "people": u'"Branko Milosavljević", "Igor Cverdelj-Fogaraši", "Željko Ivković"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"Software Design", "path": "PS", "curriculum": "E2", "code": "RI45", "people": u'"Branko Perišić", "Igor Zečević"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"Introduction to Programming", "path": "OP", "curriculum": "SIIT", "code": "SE0001", "people": u'"Branko Milosavljević", "Milan Segedinac"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"Object Oriented Programming 1", "path": "OOP1", "curriculum": "SIIT", "code": "SE0006", "people": u'"Milan Vidaković", "Nikola Nikolić"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"Algorithms and Data Structures", "path": "ASP", "curriculum": "SIIT", "code": "SE0008", "people": u'"Branko Milosavljević", "Dejan Mijić"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"Introduction to Software Engineering", "path": "USI", "curriculum": "SIIT", "code": "SE0011", "people": u'"Branko Perišić", "Petar Bjeljac"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"Platforms for Object Oriented Programming", "path": "PZOP", "curriculum": "SIT", "code": "SIT020", "people": u'"Goran Savić"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"Fundamentals of Software Architectures", "path": "OSA", "curriculum": "SIT", "code": "SIT027", "people": u'"Dragan Ivanović"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"Technologies and Platforms for Managing Digital Contents and Documents", "path": "TPUDSD", "curriculum": "SIT", "code": "SIT032", "people": u'"Dragan Ivanović"', "canvas": "https://enastava.io/courses/123"},
    {"title": u"E-Learning Systems and Technologies", "path": "TSEO", "curriculum": "SIT", "code": "SIT047", "people": u'"Milan Segedinac"', "canvas": "https://enastava.io/courses/123"},
]

template = u"""
---
layout: course
title: %s
collection: courses
path: %s
name: %s
curriculum: [%s]
code: %s
people: [%s]
canvas: %s
info:
---


### Podnaslov

This page presents %s.
"""

for c in kursevi:
    with codecs.open(c["path"] + ".md", "w", encoding="utf-8") as fajl:
        print c["title"]
        string = template % (c["title"], c["path"], c["path"], c["curriculum"], c["code"], c["people"], c["canvas"], c["title"])
        fajl.write(string)