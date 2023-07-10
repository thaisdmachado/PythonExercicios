medida = float(input('Digite uma distância em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de {:.1f} corresponde a: '.format(medida))
print('{:.3f}km'.format(km))
print('{:.2f}hm'.format(hm))
print('{:.1f}dam'.format(dam))
print('{}dm'.format(dm))
print('{}cm'.format(cm))
print('{}mm'.format(mm))