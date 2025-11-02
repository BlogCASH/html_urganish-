# def darajaga_kotar(son, daraja):
#     """Sonni darajaga ko'taruvchi rekursiv funksiya."""
#     if daraja == 0:
#         return 1
#     else:
#         return son * darajaga_kotar(son, daraja - 1)
#     #  return son ** daraja
# print(darajaga_kotar(2, 10))
def parametrni_top(son):
    """Berilgan sonning raqamlar yig'indisini topuvchi rekursiv funksiya."""
    if son == 0:
        return 0
    else:
        return son % 10 + parametrni_top(son // 10)