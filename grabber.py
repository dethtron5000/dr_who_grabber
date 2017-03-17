from bs4 import BeautifulSoup

f = open("unearthly_child.html")
z = f.read()

s = BeautifulSoup(z)

tags = s.find("a", text="Companions").find_parent().find_parent().find(
    "ul").find_all("a")

print tags

for tag in tags:
    print tag.get_text()
