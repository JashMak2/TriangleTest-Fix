"""Testing different triangles"""
def classify_triangle(a, b, c):
    """function for testing triangle types"""
    if a > 200 or b > 200 or c > 200:
        print("InvalidInput")
    if a <= 0 or b <= 0 or c <= 0:
        print("InvalidInput")
    if not(isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 'NotATriangle' 
    if a == b == c:
        return 'Equilateral'
    if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2):
        return 'Right'
    if a !=b and b !=c and a !=c:
        return 'Scalene'
    return 'Isoceles'
