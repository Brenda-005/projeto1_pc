import math as m
import random as r
import datetime as d
import statistics as s
import locale as l

l.setlocale(l.LC_ALL, 'pt_BR.UTF-8')

#entradas
capital_inicial = float(input('Valor da capital inicial: '))
aporte_mensal = float(input('Valor do aporte mensal: '))
meses = int(input('Prazo (em meses): ')) 
cdi_anual = float(input('CDI anual (%): '))/100
perc_cdb = float(input('Percentual do CDI - CDB (%): '))/100
perc_lci = float(input('Percentual do CDI - LCI (%): '))/100
taxa_fii = float(input('Rentabilidade do FII (%): '))/100
meta = float(input('Meta financeira (R$): '))

#processamento - conversao CDI
cdi_mensal = m.pow((1+cdi_anual), 1/12) - 1

#total investido
total_investido = capital_inicial + (aporte_mensal * meses)

#CDB
taxa_cdb = cdi_mensal * perc_cdb
montante_cdb =(capital_inicial * m.pow((1+taxa_cdb),meses)) + (aporte_mensal * meses)
lucro_cdb = montante_cdb - total_investido
montante_cdb_liquido = total_investido + (lucro_cdb * 0.85)

#LCI
taxa_lci = cdi_mensal * perc_lci
montante_lci = (capital_inicial * m.pow((1+taxa_lci), meses)) + (aporte_mensal * meses)

#poupança
taxa_poupanca = 0.005
montante_poupanca = (capital_inicial * m.pow((1+taxa_poupanca), meses)) + (aporte_mensal * meses)

#FII
taxa_fii_mensal = taxa_fii

fii1 = (capital_inicial * m.pow((1+taxa_fii), meses) + (aporte_mensal * meses)) * (1 + r.uniform(-0.03, 0.03))
fii2 = (capital_inicial * m.pow((1+taxa_fii), meses) + (aporte_mensal * meses)) * (1 + r.uniform(-0.03, 0.03))
fii3 = (capital_inicial * m.pow((1+taxa_fii), meses) + (aporte_mensal * meses)) * (1 + r.uniform(-0.03, 0.03))
fii4 = (capital_inicial * m.pow((1+taxa_fii), meses) + (aporte_mensal * meses)) * (1 + r.uniform(-0.03, 0.03))
fii5 = (capital_inicial * m.pow((1+taxa_fii), meses) + (aporte_mensal * meses)) * (1 + r.uniform(-0.03, 0.03))

#media FII
lista_fii = [fii1,fii2,fii3,fii4,fii5]
media_fii = s.mean(lista_fii)
mediana_fii = s.median(lista_fii)
desvio_fii = s.stdev(lista_fii)
montante_fii = media_fii

#meta FII
meta_atingida = montante_fii >= meta

#media_formatada
media_fii_formatada = l.currency(media_fii, grouping=True)
mediana_fii_formatada = l.currency(mediana_fii, grouping=True)
desvio_fii_formatado = l.currency(desvio_fii, grouping=True)

#datetime
data_simulada = d.date.today()
data_resgate = data_simulada + d.timedelta(days=meses * 30)
data_simulada_formatada = data_simulada.strftime('%d/%m/%Y')
data_resgate_formatada = data_resgate.strftime('%d/%m/%Y')

#locale
valor_total = l.currency(total_investido, grouping=True)
valor_cdb = l.currency(montante_cdb_liquido, grouping=True)
valor_lci = l.currency(montante_lci, grouping=True)
valor_poupanca = l.currency(montante_poupanca, grouping=True)
valor_fii = l.currency(montante_fii, grouping=True)
valormedia_fii = l.currency(media_fii, grouping=True)
valormediana_fii = l.currency(mediana_fii, grouping=True)

#gráfico
grafico_cdb = '█' * int(montante_cdb_liquido/1000)
grafico_lci = '█' * int(montante_lci/1000)
grafico_poupanca = '█' * int(montante_poupanca/1000)
grafico_fii = '█' * int(montante_fii/1000)

#saídas
print(f'\n======== RELATÓRIO PYINVEST ========\n')
print(f'Data da simulação: {data_simulada_formatada}')
print(f'Data estimada do resgate: {data_resgate_formatada}')
print(f'Total investido: {valor_total}')
print(f'CDB: {valor_cdb}')
print(f'LCI/LCA: {valor_lci}')
print(f'Poupança: {valor_poupanca}')
print(f'FII: {valor_fii}')
print(f'Média do FII: {media_fii_formatada}')
print(f'Mediana do FII: {mediana_fii_formatada}')
print(f'Desvio do FII: {desvio_fii_formatado}')
print(f'Meta atingida: {meta_atingida}')
print('\n========GRÁFICOS========\n')
print(f'Gráfico CDB: {grafico_cdb}')
print(f'Gráfico LCI: {grafico_lci}')
print(f'Gráfico Poupança: {grafico_poupanca}')
print(f'Gráfico FII: {grafico_fii}')
