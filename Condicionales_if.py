cota = 1495
if cota < 500:
    print ('Estamos en el piso basal, altitud inferior a 500 metros')
elif cota > 500 and cota <= 1250:
    print ('Estamos en el piso montano, altitud entre 500 y 1250 metros')
elif cota > 1250 and cota <= 2500:
    print ('Estamos en el piso subalpino, altitud entre 1250 y 2500 metros')
elif cota > 2500 and cota <= 3000:
    print ('Estamos en el piso alpino, altitud entre 2500 y 3000 metros')
elif cota > 3000:
    print ('Estamos en el piso nival, altitud superior a 3000 metros')