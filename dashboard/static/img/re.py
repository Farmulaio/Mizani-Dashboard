# importing os module 
import os 
  
pat = os.getcwd()
# Function to rename multiple files 
def main(): 
  
    for count, filename in enumerate(os.listdir(pat)): 
        print(filename)
        src = filename.replace(" ", "") 
        print(src)
          
        # rename() function will 
        # rename all the files 
        os.rename(src, src) 
  
# # Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 
