#create the destinations

destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'Sao Paulo, Brazil', 'Cairo, Egypt']

#define test traveler with current location and interests
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

#when traveler arrives at destination want to know where they are, want to know location based on index but need to retriece index first then interpret value

#function to get index of destination
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

# test: print(get_destination_index('Paris, France'))

#define a function to get traveler location
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  get_destination_index(traveler_destination)
  return get_destination_index