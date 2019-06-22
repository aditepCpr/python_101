Dollar = 31.30
Yen = 3.54
Won = 35.59

bath = float(input("Enter thai bath = "))
BahtTODollar = bath / Dollar
BahtTOYen = bath * Yen
BahtTOWon = bath * Won
print(bath, 'Baht =', BahtTODollar, 'Dollar')
print(bath, 'Baht =', BahtTOYen, 'Yen')
print(bath, 'Baht =', BahtTOWon, 'Won')

# Output
# 10 Baht = 0.3194888178913738 Dollar
# 10 Baht = 35.4 Yen
# 10 Baht = 355.90000000000003 Won

