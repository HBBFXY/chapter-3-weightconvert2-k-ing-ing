initial_weight = 50
annual_gain = 0.5
moon_gravity_ratio = 0.165
moon_weight = round(earth_weight * 0.165, 3)
print("年份    地球体重(kg)    月球体重(kg)")
print("-" * 40)
for year in range(1, 11):
    earth_weight = initial_weight + annual_gain * year
    moon_weight = earth_weight * moon_gravity_ratio
    print("{:<6}{:<16.1f}{:.1f}".format(year, earth_weight, moon_weight))
