def get_common_movies(collections):
    for num in range(0, len(collections) - 1):
        common_movies = collections[num].intersection(collections[num + 1])
    return common_movies
