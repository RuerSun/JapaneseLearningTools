from random import choice
from os import system
import sys  

def loadHiraganaData():
    fiftyTones = {"あ": "a", "か": "ka", "さ": "sa", "た": "ta", "な": "na", "は": "ha", "ま": "ma", "や": "ya", "ら": "ra", "わ": "wa", "ん": "n",
                  "い": "i", "き": "ki", "し": "shi", "ち": "chi", "に": "ni", "ひ": "hi", "み": "mi", "り": "ri",
                  "う": "u", "く": "ku", "す": "su", "つ": "tsu", "ぬ": "nu", "ふ": "fu", "む": "mu", "ゆ": "yu", "る": "ru",
                  "え": "e", "け": "ke", "せ": "se", "て": "te", "ね": "ne", "へ": "he", "め": "me", "れ": "re",
                  "お": "o", "こ": "ko", "そ": "so", "と": "to", "の": "no", "ほ": "ho", "も": "mo", "よ": "yo", "ろ": "ro", "を": "(w)o"}
    return fiftyTones


def loadKatakanaData():
    fiftyTones = {"ア": "a", "カ": "ka", "サ": "sa", "タ": "ta", "ナ": "na", "ハ": "ha", "マ": "ma", "ヤ": "ya", "ラ": "ra", "ワ": "wa", "ン": "n",
                  "イ": "i", "キ": "ki", "シ": "shi", "チ": "chi", "ニ": "ni", "ヒ": "hi", "ミ": "mi", "リ": "ri",
                  "ウ": "u", "ク": "ku", "ス": "su", "ツ": "tsu", "ヌ": "nu", "フ": "fu", "ム": "mu", "ユ": "yu", "ル": "ru",
                  "エ": "e", "ケ": "ke", "セ": "se", "テ": "te", "ネ": "ne", "ヘ": "he", "メ": "me", "レ": "re",
                  "オ": "o", "コ": "ko", "ソ": "so", "ト": "to", "ノ": "no", "ホ": "ho", "モ": "mo", "ヨ": "yo", "ロ": "ro", "ヲ": "(w)o"}
    return fiftyTones


def loadHiraganaKatakanaData():
    fiftyTones = {"あ": "a", "か": "ka", "さ": "sa", "た": "ta", "な": "na", "は": "ha", "ま": "ma", "や": "ya", "ら": "ra", "わ": "wa", "ん": "n",
                  "い": "i", "き": "ki", "し": "shi", "ち": "chi", "に": "ni", "ひ": "hi", "み": "mi", "り": "ri",
                  "う": "u", "く": "ku", "す": "su", "つ": "tsu", "ぬ": "nu", "ふ": "fu", "む": "mu", "ゆ": "yu", "る": "ru",
                  "え": "e", "け": "ke", "せ": "se", "て": "te", "ね": "ne", "へ": "he", "め": "me", "れ": "re",
                  "お": "o", "こ": "ko", "そ": "so", "と": "to", "の": "no", "ほ": "ho", "も": "mo", "よ": "yo", "ろ": "ro", "を": "(w)o",
                  "ア": "a", "カ": "ka", "サ": "sa", "タ": "ta", "ナ": "na", "ハ": "ha", "マ": "ma", "ヤ": "ya", "ラ": "ra", "ワ": "wa", "ン": "n",
                  "イ": "i", "キ": "ki", "シ": "shi", "チ": "chi", "ニ": "ni", "ヒ": "hi", "ミ": "mi", "リ": "ri",
                  "ウ": "u", "ク": "ku", "ス": "su", "ツ": "tsu", "ヌ": "nu", "フ": "fu", "ム": "mu", "ユ": "yu", "ル": "ru",
                  "エ": "e", "ケ": "ke", "セ": "se", "テ": "te", "ネ": "ne", "ヘ": "he", "メ": "me", "レ": "re",
                  "オ": "o", "コ": "ko", "ソ": "so", "ト": "to", "ノ": "no", "ホ": "ho", "モ": "mo", "ヨ": "yo", "ロ": "ro", "ヲ": "(w)o"}
    return fiftyTones


def loadVoicedSoundData():
    voicedSound = {"が": "ga", "ぎ": "gi", "ぐ": "gu", "げ": "ge", "ご": "go", 
                   "ざ": "za", "じ": "zi", "ず": "zu", "ぜ": "ze", "ぞ": "zo", 
                   "だ": "da", "ぢ": "zi", "づ": "zu", "で": "de", "ど": "do", 
                   "ば": "ba", "び": "bi", "ぶ": "bu", "べ": "be", "ぼ": "bo", 
                   "ぱ": "pa", "ぴ": "pi", "ぷ": "pu", "ぺ": "pe", "ぽ": "po"}
    return voicedSound

def loadLongVoweldata():
    longVowel = {"あ 行": "あ", "い 行": "い", "う 行": "う", "え 行": ("え","い"), "お 行": ("お","う")}
    return longVowel


def loadProtonationData():
    protonationData={"小写的つ": "例如: あさって (明後日)[键盘键入 a sa t te], 功能是用于发音停顿"}
    return protonationData


def loadIntonationData():
    intonationData={"きゃ": "kya", "きゅ": "kyu", "きょ": "kyo", "しゃ": "sha", "しゅ": "shu", "しょ": "sho", "ちゃ": "cha", "ちゅ": "chu", "ちょ": "cho",
                     "にゃ": "nya", "にゅ": "nyu", "にょ": "nyo", "ひゃ": "hya", "ひゅ": "hyu", "ひょ": "hyo", "みゃ": "mya", "みゅ": "myu", "みょ": "myo",
                     "りゃ": "rya", "りゅ": "ryu", "りょ": "ryo", "ぎゃ": "gya", "ぎゅ": "gyu", "ぎょ": "gyo", "じゃ": "ja", "じゅ": "ju", "じょ": "jo",
                     "ぢゃ": "dya", "ぢゅ": "dyu", "ぢょ": "dyo", "びゃ": "bya", "びゅ": "byu", "びょ": "byo", "ぴゃ": "pya", "ぴゅ": "pyu", "ぴょ": "pyo"}
    return intonationData


def loadAllData():
    allData={"あ": "a", "か": "ka", "さ": "sa", "た": "ta", "な": "na", "は": "ha", "ま": "ma", "や": "ya", "ら": "ra", "わ": "wa", "ん": "n",
                    "い": "i", "き": "ki", "し": "shi", "ち": "chi", "に": "ni", "ひ": "hi", "み": "mi", "り": "ri",
                    "う": "u", "く": "ku", "す": "su", "つ": "tsu", "ぬ": "nu", "ふ": "fu", "む": "mu", "ゆ": "yu", "る": "ru",
                    "え": "e", "け": "ke", "せ": "se", "て": "te", "ね": "ne", "へ": "he", "め": "me", "れ": "re",
                    "お": "o", "こ": "ko", "そ": "so", "と": "to", "の": "no", "ほ": "ho", "も": "mo", "よ": "yo", "ろ": "ro", "を": "(w)o",
                    "ア": "a", "カ": "ka", "サ": "sa", "タ": "ta", "ナ": "na", "ハ": "ha", "マ": "ma", "ヤ": "ya", "ラ": "ra", "ワ": "wa", "ン": "n",
                    "イ": "i", "キ": "ki", "シ": "shi", "チ": "chi", "ニ": "ni", "ヒ": "hi", "ミ": "mi", "リ": "ri",
                    "ウ": "u", "ク": "ku", "ス": "su", "ツ": "tsu", "ヌ": "nu", "フ": "fu", "ム": "mu", "ユ": "yu", "ル": "ru",
                    "エ": "e", "ケ": "ke", "セ": "se", "テ": "te", "ネ": "ne", "ヘ": "he", "メ": "me", "レ": "re",
                    "オ": "o", "コ": "ko", "ソ": "so", "ト": "to", "ノ": "no", "ホ": "ho", "モ": "mo", "ヨ": "yo", "ロ": "ro", "ヲ": "(w)o",
                    "が": "ga", "ぎ": "gi", "ぐ": "gu", "げ": "ge", "ご": "go", 
                    "ざ": "za", "じ": "zi", "ず": "zu", "ぜ": "ze", "ぞ": "zo", 
                    "だ": "da", "ぢ": "zi", "づ": "zu", "で": "de", "ど": "do", 
                    "ば": "ba", "び": "bi", "ぶ": "bu", "べ": "be", "ぼ": "bo", 
                    "ぱ": "pa", "ぴ": "pi", "ぷ": "pu", "ぺ": "pe", "ぽ": "po",
                    "きゃ": "kya", "きゅ": "kyu", "きょ": "kyo", "しゃ": "sha", "しゅ": "shu", "しょ": "sho", "ちゃ": "cha", "ちゅ": "chu", "ちょ": "cho",
                    "にゃ": "nya", "にゅ": "nyu", "にょ": "nyo", "ひゃ": "hya", "ひゅ": "hyu", "ひょ": "hyo", "みゃ": "mya", "みゅ": "myu", "みょ": "myo",
                    "りゃ": "rya", "りゅ": "ryu", "りょ": "ryo", "ぎゃ": "gya", "ぎゅ": "gyu", "ぎょ": "gyo", "じゃ": "ja", "じゅ": "ju", "じょ": "jo",
                    "ぢゃ": "dya", "ぢゅ": "dyu", "ぢょ": "dyo", "びゃ": "bya", "びゅ": "byu", "びょ": "byo", "ぴゃ": "pya", "ぴゅ": "pyu", "ぴょ": "pyo"}
    return allData


def randomLoad(data):
    randomdatakey = choice(list(data.keys()))
    randomdatavalue = data[randomdatakey]
    return randomdatakey, randomdatavalue


def keyValDel(data, randomdatakey):
    del data[randomdatakey]


def trainAndcheck(randomdatakey, randomdatavalue):
    print("this time the word is : ", randomdatakey)
    # print("the word pronunciation is : ", randomdatavalue)
    if sys.stdin.isatty():
        pronunc = input("please input the Roman pronunciation : ")
    else:    
        print("无法在非终端环境中读取输入")
    pronunc = pronunc.lower()
    if pronunc==str(randomdatavalue):
        print("\nyour answer is true\n\n")
        return True
    else:
        print("your answer is error")
        print("the word correct pronunciation is : ", randomdatavalue)
        print("\n\n")
        return False


def showData(selected, data):
    count=0
    print("the whole  tones : \n") 
    for key in list(data.keys()):
        print(key,":",data[key],end=", ")
        count=count+1
        if count==10:
            count=0
            print("\n")
    if selected=='1':
        print("\n\nNotes:\n\
          \tthese words pronunciation is special:\n\n\
          'し'读:'xi', 'ち'读:'qi', 'つ'读:'ci', 'ふ'读:'fu', 'r'读:'l'\n\
          \tn 作为辅音")
    if selected=='2':
        print("\n\nNotes:\n\
          \tthese words pronunciation is special:\n\n\
          'シ'读:'xi', 'チ'读:'qi', 'ツ'读:'ci', 'フ'读:'fu', 'r'读:'l'\n\
          \tn 作为辅音")
    if selected=='4':
        print("\n\nNotes:\n\
          \tthese words pronunciation is special:\n\n\
          'じ'读:'ji', 'ぢ'读:'ji', 'ず'读:'zi', 'づ'读:'zi'\n")
    if selected=='5':
        print("\n\nNotes:\n\
          \t例如: あ 行指 か さ た な は ま や ら わ \n\
          \tあ行 + あ 发长音")
    if selected=='7':
        print('\n\nNotes:\n\
          \t"しゃ": "sya" 读:xya, "しゅ": "syu" 读:xyu, "しょ": "syo" 读:xyo, "ちゃ": "tya" 读:qya, "ちゅ": "tyu" 读:qyu, "ちょ": "tyo" 读:qyo,\n\
          \t"じゃ": "zya" 读:jya, "じゅ": "zyu" 读:jyu, "じょ": "zyo" 读:jyo, "ぢゃ": "dya" 读:jya, "ぢゅ": "dyu" 读:jyu, "ぢょ": "dyo" 读:jyo')
        
    if sys.stdin.isatty():
        input("\npress <enter> to clear these tones")
    system("cls")

def loadData(selected):
    data = []
    _data = []

    if selected == '1':
        data = loadHiraganaData()
    elif selected == '2':
        data = loadKatakanaData()
    elif selected == '3':
        data = loadHiraganaKatakanaData()
    elif selected == '4':
        data = loadVoicedSoundData()
    elif selected == '5':
        data = loadLongVoweldata()
        _data = loadHiraganaData()
    elif selected == '6':
        data = loadProtonationData()
    elif selected == '7':
        data = loadIntonationData()
    elif selected == '8':
        data = loadAllData()
    return data, _data

def runTrain(selected):
    data, _data = loadData(selected)
    if len(data) > 0:
        showData(selected, data)
    if len(_data) > 0:
        showData(selected, _data)
    while True:
        if sys.stdin.isatty():
            next = input("do you want to start the train ?(y/n)[default is y,press <enter>]: ")
        else:    
            print("无法在非终端环境中读取输入")
        
        if next.lower() == "y" or not next:
            if sys.stdin.isatty():
                times = input("input the times that you want to train[default is 10]: ")
            else:    
                print("无法在非终端环境中读取输入")
            if not times:
                times=10
            data, _data = loadData(selected)
            right=0
            error=0
            for time in range(int(times)):
                randomdatakey, randomdatavalue = randomLoad(data)
                print(f"Progress Bar: {time+1}/{times} ", "(", len(data), ")\n")
                if trainAndcheck(randomdatakey, randomdatavalue):
                    keyValDel(data, randomdatakey)
                    right=right+1
                else:
                    error=error+1
                if len(data) == 0:
                    data, _data = loadData(selected)
            print("right times: ", right)
            print("error times: ", error)
            print("accuracy: ",right/int(times))
            print("\n\n\n")
        else:
            break


def menu():
    print("==========================     MENU    ==========================")
    print("\n========== 1. 日语五十音看字识音训练(平假名)\t\t==========")
    print("\n========== 2. 日语五十音看字识音训练(片假名)\t\t==========")
    print("\n========== 3. 日语五十音看字识音训练(平假名&片假名)\t==========")
    print("\n========== 4. 日语浊音看字识音训练\t\t\t==========")
    print("\n========== 5. 日语延长音组合\t\t\t\t==========")
    print("\n========== 6. 日语促音(停顿音)组合\t\t\t==========")
    print("\n========== 7. 日语拗音看字识音训练\t\t\t==========")
    print("\n========== 8. 日语看字识音汇总训练\t\t\t==========")
    print("\n========== 0. 退出\t\t\t\t\t==========")
    print("\n\t\t\t\t\t\tPowered By Ruer")



if __name__ == "__main__":
    while True:
        menu()
        selected = input("Select your choice... [default is 0]: ")
        if selected == "0" or not selected:
            exit(0)
        if int(selected) <=8 and int(selected) >=1:
            runTrain(selected)
            
        else:
            print("**********Error,input your choice again**************\n\n")
            input("\npress <enter> to continue...")
            system("cls")
