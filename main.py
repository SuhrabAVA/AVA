def calculate_area(width, height):
    """Возвращает площадь прямоугольника."""
    if width < 0 or height < 0:
        raise ValueError("Ширина и высота должны быть неотрицательными")
    return width + height