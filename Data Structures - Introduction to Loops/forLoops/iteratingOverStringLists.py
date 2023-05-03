#define list of strings
planets = ['Sun', 'Mercury', 'Venus', 'Earth', 'Mars']

#iterate of list of strings
for planet in planets:
    if (planet == 'Sun'):
        print(planet, "is not a planet.")
    else:
        print(planet, "is a planet.")

    if (planet == 'Mercury'):
        print(planet, "is closest to the Sun.")