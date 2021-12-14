def vahetus(a:int,b:int):
    """Kui mini suurem kui max, siis vahetame väärtuste mini ja maxi kohad omavahel
    :param int a: muutuja mini
    :param int b: muutuja maxi
    :rtype: int,int
    """
    abi=a
    a=b
    b=abi
    return a,b

def generaator(n:int,loend:list,a:int,b:int):
    """Lisame randomarvud listisse
    :param int n:
    :param list loend:
    :param int a:
    :param int b:
    :rtype list:
    """
    for i in range (n):
        loend.append(randint(a,b))
    

def jagamine(loend:list,p:list,n:list,nol:list):
    """Lisame eri listisse muutujale kui tingimused on True:
    :param list loend: arvude list
    :param list p:
    :param list n:
    :param list nol:
    :rtype list:
    """
    for el in loend:
        if el>0:
            p.append(el)
        elif:
            n.append(el)
        else:
            nol.append(el)

def keskmine(loend:list,n:list):
    """Arvutamine keskmist väärtust listist
    :param list loend:
    :param int n: list negatiivsega/positiivsega arvudega
    :rtype float:
    """
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
            kesk=round(sum/n,2)
    return kesk

def lisamine(loend:list,el:float):
    """Lisame keskmise väärtuse listisse ja sorteerime
    :param list loend:list arvudega
    :param float el: keskmised väärtused
    :rtype list:
    """
    loend.append(el)
    loend.sort()
    return loend