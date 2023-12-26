import random
#Vamos armazenar uma variável para continuar jogando  dados
response="P"
while response=="P":
    N=random.randint(1,6)
    if N==1:
        print("[-----]") 
        print("[     ]")
        print("[  0  ]")
        print("[     ]") 
        print("[-----]")   
    
    if N==2:
        print("[-----]") 
        print("[   0 ]")
        print("[     ]")
        print("[ 0   ]") 
        print("[-----]")  
         
    if N==3: 
        print("[-----]") 
        print("[    0]")
        print("[  0  ]")
        print("[0    ]") 
        print("[-----]")
          
    if N==4:
        print("[-----]") 
        print("[0   0]")
        print("[     ]")
        print("[0   0]") 
        print("[-----]")  
               
    if N==5:
        print("[-----]") 
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]") 
        print("[-----]")  
        
    if N==6:    
        print("[-----]") 
        print("[0   0]")
        print("[0   0]")
        print("[0   0]") 
        print("[-----]")   
        
        
        
        
        
response=input("Pressione P para jogar novamente e n para sair") 
print("\n")            