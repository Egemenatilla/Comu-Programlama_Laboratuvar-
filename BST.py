class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
        
def insert(root,node):
    if root is None: #Agac bos ise deger kok olur
        root=node
    else:
        if root.val < node.val:        #Kok degeri eklencek degerden kucuk ise saga eklenme yapilir.
            if root.right is None:     #Sagda deger yoksa ilk deger sagın koku olur.
                root.right = node
            else:               
                insert(root.right,node)#Deger varsa recursive olarak islem gerçeklestirilir.
        else:                          #Eklenme sola yapilir. 
            if root.left is None:
                root.left = node
                
            else:
                insert(root.left,node)
                

def minValueNode(node):
    current = node
    while(current.left is None):
        current=current.left
    return current

def deleteNode(root,key):
    if root is None:
        return root
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None  
            return temp
         
        temp = minValueNode(root.right)
        root.key = temp.val
        root.right = deleteNode(root.right, temp.val)    
    return root
            
def search(root,key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right,key)
    return search(root.left,key)
                
                
def inorder(root):         #inorder siralama sol kok sag
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def preorder(root):        #preorder siralama kok sol sag
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)
        
def postorder(root):       # postorder sol sag kok
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)                    


        
        
        
r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80)) 





print(inorder(r))
#print(preorder(r))
#print(postorder(r))

root = deleteNode(r, 20) 
print("Inorder traversal of the modified tree")
inorder(r) 

root = deleteNode(r, 80) 
print("Inorder traversal of the modified tree")
inorder(r) 

root = deleteNode(r, 70) 
print("Inorder traversal of the modified tree")
inorder(r) 
