#include <iostream>
using namespace std;

class node{
    public:
    int lbit;
    int rbit;
    node* l;
    node*r;
    int data;
    node(){
        lbit=1;
        rbit=1;
    }
};
class stack{
    public:
    node* arr[20];
    int top=-1;
    void push(node* a){
        arr[++top]=a;
    }
    node* pop(){
        node* te=arr[top];
        top--;
        return te;
    }
};

class threadedbst{
    public:
    node*head;
    node* root;
    threadedbst(){
        root=NULL;
        head=new node;
        head->l=NULL;
        head->r=NULL;
    }
    void create(node* root1,int d){
        if(root1==NULL){
            root=new node;
            root->l=head;
            root->r=head;
            root->data=d;
            head->l=root;
        }
        else{
        node* temp = new node;
        if(d>root1->data){
            if(root1->rbit==0){
                create(root1->r,d);
            }
            else{
                temp->r=root1->r;
                root1->rbit=0;
                root1->r=temp;
                temp->data=d;
                temp->l=root1;
                if(temp->r==root){
                    temp->r=head;
                }
            }
        }
        else{
            if(root1->lbit==0){
                create(root1->l,d);
            }
            else{
                temp->l=root1->l;
                root1->l=temp;
                root1->lbit=0;
                temp->r=root1;
                temp->data=d;
                if(temp->l==root){
                    temp->l=head;
                }
            }
        }
        }
    }
    node* inordersucc(node* k){
        if(k->rbit==1){
            return k->r;
        }
        k=k->r;
        while(k->lbit!=1){
            k=k->l;
        }
        return k;
    }
    void inordertraversal(){
        if(head->l==NULL){
            cout<<"Empty"<<endl;
            return;
        }
        node*temp=root;
        while(temp->l!=head && temp->lbit==0){
            temp=temp->l;
        }
        while(temp!=head){
            cout<<temp->data<<" ";
            temp=inordersucc(temp);
        }
    }
    void preordertraversal(){
        node* temp=root;
        while(temp!=NULL){
            if(temp->lbit==0){
                temp=temp->l;
            }
            else if(temp->rbit==0){
                temp=temp->r;
            }
            else{
                while(temp!=NULL && temp->rbit==1){
                    temp=temp->r;
                }
                if(temp!=NULL){
                    temp=temp->r;
                }
            }
            
        }
    }
    void deletion(int d){
        int found=0;
        node*temp=root;
        node*parent=NULL;
        while(true){
        if(d>temp->data){
            if(temp->rbit==1){
                break;
            }
            else{
                parent=temp;
                temp=temp->r;
            }
        }
        else if(d<temp->data){
            if(temp->lbit==1){
                break;
            }
            else{
                parent=temp;
                temp=temp->l;
               
            }
        }
        else{
            found=1;
            break;
        }
        }
        if(found==0){
            cout<<"Not found."<<endl;
        }
        else{
            if(temp->lbit==0 && temp->rbit==0){
                caseA(temp,parent);
            }
            else if(temp->rbit==1 && temp->lbit==1){
                caseB(temp,parent);
            }
            else{
                caseC(temp,parent);
            }
        }
    }

    void caseA(node* current,node* parent){
        //Node has left and right child
        node*temp=current;
        temp=temp->r;
        while(temp->lbit!=1){
            parent=temp;
            temp=temp->l;
        }
        current->data=temp->data;
        parent->l=temp->l;
        parent->lbit=1;
        delete temp;
    }
    void caseB(node*current, node*parent){
        //Node has no child
        if(parent==NULL){
            //root has to be deleted.
            head->l=NULL;
            delete root;
            return;
        }
        if(parent->l==current){
            //parent's left child has to deleted
            parent->l=current->l;
            parent->lbit=1;
            delete current;
        }
        else{
            //parent's right child has to be deleted.
            parent->r=current->r;
            parent->rbit=1;
            delete current;
        }
    }
    void caseC(node*current, node*parent){
        //Node has one child
        if(current->lbit==1){
            //Node has a right subtree.
            node*temp=current;
            temp=temp->r;
            while(temp->lbit!=1){
                temp=temp->l;
            }
            if(temp->l!=head){
            temp->l=current->l;
            }
            if(parent->r==current){
                //The node to be deleted lies at the right of parent.
                parent->r=current->r;
            }
            else{
                //The node to be deleted lies to the left of parent.
                parent->l=current->r;
            }
        }
        else{
            //Node has left subtree.
            node*temp=current;
            temp=temp->l;
            //finding inorder predecessor of the node to be deleted.
            while(temp->rbit!=1){
                temp=temp->r;
            }
            if(temp->r!=head){
                temp->r=current->r;
            }
            if(parent->l==current){
                parent->l=current->l;
            }
            else{
                parent->r=current->l;
            }
        }
        delete current;
    }
    void create2(){
        cout<<"Enter number of entries : "<<endl;
        int n;
        cin>>n;
        int d;
        for(int i=0;i<n;i++){
            cin>>d;
            create(root,d);
        }
    }

};
int main()
{
    threadedbst obj;
    obj.create2();
    // cout<<obj.root->data;
    obj.inordertraversal();
    //obj.preordertraversal();
    int d;
    cout<<endl;
    cout<<"Enter node to be deleted : ";
    cin>>d;
    obj.deletion(d);
    cout<<endl;
    obj.inordertraversal();
}