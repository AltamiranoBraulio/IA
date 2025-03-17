def litros_millas(litros):
    millas =100* 1000 / 1609.344
    galones = litros / 3.785411784 
    return millas / galones

def millas_litros(millas):
    litros = 3.785411784
    kilometros = millas * 1609.344 / 1000 
    return (litros / kilometros) * 100



print (litros_millas(3.9))
print (litros_millas(7.5))
print (litros_millas(10.0))

print (millas_litros(60.3))
print (millas_litros(31.4))
print (millas_litros(23.5))
