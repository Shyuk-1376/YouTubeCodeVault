import os
import json

script_path = os.path.dirname(os.path.abspath(__file__))
data_folder = os.path.join(script_path, "data")
word_data_file = os.path.join(data_folder, "word_data.json")

data_setup = {}

if not os.path.exists(word_data_file):
    with open(word_data_file, "w", encoding="utf-8") as file:
        json.dump(data_setup, file, ensure_ascii=False, indent=4)

def data_load():
    try:
        with open(word_data_file, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("파일이 손상되었거나, 존재하지 않습니다.")
        return {}

def join_word(word, meaning, tag, description):
    data = data_load()
    data[word] = {
        "meaning" : meaning,
        "tag" : tag,
        "description" : description
    }

    with open(word_data_file, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def save_word(word, meaning, tag, description, up_data=False):
    if up_data:
        data = data_load()
        if word in data:
            join_word(word, meaning, tag, description)
            print(f"'{word}'단어를 수정했습니다.")
        else:
            print(f"'{word}'단어가 존재하지 않습니다.")
    else:
        data = data_load()
        if word in data:
            print(f"'{word}'단어가 이미 존재합니다.")
        else:
            join_word(word, meaning, tag, description)
            print(f"'{word}'단어를 추가했습니다.")

def add_word(word, meaning, tag, description):
    save_word(word, meaning, tag, description, up_data=False)

def word_updata(word, meaning, tag, description):
    save_word(word, meaning, tag, description, up_data=True)

def word_delete(word):
    data = data_load()
    if word in data:
        del data[word]
        with open(word_data_file, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print(f"'{word}'단어를 삭제했습니다.")
    else:
        print(f"'{word}'단어가 존재하지 않습니다.")

def word_search(key, type):
    data = data_load()
    extract_data = []
    if type == "word":
        for i in data:
            if key == i:
                extract_data.append(i)
    else:
        for i in data:
            if key in data[i][type]:
                extract_data.append(i)
    
    return extract_data

def word_find(key):
    data = data_load()
    for i in data:
        if key == i:
            extract_data = data[key]
    
    return extract_data