import json
merge_file={}
num=1
folderPath=input()
file_name=input()
output_file_name=input()
max_file_size=int(input())
for j in range(0,100):
    try: 
        path=folderPath+"\\"+file_name+str(num)+".json"
        num=num+1
        with open(path) as file:
            data=json.load(file)
        for datas in data:
            if datas in merge_file.keys():
                merge_file[datas]=data[datas]+data[datas]
            else:
                merge_file[datas]=data[datas]
    except:
        break
output_file=folderPath+"\\"+output_file_name+".json"
with open(output_file,'w') as fp:
    json.dump(data,fp)
size=json.dumps(merge_file)
json_size=len(size)
if json_size<=max_file_size:
    print(merge_file)
else:
    print("merged file size is more than max file size")
    print(merge_file)
