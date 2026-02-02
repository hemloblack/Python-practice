import random
import pickle
data=[]
for i in range(100):
    this_one=(random.randint(1,6),random.randint(1,6))
    data.append(this_one)
    
taas_out=open("mosabeghe.tass","wb")
pickle.dump(data,taas_out)
taas_out.close()
