from IPython.display import clear_output
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
def covariance():
    print('Covariance calculator.')
    print('Note: Only csv or excel files are allowed.')
    
    #Chosing a method of entry.
    Start = True
    while Start:
        method = input('Manual entry or File entry?')
    
    
        if method[0].lower() =='m':
            clear_output()
            xvalues = (input('Enter values of X seperated by comma:'))
            clear_output()
            yvalues = (input('Enter values of Y seperated by comma:'))
        
            #Converting input string into integer 
            xvaluelist = []
            yvaluelist = []
            for x in xvalues.split(','):
                xvaluelist.append(int(x))
            for y in yvalues.split(','):
                yvaluelist.append(int(y))
        
            avgx = sum(xvaluelist)/len(xvaluelist)
            avgy = sum(yvaluelist)/len(yvaluelist)
        
            difx = []
            dify = []
            for x in xvaluelist:
                difx.append(x - avgx)
            
            for y in yvaluelist:
                dify.append(y-avgy)
        
            mylistxy = []   
            for i in range(0,len(difx)):
                mylistxy.append(difx[i]*dify[i])
            Sum = sum(mylistxy)
            Covariance = Sum/len(difx)
            print(f"The Covariance is {round(Covariance)}")
            Start = False
            
        elif method[0].lower() == 'f':    
            x = input("Please enter the location of your file.")
            choice = True
            #Checking for correct file type.
            while choice == True:
                y = input("Please chose your file type (csv or excel)")
                #input('Please state the type of your file.')
                if y.lower() in ['csv','excel']:
                    choice = False
                else:
                    clear_output()
                    print('I can only read excel or csv formats.')
                    print('Please enter a correct file type.')
                    choice = True 
    
        #Checking for correct file location.
            
            import pandas as pd
            df = pd.DataFrame()
            if y.lower() in ['csv','excel']:
                try:
                    df = pd.read_csv(x)
                    
                except:
                    df = pd.read_excel(x)
                else:
                    fchoice = True
                    while fchoice == True:
                        clear_output()
                        print('You had entered an incorrect file location.')
                        x = input('Please enter a correct file location.')
                        if x.lower().split('.')[-1] in ['csv','xlsx']:
                            fchoice = False
                finally:
                    print('File path accepted')
    
    
            mylistx = []
            mylisty = []
            for x in df[df.columns[0]]:
                mylistx.append(x - df[df.columns[0]].mean())

            for y in df[df.columns[1]]:
                mylisty.append(y - df[df.columns[1]].mean())
            mylistxy = []   
            for i in range(0,len(mylistx)):
                mylistxy.append(mylistx[i]*mylisty[i])
            Sum = sum(mylistxy)
            Covariance = Sum/len(mylistx)
            print(f"The Covariance is {round(Covariance)}")
            Start = False
        
        else:
            clear_output()
            print("Wrong method. Please reply with Manual or File Entry")
            Start = False