
# By default, no frozen layer for resnet18/34/50, mobilenetv2, seresnext and yolov5, 
# while the first two (backbone.body.conv1., backbone.body.layer1.) layers are frozen 
# in resnet_backbone for fasterrcnn, maskrcnn and retinanet.
supported_model_layer_info = {
    'resnet': [('conv1.', 'bn1.'), 'layer1.', 'layer2.', 'layer3.', 'layer4.'],
    'mobilenetv2': ['features.0.', 'features.1.', 'features.2.', 'features.3.', 'features.4.', 'features.5.',
                    'features.6.', 'features.7.', 'features.8.', 'features.9.', 'features.10.', 'features.11.',
                    'features.12.', 'features.13.', 'features.14.', 'features.15.', 'features.16.', 'features.17.',
                    'features.18.'],
    'seresnext': ['layer0.', 'layer1.', 'layer2.', 'layer3.', 'layer4.'],
    'yolov5_backbone': ['model.0.', 'model.1.', 'model.2.', 'model.3.', 'model.4.',
                        'model.5.', 'model.6.', 'model.7.', 'model.8.', 'model.9.'],
    'resnet_backbone': ['backbone.body.conv1.', 'backbone.body.layer1.', 'backbone.body.layer2.',
                        'backbone.body.layer3.', 'backbone.body.layer4.']
}
