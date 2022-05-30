class City:

    def __init__(self, value):
        self.value = value
        self.adjacent_cities = {}
    
    # Weighted directional graphs
    def add_route(self, vertex, weight):
        self.adjacent_cities[vertex] = weight
    
    def print_adjacent_cities(self):
        print(self.value, "neighbours: ", [(k.value,v) for k,v in self.adjacent_cities.items()])


def dijkstra_shortest_path(starting_city, final_destination):

    # Hash table for storing cheapest prices from Atlanta
    cheapest_prices_table = {}

    # Hash table for cheapest previous stopover cities for retracing the cheapest path
    cheapest_previous_stopover_city_table = {}

    unvisited_cities = []
    visited_cities = {}

    # Starting city will have 0 price in the cheapest prices table
    cheapest_prices_table[starting_city.value] = 0

    # To begin with, current city will be the source city
    current_city = starting_city

    
    # Main loop to find the cheapest distance to the destination
    while current_city:

        visited_cities[current_city.value] = True
        
        # If current city is unvisited, then remove
        if current_city in unvisited_cities:
            unvisited_cities.remove(current_city)
        
        # Checking prices from current city to all adjacent cities
        for adjacent_city, price in current_city.adjacent_cities.items():

            if adjacent_city.value not in visited_cities and adjacent_city not in unvisited_cities:
                unvisited_cities.append(adjacent_city)

            # If cheapest_prices_table.get(current_city.name):
            price_through_current_city = cheapest_prices_table[current_city.value] + price
            # else:
            #     price_through_current_city = price

            if (not cheapest_prices_table.get(adjacent_city.value)) or \
                price_through_current_city < cheapest_prices_table[adjacent_city.value]:

                cheapest_prices_table[adjacent_city.value] = price_through_current_city
                cheapest_previous_stopover_city_table[adjacent_city.value] = current_city.value
        

        # Choosing the cheapest adjacent city as our next current city
        # Trying to find the cheapest next route from our unvisited cities list, into the cheapest prices table
        if unvisited_cities:
            print([city.value for city in unvisited_cities])
            cheapest_unvisited_cities = {cheapest_prices_table[city.value]:city for city in unvisited_cities}

            print(list(cheapest_unvisited_cities.keys()))
            cheapest_unvisited_city_price = min(list(cheapest_unvisited_cities.keys()))

            current_city = cheapest_unvisited_cities[cheapest_unvisited_city_price]

        else:
            current_city = None        


    # Core algorithm ends here
    # Creating cheapest path now

    cheapest_path = []
    current_city_value = final_destination.value
    print(cheapest_previous_stopover_city_table)

    # Continue searching till current city does not equal starting city
    while current_city_value != starting_city.value:

        cheapest_path.append(current_city_value)
        current_city_value = cheapest_previous_stopover_city_table[current_city_value]
    
    # In the final, adding the starting city to our cheapest path #Fencing :D
    cheapest_path.append(current_city_value)

    return cheapest_path


atlanta = City("Atlanta")
boston = City("Boston")
chicago = City("Chicago")
denver = City("Denver")
el_paso = City("El Paso")

atlanta.add_route(boston, 100)
atlanta.add_route(denver, 160)
boston.add_route(chicago, 120)
boston.add_route(denver, 180)
chicago.add_route(el_paso, 80)
denver.add_route(chicago, 40)
denver.add_route(el_paso, 140)
el_paso.add_route(boston, 100)

atlanta.print_adjacent_cities()
boston.print_adjacent_cities()
chicago.print_adjacent_cities()
denver.print_adjacent_cities()
el_paso.print_adjacent_cities()

final_path = dijkstra_shortest_path(atlanta, el_paso)

for city in final_path[::-1]:
    print(f'{city} > ', end="")
print()