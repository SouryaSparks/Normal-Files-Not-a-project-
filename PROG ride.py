

string = input("")
second_string = input('')
def comet_processor(istring):
    dictionary = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    data_set = []
    for x in istring:
        data_set.append(dictionary[x])
    return data_set
total_list_second = comet_processor(second_string)
total_list = comet_processor(string)
if sum(total_list_second) == sum(total_list):
    print('Approved')
else:
    print('Denied')