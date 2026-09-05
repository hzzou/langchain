import json

d = {
    "name": "周杰伦",
    "age": 11,
    "gender": "男"
}
print(str(d))
s = json.dumps(d, ensure_ascii=False)  # 不需要转化为ascii码
print(s, type(s))

arr = [
    {
        "name": "周杰伦",
        "age": 15,
        "gender": "男"
    },
    {
        "name": "蔡依林",
        "age": 41,
        "gender": "女"
    }
    ,
    {
        "name": "小明",
        "age": 34,
        "gender": "男"
    }
]

print(json.dumps(arr, ensure_ascii=False), type(json.dumps(arr, ensure_ascii=False)))

json_str = '{"name": "周杰伦", "age": 11, "gender": "男"}'
json_arr_str = '[{"name": "周杰伦", "age": 15, "gender": "男"}, {"name": "蔡依林", "age": 41, "gender": "女"}, {"name": "小明", "age": 34, "gender": "男"}]'

res_dict = json.loads(json_str)
print(res_dict, type(res_dict))

res_arr = json.loads(json_arr_str)
print(res_arr, type(res_arr))