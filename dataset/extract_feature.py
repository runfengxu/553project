from torchvision import models,transforms
import torch
from PIL import Image

alexnet = models.alexnet(pretrained = True)
transform = transforms.Compose([transforms.Resize(256),transforms.CenterCrop(224),
            transforms.ToTensor(),transforms.Normalize(mean = [0.485,0.456,0.406],std = [0.229,0.224,0.225])])
alexnet.eval()
alexnet.classifier = alexnet.classifier[:-1]
def extract(img_path):
    img = Image.open(img_path)
    img_t = transform(img)
    batch_t = torch.unsqueeze(img_t,0)
    out = alexnet(batch_t)
    out.squeeze()
    
