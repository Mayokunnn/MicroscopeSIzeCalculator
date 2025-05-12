def calculate_real_size(image_size_mm, magnification):
    try:
        if magnification == 0:
            return "Magnification cannot be zero"
        
        real_size_um = (image_size_mm / magnification) * 1000
        return round(real_size_um, 2)
    except Exception as e:
        return str(e)
