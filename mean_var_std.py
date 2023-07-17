import numpy as np
def calculat(*liste):
    Liste=np.array(liste)
    Array=Liste.reshape(3,3)
    Mean_rows=list(Array.mean(axis=0))
    Mean_columns=list(Array.mean(axis=1))
    Mean=np.mean(Array)
    Variance_rows=list(Array.var(axis=0))
    Variance_columns=list(Array.var(axis=1))
    Variance=np.var(Array)
    Standard_deviation_rows=list(Array.var(axis=0))
    Standard_deviation_columns=list(Array.var(axis=1))
    Standard_deviation=np.std(Array)
    Max_rows=list(Array.max(axis=0))
    Max_columns=list(Array.max(axis=1))
    Max=np.max(Array)
    Min_rows=list(Array.min(axis=0))
    Min_columns=list(Array.min(axis=1))
    Min=np.min(Array)
    Sum_rows=list(Array.sum(axis=0))
    Sum_columns=list(Array.sum(axis=1))
    Sum=np.sum(Array)
    dictionnary={'mean':[Mean_rows,Mean_columns,Mean],'variance':[Variance_rows,Variance_columns,Variance],'standard deviation':[Standard_deviation_rows,Standard_deviation_columns,Standard_deviation],'Max':[Max_rows,Max_columns,Max],'Min':[Min_rows,Min_columns,Min],'Sum':[Sum_rows,Sum_columns,Sum]}
    
    return dictionnary

def calculate(*liste):
    
  Liste=list(liste)
    L=len(Liste)
    try:
        
        print(calculat(*liste))
        
        assert L==9
    except ValueError:
        
        print("List must contain nine numbers.")

calculate(1,2,3,4,5,6,7,8,9)      
