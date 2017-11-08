def feature_counter (input_lst,index,input_str,header_row = False):
    movie_count = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for every_movie in input_lst:
        movie_detail = every_movie.split(',')
        if movie_detail[index] == input_str:
            movie_count = movie_count + 1
            
    return movie_count    

filehandle = open('movie_metadata.csv','r')
string_movie_data = filehandle.read()

movie_data_all = string_movie_data.split('\n')

num_of_us_movies = feature_counter(movie_data_all, 6 , "USA", header_row = True)
print(num_of_us_movies)