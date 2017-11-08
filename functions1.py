filehandle = open('movie_metadata.csv','r')
string_movie_data = filehandle.read()
#print(string_movie_data)
movie_data = []
movie_data_all = string_movie_data.split('\n')

for i in movie_data_all:
    each_movie = i.split(',')
    movie_data.append(each_movie)
    
print(movie_data[0:5])