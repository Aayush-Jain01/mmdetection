# The new config inherits a base config to highlight the necessary modification
_base_ = '/kaggle/working/mmdetection/configs/mask_rcnn/mask_rcnn_x101_64x4d_fpn_mstrain-poly_3x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=3),
        mask_head=dict(num_classes=3)))
        # mask_iou_head=dict(num_classes=3)))
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
load_from = '/kaggle/working/mmdetection/checkpoints/mask_rcnn_x101_64x4d_fpn_mstrain-poly_3x_coco_20210526_120447-c376f129.pth'
