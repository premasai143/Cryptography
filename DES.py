from Crypto.Cipher import DES
import string
cnt = 0
CT = "4B518774A408E3E5"
a = string.letters + string.digits
for b in range(255):
    for c in range(255):
        for i in range(255):
            for j in range(255):
                for k in range(255):
                    for x in range(255):
                        for y in range(255):
                            for z in range(255):
                                key = chr(b)+chr(c)+chr(i)+chr(j)+chr(k)+chr(x)+chr(y)+chr(z)
                                des = DES.new(key,DES.MODE_ECB)
                                PT = des.decrypt(CT.decode("hex"))
                                if(all(d in a for d in PT)):
                                    print(cnt)
                                    print(PT)
                                    res  = open('plaintext',"a")
                                    res.write("[ "+key.encode("hex")+" : ")
                                    res.write(PT+" ]\n")
                                    res.close()
                                cnt += 1


