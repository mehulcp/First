def getAllFirstElement(inputList):
    FirstElements = []
    for eachRow in inputList:
        Elements = eachRow.split(',')
        FirstElements.append(Elements[0].strip())
    
    return FirstElements

filehandle = open('movie_metadata.csv','r')
string_movie_data = filehandle.read()
movie_names = []
movie_data_all = string_movie_data.split('\n')

movie_names = getAllFirstElement(movie_data_all[1:len(movie_data_all)])
print(movie_names)