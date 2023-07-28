from numpy import dtype, gradient
import torch
x_train=torch.tensor([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],dtype=torch.float32)
w=torch.tensor(0.0,dtype=torch.float64,requires_grad=True)
y_train=torch.tensor([1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400],dtype=torch.float32)

def model(x_train,y_train,n_iters,lr,w):
    for epoch in range(n_iters):
        ypred=w*x_train
        loss=((ypred-y_train)**2).mean()
        loss.backward()
        # dw=2*(x_train*(ypred-y_train)).mean()
        with torch.no_grad():
            w-=lr*w.grad
        w.grad.zero_()
        print(f'epoch {epoch+1:.3f},loss {loss:.8f} w {w}')
    return w
w=model(x_train,y_train,10000,0.0001,w)
x_test=torch.tensor([100,20,30,34],dtype=torch.float32)

print(f'prediction after training {w*x_test}')