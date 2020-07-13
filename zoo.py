zoo = ("dog", "cat", "bear", "coyote", "zebra", "lion", "tiger", "goldfish", "cobra", "turtle")
animal_to_find = "zebra"
zoo.index(animal_to_find)
if animal_to_find in zoo:
  print("Found it!")

(animal1, animal2, animal3, animal4, animal5, animal6, animal7, animal8, animal9, animal10, ) = zoo
animal_list = []
for animal in zoo:
  animal_list.append(animal)