from googletrans import Translator
t = Translator()
a=input("Enter the text to be translated: ")
b=input("Enter the language to which you want to translate: ")
res=t.translate(a,dest=b)
print(res.text,end=" ")