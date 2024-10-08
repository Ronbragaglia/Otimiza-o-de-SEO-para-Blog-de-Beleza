# -*- coding: utf-8 -*-
"""Otimização de SEO para Blog de Beleza"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VfCJU5Gm6cY-WsptBschy_Qo391zt6qE
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def introduction():
    print("## Introdução")
    print("Neste projeto, vamos explorar como as estratégias de SEO foram implementadas para otimizar um blog de beleza,")
    print("resultando em um aumento de 50% no tráfego orgânico.")
    print("As técnicas utilizadas incluem otimização de palavras-chave e link building.")

def strategies():
    print("## Estratégias de SEO Utilizadas")
    print("- **Otimização de Palavras-Chave:**")
    print("  - Pesquisa e seleção de palavras-chave relevantes para o nicho de beleza.")
    print("  - Inclusão de palavras-chave em títulos, descrições e conteúdo.")
    print("- **Link Building:**")
    print("  - Criação de backlinks de qualidade através de parcerias com outros blogs e influenciadores.")
    print("  - Publicação de guest posts e comentários em outros sites.")

def analyze_results():
    data = {
        'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
        'Tráfego Orgânico': [1200, 1500, 1800, 2200, 2500, 3000, 3500, 4000, 4200, 4800, 5000, 6000]
    }

    df = pd.DataFrame(data)

    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='Mês', y='Tráfego Orgânico', marker='o')
    plt.title('Aumento do Tráfego Orgânico do Blog de Beleza')
    plt.xlabel('Mês')
    plt.ylabel('Tráfego Orgânico')
    plt.grid()
    plt.xticks(rotation=45)
    plt.show()

def conclusion():
    print("## Conclusões")
    print("As estratégias de SEO implementadas resultaram em um aumento significativo do tráfego orgânico,")
    print("o que demonstra a importância da otimização de palavras-chave e da construção de links.")
    print("Para melhorias futuras, sugere-se continuar monitorando as palavras-chave e explorar novas oportunidades de link building.")

introduction()
strategies()
analyze_results()
conclusion()