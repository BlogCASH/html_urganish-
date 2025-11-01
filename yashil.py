# # # # # mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# # # # # narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
# # # # # sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat
# # # # # ismlar = [] # bo'sh ro'yxat
# # # # fruits = ['pear','banana','apple','watermelon','lemon']
# # # # print("Elementlar soni:",len(fruits)) # len(fruits) ro'yxat uzunligini qaytaradi
# # # def getArea(r,pi=3.14159):
# # #     """Doiraning yuzini qaytaruvchi funksiya"""
# # #     return pi*(r**2)

# # # def getPerimeter(r,pi=3.14159):
# # #     """Doiraning perimetrini qaytaruvchi funksiya"""
# # #     # return 2*pi*r
# # import unittest
# # from circle import getArea, getPerimeter

# # class CircleTest(unittest.TestCase):
# #     def test_area(self):
# #         self.assertAlmostEqual(getArea(10), 314.159)
# #         self.assertAlmostEqual(getArea(3),28.27431)
# #     def test_perimeter(self):
# #         self.assertAlmostEqual(getPerimeter(10), 62.8318)
# #         self.assertAlmostEqual(getPerimeter(4), 25.13272)
        
# # unittest.main())
# def tubSonmi(n):
#     if n==2 or n==3: return True
#     if n%2==0 or n<2: return False
#     for i in range(3, int(n**0.5)+1, 2):   # faqat toq sonlarni tekshiramiz
#         if n%i==0:
#             return False   
#     return True
