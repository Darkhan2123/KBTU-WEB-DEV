def squirrel_play(temperature, is_summer):
    if is_summer:
        return temperature >= 60 and temperature <= 100
    else:
        return temperature >= 60 and temperature <= 90
