import torch
import torchvision
from torchvision.models.video import r3d_18, mc3_18, r2plus1d_18
from torchvision.models.feature_extraction import create_feature_extractor

model1 = r3d_18()
model1.eval()
# PATH1 = 'r3d_18-b3b3357e.pth'
PATH1 = 'network/r3d_18-b3b3357e.pth'

# model2 = mc3_18()
# model2.eval()
# PATH2 = 'mc3_18-a90a0ba3.pth'

# model3 = r2plus1d_18()
# model3.eval()
# PATH3 = 'r2plus1d_18-91a641e6.pth'

device = torch.device('cpu')
model1.load_state_dict(torch.load(PATH1, map_location=device))

return_nodes = {
	'layer1': 'layer1',
	'layer2': 'layer2',
	'layer3': 'layer3',
	'layer4': 'layer4',
	'avgpool': 'avgpool',
}

video = torch.randn(1,3,16,112,112) # Input video with: Batch size, channels, number of frames, height, width
feat_extract = create_feature_extractor(model1, return_nodes=return_nodes)
feature = feat_extract(video)['avgpool'].squeeze(-1).squeeze(-1).squeeze(-1) # Feature obtained after pooling
pred = model1(video).squeeze(0).softmax(0) # Prediction with the original 400 classes (can be viewed as another kind of feature)
# label = pred.argmax().item() # For checking only

# print("Label: {}".format(label))