import json
##imoort os #uncomment to write

#This fuction returns ranks inside category
def cat_val(k):
        d = [*k.values()][0]
        return [*d['category'].values()][0]

#converts dictionary to frozen sets this needs to be done so that 
# it becomes hashable to have a immutable hash value
def dict_to_set(d):
        return frozenset(
            (k, dict_to_set(v) if isinstance(v, dict) else v)
            for k, v in d.items())

#main function for merging data
def merge_data(data):     
    data.sort(key=cat_val, reverse=True)   #sorts in reverse order based on key  
    seen = set() #tracker
    result = []
    for d in data:
        temp=d[str(*d)]['category']
        del d[str(*d)]['category']
        rep = dict_to_set(d)
        if rep in seen:
            continue
        d[str(*d)].update({'category':temp})
        result.append(d)
        seen.add(rep)

    # os.remove('outputfile.json')
    # for r in result:
    #     with open('outputfile.json', 'a') as fout:
    #         json.dump(r, fout)
    #         fout.write('\n')
    print(len(result))

if __name__ == '__main__':
    # Reads data from the file
    data=[]
    for line in open('merging_challenge_data.json', 'r'):
        data.append(json.loads(line))
    merge_data(data)
#250000 time 2.00 print 10 sec write 716 sec   memory-usage : 216 mb cpu-usage : negligible 0-1% and 7% - 12% when writing file