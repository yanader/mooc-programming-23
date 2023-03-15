# Write your solution here

def same_chars(str, x, y):
    if x >= len(str) or y >= len(str):
        return False
    if str[x] == str[y]:
        return True
    else:
        return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))