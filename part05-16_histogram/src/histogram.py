# Write your solution here
def histogram(myString: str):
    histogram = {}
    for c in myString:
        if c not in histogram:
            histogram[c] = 0
        histogram[c]+=1
    for key in histogram:
        print(key + ' ' + '*'*histogram[key])

if __name__ == "__main__":
    histogram("abba")