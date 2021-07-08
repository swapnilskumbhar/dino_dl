from fastai.vision.all import *
import torch

# class custom_model(nn.Module):
#     def __init__(self):
#         super(custom_model, self).__init__()
#         self.conv_layers = nn.Sequential(
#         nn.Conv2d(3, 8, 7),
#         nn.ReLU(),
#         nn.BatchNorm2d(8),
#         nn.Conv2d(8, 16, 7, stride=2),
#         nn.ReLU(),
#         nn.BatchNorm2d(16),
#         nn.Conv2d(16, 32, 7, stride=2),
#         nn.ReLU(),
#         nn.BatchNorm2d(32),
#         nn.Conv2d(32, 16, 7, stride=2),
#         nn.ReLU(),
#         nn.BatchNorm2d(16),
#         nn.Conv2d(16, 8, 7, stride=2),
#         nn.ReLU()
#         )
#         self.linear = nn.Linear(512,3,bias=True)
        
#     def forward(self, x):
#         x = self.conv_layers(x)
#         x = x.view(x.shape[0],-1)
#         x = self.linear(x)
#         return x


class custom_model(nn.Module):
    def __init__(self):
        super(custom_model, self).__init__()
        self.conv_layers = nn.Sequential(
        nn.Conv2d(3, 8, 7),
        nn.ReLU(),
        nn.BatchNorm2d(8),
        nn.Conv2d(8, 16, 7, stride=2),
        nn.ReLU(),
        nn.BatchNorm2d(16),
        nn.Conv2d(16, 32, 7, stride=2),
        nn.ReLU(),
        nn.BatchNorm2d(32),
        nn.Conv2d(32, 16, 7, stride=2),
        nn.ReLU(),
        nn.BatchNorm2d(16),
        nn.Conv2d(16, 8, 7, stride=2),
        nn.ReLU(),
        nn.Conv2d(8, 4, 7, stride=2),
        nn.ReLU()
        )
        self.linear = nn.Linear(24,3,bias=True)
        
    def forward(self, x):
        x = self.conv_layers(x)
        x = x.view(x.shape[0],-1)
        x = self.linear(x)
        return x
















def get_model(path_img = './imgs',model_train_dir = 'model_best_10'):
    dls = ImageDataLoaders.from_folder(Path(path_img),valid=None,bs=64,conver_mode='L',item_tfms=Resize((216,384),'squish'))
    learn = Learner(dls, custom_model(), metrics=error_rate, loss_func=torch.nn.CrossEntropyLoss())
    learn.load(model_train_dir)
    return learn.model