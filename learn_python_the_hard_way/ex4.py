# define variables
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passanger_per_car = passengers / cars_driven


# print lines with variables in between the 2 strings
print('There are ', cars, ' cars avaliable')
print('There are only', drivers, 'drivers avaliable')
print('There will be', cars_not_driven, 'empty cars today.')
print('We can transport', carpool_capacity, 'people today')
print('We have', passengers, 'to carpool')
print('We need to put about', average_passanger_per_car, 'in each car')
