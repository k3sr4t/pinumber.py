pifloat = 3.14159265358979323846264
pi = "3.14159265358979323846264"
pismal = "3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328"
pibig = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989"
π = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989"
pieasy = 3.14
pifr = 22/7
piday= ("march 14")





def pidigit(digit):
    somedigitofpi = pibig[:digit + 1]
    x = float(somedigitofpi)
    print(x)
    return somedigitofpi


def circle(r):
    print(pifloat*r*2)


def circlearea(r):
    print(pifloat*r**2)

def circlecube(r):
    print(4/3*pifloat*r**2)
    return r 

def foundrcircler(thecirclesarea):
    def karekok_bul(numara):
        tahmin = numara
        hassasiyet = 0.000001  # İstenen hassasiyeti belirleyin
        while abs(tahmin * tahmin - numara) > hassasiyet:
            tahmin = (tahmin + numara / tahmin) / 2
        return tahmin 

    r2 = thecirclesarea / pifloat
    sonuc = karekok_bul(r2)
    print(sonuc)
    return sonuc

def cylindir(r,h):
    area = pifloat * r ** 2 * h
    print(area)
    return area

def whenisPiDay():
    print(piday)
    return piday

def creatpasswd():
    1 == 0
    