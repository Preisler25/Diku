#region elso Óra
def feladat1():
    print("Hello World!")
def feladat2():
    #ez egy komment
    """
    ez egy több soros komment
    alma
    """
    '''
    ez is egy több soros komment
    alma
    '''
def feladat3():
    szam = int 
    tort = float 
    szoveg = str 
def feladat4():
    igaz_hamis = bool 
    lista = list 
    konstans_list = tuple
    map = dict
def feladat5(szam1: int, szam2: int):
    osszeg = szam1 + szam2
    kulonbseg = szam1 - szam2
    szorzat = szam1 * szam2
    hatvany = szam1 ** szam2
    hanyados = szam1 / szam2
    maradek = szam1 % szam2
    egész_hányados = szam1 // szam2
def feladat6(szam: int):
    szam += 1
    szam -= 1
    szam *= 1
    szam **= 1
    szam /= 1
    szam //= 1
    szam %= 1
#endregion
#region masodik Óra
def feladat7(szam1: int, szam2: int):
    val1 = szam1 > szam2
    val2 = szam1 < szam2
    val3 = szam1 >= szam2
    val4 = szam1 <= szam2
    val5 = szam1 == szam2
    val6 = szam1 != szam2
def feladat8(szam1: int, szam2: int):
    val1 = szam1 > 0 and szam2 > 0
    val2 = szam1 > 0 or szam2 > 0
    val3 = szam1 > 0 and not szam2 > 0
    val4 = not szam1 > 0
def feladat9(list: list):
    list.append(2)
    list.append(3)
    list.insert(0, 1)
    list.remove(2)
    list.reverse()
    list.sort()
def feladat10(list1: list):
    val1 = list1[0]
    val2 = list1[-1]
    val3 = list1[0:2]
    val4 = list1[0:]
    val5 = list1[:2]
    val6 = list1[0:6:2]
    val7 = list1[::2]
    val8 = list(range(100))
def feladat11(list: list):
    print(len(list))
    for i in list:
        print(i)
    for i in range(10):
        print("Hello World!")
    for i in range(len(list)):
        print(list[i])
def feladat12(num: int):
    while num < 10:
        print("Hello World!")
        num += 1
#endregion
#region Main
def main():
    feladat1()
    feladat2()
    feladat3()
    feladat4()
    feladat5(1, 2)
    feladat6(1)
    feladat7(1, 2)
    feladat8(1, 2)
    feladat9([])
    feladat10([1])
    feladat11([1, 2, 3])
    feladat12(2)
main()
#endregion
