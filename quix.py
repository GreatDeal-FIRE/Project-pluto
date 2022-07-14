from sklearn.metrics import confusion_matrix

y_true =[1,1,0,1,0,0,1,0,0,0,1,0,1]
y_pred =  [0,1,1,1,0,0,1,0,1,0,1,0,1]
       

tn, fp, fn, tp = confusion_matrix(y_true, y_pred, labels=[0, 1]).ravel()
print(tn, fp, fn, tp)  # 1 1 1 1