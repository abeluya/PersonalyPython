from tkinter import Tk


class Acronym:
    url = ""
    synonims = []


    def set_url(self, url):
        self.url = url

    def set_synonim(self, synonim):
        self.synonims.append(synonim)

    def set_synonims(self, synonims):
        self.synonims = synonims

    def get_url(self):
        return self.url

    def get_synonims(self):
        return self.synonims

    def get_synonim(self, index):
        return self.synonims[index]


acronym_list = [Acronym()]
urlList = Tk().clipboard_get().split('\n')  # Get the URLs from the clipboard
print(len(urlList))
print(urlList)
for url in urlList:
    if len(url) >= 1:
        acronym = Acronym()
        print(len(url))
        test = url.split('\t')
        print(len(test))
        acronym.set_url(test[0])
        acronym.set_synonims(test[1].split(','))
        print(acronym.get_url())
        print(acronym.get_synonims())
        acronym_list.append(acronym)

print(acronym_list)
for x in acronym_list:
    print(x.get_url())
    print(x.get_synonims())
