"""
図形の面積を求める
"""

def triangle(width, height):
    """
    三角形の面積を求める
    """
    return int(width * height * 0.5)

def rectangle(width,  height):
    """
    短形の面積を求める
    """
    return width * height

def circle(redius):
    """
    円の面積を求める
    """
    return int(redius * redius * 3.14)