# The new config inherits a base config to highlight the necessary modification
_base_ = '/kaggle/working/mmdetection/configs/ms_rcnn/ms_rcnn_x101_32x4d_fpn_1x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=3),
        mask_head=dict(num_classes=3),
        mask_iou_head=dict(num_classes=3)))
# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ('HTEL', 'Ni-Net', 'Steel')
data = dict(
    train=dict(
        img_prefix='/kaggle/working/mmdetection/RGBDataset/train/',
        classes=classes,
        ann_file='/kaggle/working/mmdetection/RGBDataset/train/_annotations.coco.json'),
    val=dict(
        img_prefix='/kaggle/working/mmdetection/RGBDataset/valid/',
        classes=classes,
        ann_file='/kaggle/working/mmdetection/RGBDataset/valid/_annotations.coco.json'),
    test=dict(
        img_prefix='/kaggle/working/mmdetection/RGBDataset/test/',
        classes=classes,
        ann_file='/kaggle/working/mmdetection/RGBDataset/test/_annotations.coco.json'))

# We can use the pre-trained Mask RCNN model to obtain higher performance
load_from = '/kaggle/working/mmdetection/checkpoints/ms_rcnn_x101_32x4d_fpn_1x_coco_20200206-81fd1740.pth'
