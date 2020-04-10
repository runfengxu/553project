from torchvision import models,transforms
import torch
from PIL import Image
import os
import numpy as np
def extract(img_path,j):
    img = Image.open(img_path)
    img_t = transform(img)
    batch_t = torch.unsqueeze(img_t,0)
    out = alexnet(batch_t)
    out.squeeze()
    out = out.tolist()
    k={img_path.split('.')[0]:out}
    with open('feature.json','a') as f:
        f.write(str(k)+'\n')



if __name__ == '__main__':
    alexnet = models.alexnet(pretrained = True)

    transform = transforms.Compose([transforms.Resize(256),transforms.CenterCrop(224),
            transforms.ToTensor(),transforms.Normalize(mean = [0.485,0.456,0.406],std = [0.229,0.224,0.225])])
    alexnet.eval()
    alexnet.classifier = alexnet.classifier[:-1]

    img_paths  = os.listdir('img')
    j=0
    for img_path in img_paths:
        extract(img_path,j)
        j+=1
        if j%1000==0:
            print(j)