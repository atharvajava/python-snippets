def count_substring(s, ss):
    count=0
    for i in range(0, len(s)):
        if s[i:i+len(ss)] == ss:
            count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)