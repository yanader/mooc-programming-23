# Write your solution here
def longest_series_of_neighbours(my_list: list):
    currentSeries = 1
    longestSeries = 0
    i = 0
    while i < len(my_list)-1:
        if my_list[i]+1 == my_list[i+1] or my_list[i]-1 == my_list[i+1]:
            currentSeries +=1
        else:
            if currentSeries > longestSeries:
                longestSeries = currentSeries
            currentSeries = 1
        i+=1
        if currentSeries > longestSeries:
                longestSeries = currentSeries
    return longestSeries

if __name__ == "__main__":
    print(longest_series_of_neighbours([1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25]))
   