import sys, hashlib, getpass

def get_hashed_text(text:str):
    return hashlib.sha256(text.encode()).hexdigest()

while 1:
   key = getpass.getpass('[+] Enter key: ')
   if get_hashed_text(key) != '477a4494a9b8bd2e6ad0eeeb6ecd6aa7d16a5b5f161c954d76b96a7eb311325c':
      sys.stderr,write(f'your given key "{key}" is incorrect.\n')
   
   else:
       break
	   
# Our main function 
print('Hello there!')
print('Welcome to this SMS BOMBEING TOOL👹👹,')
print('You are seeing this because you passed the key verification')

ⴣⴭⴭⴭⴭ⁻䑁䥍⁎义但素ⴭⴭⴭⴭⴭ⌊䄠呕佈⁒†刺䙁义䬠䅈੎‣䕔䵁†䄠呕佈⁒›䅒䥆੎ⴣⴭⴭⴭⴭⴭⴭⴭⴭⴭⴭⴭⴭⴭⴭⴭ‭ਊ浩潰瑲猠獹椊灭牯⁴楴敭椊灭牯⁴獯椊灭牯⁴敲畱獥獴椊灭牯⁴浳灴楬੢漊⹳祳瑳浥∨摸ⵧ灯湥栠瑴獰⼺眯睷昮捡扥潯⹫潣⽭牰景汩⹥桰㽰摩ㄽ〰㠰㌰㐶㔳㠴㌶洦扩硥楴㵤扚䭗䱷⤢ਠ獯献獹整⡭挢敬牡⤢搊晥猠睬氨㨩 映牯椠椠⁮㩬 †猠
