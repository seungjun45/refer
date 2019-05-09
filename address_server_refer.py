import platform
import os

if(platform.system() == 'Linux'):
    addr_train_imgs_COCO = '/mnt/server5_hard1/seungjun/Data_Share/Datas/VQA_COCO/Images/train2014'
    addr_val_imgs_COCO = '/mnt/server5_hard1/seungjun/Data_Share/Datas/VQA_COCO/Images/val2014'
    addr_imgs_refclef = '/mnt/server5_hard1/seungjun/Data_Share/Datas/RefClef/saiapr_tc-12'

elif (platform.system() == 'Windows'):
    addr_train_imgs_COCO = 'D:\\Data_Share\\Datas\\VQA_COCO\\Images\\train2014' # coco image location
    addr_val_imgs_COCO = 'D:\\Data_Share\\Datas\\VQA_COCO\\Images\\val2014'
    addr_imgs_refclef = 'D:\\Data_Share\\Datas\\RefClef\\saiapr_tc-12' # "saiapr_tc-12" location