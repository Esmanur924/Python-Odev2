# 1) Bir aracın yakıt tipine göre (benzin,dizel,lpg) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hesaplayan uygulamayı yapınız.
# benzin    : 39.35
# dizel     : 41.71
# lpg       : 20.28

benzin_fiyat=39.35
dizel_fiyat=41.71
lpg_fiyat=20.28
mesafe=int(input("Yol: "))
benzin_masraf=(mesafe*benzin_fiyat)
print(benzin_masraf)
dizel_masraf=(mesafe*dizel_fiyat)
print(dizel_masraf)
lpg_masraf=(mesafe*lpg_fiyat)
print(lpg_masraf)

# 2) Bir öğrencinin 2 vize 1 final notunu alarak ortalama hesaplayınız ve hesaplanan ortalamaya göre not aralığına karşılık gelen harf notunu yazdırınız.
#    90-100 => AA
#    80-89  => BA
#    70-79  => BB
#    60-69  => CB
#    50-59  => CC
#    40-49  => DC

vize1=70
vize2=75
final=81
ortalama=(vize1*0.3 + vize2*0.3 + final*0.4)
print(ortalama)
if 90<=ortalama<=100:
    print("AA")
if 80<=ortalama<=89:
    print("BA")
if 70<=ortalama<=79:
    print("BB")
if 60<=ortalama<=69:
    print("CB")
if 50<=ortalama<=59:
    print("CC")   
if 40<=ortalama<=49:
    print("DC")

