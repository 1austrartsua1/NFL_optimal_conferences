from geopy.geocoders import Nominatim
import pickle

def getLatLong(names):
    geolocator = Nominatim(user_agent='myapplication')
    lat_long = {}
    for name in names:
        location = geolocator.geocode(name)
        if location is None:
            print(name,'returned None')
        else:
            print(name,'lat:',location.raw['lat'],'long:',location.raw['lon'])
        lat_long[name] = (location.raw['lat'],location.raw['lon'])
    return lat_long
if __name__ == "__main__":
    namesNFC = ['Philadelphia',
         'Dallas',
         'New York',
         'Washington DC',
         'San Francisco',
         'LA',
         'Phoenix',
         'Seattle',
         'minneapolis',
         'Green Bay WI',
         'Chicago',
         'Detroit',
         'Tampa Bay',
         'New Orleans',
         'Atlanta',
         'Charlotte NC'
    ]
    namesAFC = [
        'Buffalo',
        'New York',
        'Miami',
        'Boston',
        'Kansas City',
        'LA',
        'Denver',
        'Las Vegas',
        'Baltimore',
        'Cleveland',
        'Cincinnati',
        'Pittsburgh',
        'Tennessee',
        'Indianapolis',
        'Jacksonville',
        'Houston'
    ]


    #lat_longNFC = getLatLong(namesNFC)
    lat_longAFC = getLatLong(namesAFC)

    with open('lat_longAFC.pickle', 'wb') as f:
        pickle.dump(lat_longAFC, f)
