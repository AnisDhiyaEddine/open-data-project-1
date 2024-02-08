genres = [ i[:-1].split(';') for i in open('datasets/FavoriteMusic.csv', 'r').readlines() ]
hapiness = [ i[:-1].split(';') for i in open('datasets/World_Happiness_Index_by_Reports_2013-2023_no_nulls.csv', 'r').readlines()]
keys1=genres.pop(0)
keys2=hapiness.pop(0)
final_data=[]

for line in genres:
    final_data+=[ hap+line[2:] for hap in hapiness if hap[0].lower()==line[1].lower()]

final_data=[ [str(i)]+final_data[i]+['\n'] for i in range(len(final_data))]
final_data.sort(key=lambda x: int(x[0]))
final_data.insert(0, ['ID','Country']+keys2[1:]+keys1[2:]+['\n'])
to_write=[ '; '.join(data) for data in final_data]

out=open('output.csv', 'w')
out.writelines(to_write)