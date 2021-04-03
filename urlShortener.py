import pyshorteners

link = input("Input the link : ")

shortener = pyshorteners.Shortener()
x = shortener.tinyurl.short(link)

print("Shortened link is :")
print(x)