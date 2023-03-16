# Write your solution here
def anagrams(string1: str, string2: str):
    return sorted(string1) == sorted(string2)

if __name__ == "__main__":
    print(anagrams('house','esuoh'))