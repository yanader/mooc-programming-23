class Series:

    def __init__(self, title:str, seasons_count: int, genres:list) -> None:
        self.title = title
        self.season_count = seasons_count
        self.genres = genres
        self.ratings = []

    def rate(self, rating: int):
        self.ratings.append(rating)
    
    def average_rating(self):
        try:
            return sum(self.ratings) / float(len(self.ratings))
        except:
            pass
    
    def min_rating(self):
        return min(self.ratings)

    def __str__(self) -> str:
        if len(self.ratings) == 0:
            rating_text = 'no ratings'
        else:
            average = f'{self.average_rating():.1f}'
            rating_text = str(len(self.ratings)) + ' ratings, average ' + average + ' points'

        return self.title + ' (' + str(self.season_count) + ' seasons)' + '\n' + 'genres: ' + ', '.join(self.genres) + '\n' + rating_text
    

def minimum_grade(rating:float, series_list:list):
    return_list = []
    for series in series_list:
        if series.min_rating() > rating:
            return_list.append(series)
    return return_list


def includes_genre(genre:str, series_list:list):
    return_list = []
    for series in series_list:
        if genre in series.genres:
            return_list.append(series)
    return return_list


