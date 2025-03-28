def calculate_area(shape, **params):
    if shape == "rectangle":
        return params["width"] * params["height"]
    elif shape == "circle":
        from math import pi
        return pi * (params["radius"] ** 2)
    else:
        raise ValueError("Unsupported shape")

#
#
#git remote add origin https://github.com/твой-юзернейм/твой-репозиторий.git
#git branch -M main
#git push -u origin main

#git add geometry.py
#git commit -m "Добавлена функция calculate_area"
#git push origin main