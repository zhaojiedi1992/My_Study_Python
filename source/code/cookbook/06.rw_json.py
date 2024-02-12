import json 

def write_json(data):
    with open('w1.json','w') as f:
        json.dump(data,f)

write_json(data = {
    'name' : 'ACME',
    'shares' : 100,
    'price' : 542.23
}
)


def read_json(filename): 
    with open(filename,'r')as f:
        data = json.load(f)
        return data 
    
print(read_json('w1.json'))