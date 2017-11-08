def is_usa(movielist):
    if (movielist[6] == "USA"):
        return True
    else:
        return False
    
def index_equals_str(index_lst, index, str_to_compare):
    if index_lst[index]==str_to_compare:
        return True
    else:
        return False
    

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

wonder_woman_usa = is_usa(wonder_woman)
print (wonder_woman_usa)

filehandle = open('movie_metadata.csv','r')
string_movie_data = filehandle.read()
usa_movie_data = []
movie_data_all = string_movie_data.split('\n')

for movie in movie_data_all:
    i = movie.split(',')
    if is_usa(i) == True:
        usa_movie_data.append(i[0])
    
print(usa_movie_data)