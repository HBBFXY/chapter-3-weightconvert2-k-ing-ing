initial_weight = 55
annual_gain = 0.5
moon_gravity_ratio = 0.165

print("年份    地球体重(kg)    月球体重(kg)")
print("-" * 40)
for year in range(1, 11):
    earth_weight = initial_weight + annual_gain * year
    moon_weight = earth_weight * moon_gravity_ratio
    print("{:<4d}    {:<13.1f}{:<.1f}".format(year, earth_weight, moon_weight))
