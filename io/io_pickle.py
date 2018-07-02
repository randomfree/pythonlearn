import pickle

shoplistfile = 'showlist.data'

showlist=['apple','mango','carrot']

f = open(shoplistfile,'wb')

pickle.dump(showlist,f)
f.close()

del showlist

f = open(shoplistfile,'rb')

storedlist = pickle.load(f)

print(storedlist)

f.close()
