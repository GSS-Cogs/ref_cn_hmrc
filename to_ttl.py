#!/bin/env python3

import csv

print("""@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xkos: <http://rdf-vocabulary.ddialliance.org/xkos#> .
@prefix ec: <https://trade.ec.europa.eu/def/cn#> .
""")

with open('cn8-hmrc.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        path = row['Notation']
        cn_year = path[:7]
        notation = f"{path[-8:-4]} {path[-4:-2]} {path[-2:]}"
        label = row['Label']
        print(f"""<https://trade.ec.europa.eu/def/{path}>
    a skos:Concept ;
    rdfs:label "{label}"@en ;
    skos:broader <https://trade.ec.europa.eu/def/{cn_year}#section_XVIII> ;
    skos:inScheme <https://trade.ec.europa.eu/def/{cn_year}> ;
    skos:notation "{notation}"^^ec:HS6 .
""")
