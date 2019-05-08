import platform
import os

if(platform.system() == 'Linux'):
    addr_train_imgs_COCO = '/mnt/server5_hard1/seungjun/Data_Share/Datas/VQA_COCO/Images/train2014'
    addr_val_imgs_COCO = '/mnt/server5_hard1/seungjun/Data_Share/Datas/VQA_COCO/Images/val2014'

elif (platform.system() == 'Windows'):
    addr_train_imgs_COCO = 'D:\\Data_Share\\Datas\\VQA_COCO\\Images\\train2014'
    addr_val_imgs_COCO = 'D:\\Data_Share\\Datas\\VQA_COCO\\Images\\val2014'