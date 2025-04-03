import data

if __name__ == "__main__":
    end, right_key = False, False
    status = 0
    while end == False:
        print("Shyuk 단어장\n<아래의 기능들 중 번호를 입력해 주세요.>\n[1] 단어추가\n[2] 단어수정\n[3] 단어삭제\n[4] 단어검색\n[5] 시스템 종료")
        print("")
        user_input = input(">>>"); word, meaning, tag, description = "", "", "", ""

        if user_input == "1":
            word = input("단어를 입력해 주세요. \n>>>")
            meaning = input("뜻을 입력해 주세요. \n>>>")
            tag = input("태그을 입력해 주세요. \n','를 이용해 다중 태그를 넣을 수 있습니다.\n<Ex. \"명사, 과일, 붉은색\"> \n>>>")
            description = input("추가적인 설명을 입력해 주세요. \n>>>")
            print("")
            data.add_word(word, meaning, tag, description)
            input("ENTER를 눌러 확인하고 넘어가기")

        elif user_input == "2":
            word = input("단어를 입력해 주세요. \n>>>")
            meaning = input("뜻을 입력해 주세요. \n>>>")
            tag = input("태그을 입력해 주세요. \n','를 이용해 다중 태그를 넣을 수 있습니다.\n<Ex. \"명사, 과일, 붉은색\"> \n>>>")
            description = input("추가적인 설명을 입력해 주세요. \n>>>")
            print("")
            data.word_updata(word, meaning, tag, description)
            input("ENTER를 눌러 확인하고 넘어가기")

        elif user_input == "3":
            word = input("삭제할 단어를 입력해 주세요. \n>>>")
            print("")
            data.word_delete(word)
            input("ENTER를 눌러 확인하고 넘어가기")

        elif user_input == "4":
            right_key = False
            key_word = []
            while right_key == False:
                key = input("검색할 단어의 키워드를 입력해주세요. \n>>>")
                print("")
                type = input("키워드를 검색할 항목에 맞는 숫자를 입력해주세요.\n[1] 단어\n[2] 뜻\n[3] 태그\n[4] 설명\n>>>")
                print("")
                if type == "1":
                    right_key = True
                    key_word = data.word_search(key, "word")
                elif type == "2":
                    right_key = True
                    key_word = data.word_search(key, "meaning")
                elif type == "3":
                    right_key = True
                    key_word = data.word_search(key, "tag")
                elif type == "4":
                    right_key = True
                    key_word = data.word_search(key, "description")
                else:
                    print("잘못 된 입력입니다.")
                    print("")

                if right_key == True:
                     for i in key_word:
                         print(i, ":", data.word_find(i))
            input("ENTER를 눌러 확인하고 넘어가기")

        elif user_input == "5":
            end = True
            print("프로그램이 종료 되었습니다.")

        else:
                    print("잘못 된 입력입니다.")
                    print("")
                    input("ENTER를 눌러 확인하고 넘어가기")