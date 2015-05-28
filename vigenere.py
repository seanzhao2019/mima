#!/usr/bin/python
#__author__ = 'zhao'
from optparse import OptionParser
import string
usage = "usage: %prog [options] arg1 [options] arg2"
parser = OptionParser(usage=usage)
parser.add_option("-k","--key",action="store", type="string", dest="keywords",default = None)
parser.add_option("-e","--encrypt",action="store", type="string", dest="plaintext",default =None)
parser.add_option("-d","--decrypt",action="store", type="string", dest="cypher",default =None)

(options, args) = parser.parse_args()


if options.keywords is not None:
   # print options.keywords
    KEY=options.keywords
    list_keywords = list(KEY)
    b = len(KEY) #keywords length b
else :
    print "please input the keywords, keywords is very important for the Vigener-ecrypt ! "

if options.plaintext is not None:
   # print options.plaintext
    PT=options.plaintext
    list_plaintext = list(PT)
    a = len(PT)  #plaintext length a

    k =list()
    en_list=list()
    i=0
    j=0
    while (a>0):
            if ((ord(list_plaintext[i])>=65)and(ord(list_plaintext[i])<=90)) :
                k.append(list_keywords[j%b].upper())
                en_list.append(chr(((ord(PT[i])-65)+(ord(k[i])-65))%26+65))
                j+=1
                i+=1

            elif ((ord(list_plaintext[i])>=97)and(ord(list_plaintext[i])<=122)) :
                k.append(list_keywords[j%b].lower())
                en_list.append(chr(((ord(PT[i])-97)+(ord(k[i])-97))%26+97))
                j+=1
                i+=1
            else :
                k.append(list_plaintext[i])
                en_list.append(list_plaintext[i])
                i+=1
            #print k
            a-=1

  #  print en_list
    en_text="".join(en_list)
    print "The ciphertext : ",en_text
    print "Congratulations ! You get it !"
#else :
  #   print "Congratulations ! You get the plaintext !"

if options.cypher is not None:
   # print options.cypher
    CP=options.cypher
    list_cypher = list(CP)
    c = len(CP) #cypther length c

    k_de =list()
    de_list=list()
    m=0
    n=0
    while (c>0):
            if ((ord(list_cypher[m])>=65)and(ord(list_cypher[m])<=90)) :
                k_de.append(list_keywords[n%b].upper())
                de_list.append(chr(((ord(CP[m])-65)-(ord(k_de[m])-65))%26+65))
                n+=1
                m+=1

            elif ((ord(list_cypher[m])>=97)and(ord(list_cypher[m])<=122)) :
                k_de.append(list_keywords[n%b].lower())
                de_list.append(chr(((ord(CP[m])-97)-(ord(k_de[m])-97))%26+97))
                n+=1
                m+=1
            else :
                k_de.append(list_cypher[m])
                de_list.append(list_cypher[m])
                m+=1
            #print k_de
            c-=1

   # print de_list
    de_text="".join(de_list)
    print "The plaintext : ",de_text
    print "Congratulations ! You get it !"
#else :
 #   print "Congratulations ! You get the ciphertext !"


