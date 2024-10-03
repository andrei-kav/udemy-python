fav_movies = ['1st', '2nd', "3rd"]

# print(fav_movies[1])

print(f'length is {len(fav_movies)}')

# add one item at the end of a list
fav_movies.append("4th")

# add one item
# !!! the list length is 5, but 12
fav_movies.insert(12, 'some')

print(f'length is {len(fav_movies)}')

# remove the last item
del(fav_movies[len(fav_movies) - 1])

for movie in fav_movies:
    print(movie)