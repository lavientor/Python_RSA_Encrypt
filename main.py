# [목표]
# ID.txt를 읽어들여서 암호화하고 result_ID.txt를 만들자
# PW.txt를 읽어들여서 암호화하고 result_PW.txt를 만들자


# [환경설정]
# pip install pycryptodome

# [동작설명]
# 1. [0] 단계를 실행하면 공개키, 비밀키가 생성
#    1회 생성 후 주석처리 시, 동일한 공개키를 사용
#    세션키가 랜덤이므로 암호화 결과는 매번 달라짐

# 2. [1] 단계를 통한 result_ID.txt 생성
# 3. [2] 단계를 통한 result_PW.txt 생성



# [import]
import libraryRSA  # 커스텀

# [0] RSA 키 생성
libraryRSA.generateRSA_keys()

# [1] ID.txt
results = []
with open("ID.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        # print(line,end='')
        ciphertext,tag = libraryRSA.encryptRSA(line)
        results.append(ciphertext)

with open("result_ID.txt", 'w') as f:
    for result in results:
        f.write(str(result)+'\n')



# [2] PW.txt
# 2020년 최빈사용 암호 리스트를 샘플로 사용
# https://github.com/danielmiessler/SecLists/blob/master/Passwords/2020-200_most_used_passwords.txt
results = []
with open("PW.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        # print(line,end='')
        ciphertext,tag = libraryRSA.encryptRSA(line)
        results.append(ciphertext)

with open("result_PW.txt", 'w') as f:
    for result in results:
        f.write(str(result)+'\n')