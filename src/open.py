import pickle 
import sklearn

file= open('check.pkl','rb')
image=pickle.load(file)
print image 

