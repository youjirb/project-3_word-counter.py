count=dict()

line = None

while line is None:
    inp = input("Enter the name of the file: ")

    try:
        file=open(inp)
        line=file.read()
    except Exception as e:
        print(f"An error occurred: {e}. Please provide a valid file name.")

words=line.split()
for word in words:
    count[word]=count.get(word,0)+1

tmp=list()

for key,value in count.items():
    tmp.append((value,key))
temp=sorted(tmp, reverse=True)
(bignum,bigword)=temp[0]
print(f"your biggest word is '{bigword}' and it occered {bignum} times\n")
tenbig=temp[:10]
print('And top 10 repeated words\n')
for k,v in tenbig:
    print(f'word: {v}\nrepeated: {k}\n')