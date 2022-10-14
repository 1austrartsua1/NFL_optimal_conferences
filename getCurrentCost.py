from main import getCost
import pickle 

divisionsNFC = [('Philadelphia','East'),
                ('Dallas','East'),
     ('New York','East'),
     ('Washington DC','East'),
     ('San Francisco','West'),
     ('LA','West'),
     ('Phoenix','West'),
     ('Seattle','West'),
     ('minneapolis','North'),
     ('Green Bay WI','North'),
     ('Chicago','North'),
     ('Detroit','North'),
     ('Tampa Bay','South'),
     ('New Orleans','South'),
     ('Atlanta','South'),
     ('Charlotte NC','South')
]
divisionsAFC = [
    ('Buffalo','East'),
    ('New York','East'),
    ('Miami','East'),
    ('Boston','East'),
    ('Kansas City','West'),
    ('LA','West'),
    ('Denver','West'),
    ('Las Vegas','West'),
    ('Baltimore','North'),
    ('Cleveland','North'),
    ('Cincinnati','North'),
    ('Pittsburgh','North'),
    ('Tennessee','South'),
    ('Indianapolis','South'),
    ('Jacksonville','South'),
    ('Houston','South')
]

def getCurrCost(divisions,lat_long):
    div2num = {'North':0,'East':4,'South':8,'West':12}
    total = 0.
    for (city,div) in divisions:
        lat,long = lat_long[city]
        total += getCost(lat,long,div2num[div])
    return total

if __name__ == '__main__':
    with open('lat_longNFC.pickle','rb') as file:
        lat_long = pickle.load(file)
    print('NFC curr cost:',getCurrCost(divisionsNFC,lat_long))

    with open('lat_longAFC.pickle','rb') as file:
        lat_long = pickle.load(file)
        print('AFC curr cost:',getCurrCost(divisionsAFC,lat_long))
