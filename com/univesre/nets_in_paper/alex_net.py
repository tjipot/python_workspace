"""This is an TensorFLow implementation of AlexNet by Alex Krizhevsky at all.
Paper: (http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf)

Explanation can be found in my blog post:
https://kratzert.github.io/2017/02/24/finetuning-alexnet-with-tensorflow.html

This script enables finetuning AlexNet on any given Dataset with any number of
classes. The structure of this script is strongly inspired by the fast.ai
Deep Learning class by Jeremy Howard and Rachel Thomas, especially their vgg16
finetuning script:
Link: - https://github.com/fastai/courses/blob/master/deeplearning1/nbs/vgg16.py

The pretrained weights can be downloaded here and should be placed in the same
folder as this file: - http://www.cs.toronto.edu/~guerzhoy/tf_alexnet/

@author: Frederik Kratzert (contact: f.kratzert(at)gmail.com)
"""
import tensorflow as tf
import numpy as np


# AlexNet:
# conv1_relu1_norm1 --> pool1 -->
# conv2_relu2_norm2 --> pool2 -->
# conv3_relu3 -->
# conv4_relu4 -->
# conv5_relu5 --> pool5 -->
# fc6_relu6_dropout6 -->
# fc7_relu7_dropout7 -->
# fc8(logits) --> softmax
class AlexNet(object):
	"""Implementation of the AlexNet."""
	
	def __init__(self, x, keep_prob, num_classes, skip_layer, weights_path='DEFAULT'):
		""" Create the graph of the AlexNet model.
		Args:
			x: Placeholder for the input tensor.
			keep_prob:    Dropout probability.
			num_classes:  Number of classes in the dataset.
			skip_layer:   List of names of the layer, that get trained from scratch
			weights_path: Complete path to the pretrained weight file, if it
				isn't in the same folder as this code """
		# Parse input arguments into class variables
		self.X = x
		self.NUM_CLASSES = num_classes
		self.KEEP_PROB = keep_prob
		self.SKIP_LAYER = skip_layer
		
		if weights_path == 'DEFAULT':
			self.WEIGHTS_PATH = 'bvlc_alexnet.npy'
		else:
			self.WEIGHTS_PATH = weights_path
		
		# Call the create function to build the computational graph of AlexNet;
		# 什么鬼概念: 计算图就是依据编译树改来的变量间的依赖: 图有什么好计算的, 还不是要依赖底层概念;
		self.create()
	
	# 关键在create()中定义了一个类属性'self.fc8', 有了它, 就可以寻着依赖计算它了;
	
	# 重要点: 以下网络层的计算调用, 输入的是Tensor, 返回的也是Tensor, 故普通的Python变量(如'pool1')就是一个Tensor类型的变量;
	def create(self):
		"""Create the network graph."""
		# 1st Layer: Conv (w ReLu) -> Lrn -> Pool
		self.conv1 = conv(self.X, 11, 11, 96, 4, 4, padding='VALID', name='conv1')  # Add self.;
		norm1 = lrn(self.conv1, 2, 2e-05, 0.75, name='norm1')  # Add self.;
		pool1 = max_pool(norm1, 3, 3, 2, 2, padding='VALID', name='pool1')
		# 2nd Layer: Conv (w ReLu)  -> Lrn -> Pool with 2 groups
		conv2 = conv(pool1, 5, 5, 256, 1, 1, groups=2, name='conv2')
		norm2 = lrn(conv2, 2, 2e-05, 0.75, name='norm2')
		pool2 = max_pool(norm2, 3, 3, 2, 2, padding='VALID', name='pool2')
		# 3rd Layer: Conv (w ReLu)
		conv3 = conv(pool2, 3, 3, 384, 1, 1, name='conv3')
		# 4th Layer: Conv (w ReLu) splitted into two groups
		conv4 = conv(conv3, 3, 3, 384, 1, 1, groups=2, name='conv4')
		# 5th Layer: Conv (w ReLu) -> Pool splitted into two groups
		conv5 = conv(conv4, 3, 3, 256, 1, 1, groups=2, name='conv5')
		pool5 = max_pool(conv5, 3, 3, 2, 2, padding='VALID', name='pool5')
		
		# 6th Layer: Flatten -> FC (w ReLu) -> Dropout
		flattened = tf.reshape(pool5, [-1, 6 * 6 * 256])
		fc6 = fc(flattened, 6 * 6 * 256, 4096, name='fc6')
		dropout6 = dropout(fc6, self.KEEP_PROB)
		# 7th Layer: FC (w ReLu) -> Dropout
		fc7 = fc(dropout6, 4096, 4096, name='fc7')
		dropout7 = dropout(fc7, self.KEEP_PROB)
		# 8th Layer: FC and return unscaled activations;
		self.fc8 = fc(dropout7, 4096, self.NUM_CLASSES, relu=False, name='fc8')
	
	# 加载权重, 且看它如何加载;
	def load_initial_weights(self, session):
		""" Load weights from file into network.
		As the weights from http://www.cs.toronto.edu/~guerzhoy/tf_alexnet/
		come as a dict of lists (e.g. weights['conv1'] is a list) and not as
		dict of dicts (e.g. weights['conv1'] is a dict with keys 'weights' &
		'biases'), we need a special load function. """
		
		# Load the weights into memory: 'bvlc_alexnet.npy';
		# np.load(): Load arrays or pickled objects from .npy, .npz or pickled files.
		# Returns: result : array, tuple, dict, etc.
		weights_dict = np.load(self.WEIGHTS_PATH, encoding='bytes').item()
		# Loop over all layer names stored in the weights dict:
		# fc6,fc7,fc8,conv3,conv2,conv1,conv5,conv4;
		for op_name in weights_dict:
			# Check if layer should be trained from scratch: do not skip;
			if op_name not in self.SKIP_LAYER:
				with tf.variable_scope(op_name, reuse=True):
					# Assign weights/biases to their corresponding tf variable;
					# 赋值给相应的'tf.Variable';
					# data: 是有关bias或weights的list, np.ndarray, for..in: 逐bias和weights遍历;
					# type(weights_dict['conv1']) ==> <class 'list'>
					for data in weights_dict[op_name]:
						if len(data.shape) == 1:
							var = tf.get_variable('biases', trainable=False)
							session.run(var.assign(data))
						# Biases:  [weights(ndarray),
						#           array([0.10706235, 0.04205888, 0.0946017 , ..., 0.14076257, 0.12524039, 0.18391114], dtype=float32)];
						# Weights: [array([[-0.00433848, -0.00716358, -0.00672231, ..., -0.00185999,-0.00616173, -0.00336802],
						#                  [-0.00273971, -0.0073863 ,  0.01227041, ..., -0.00323482, 0.00020631, -0.00540252],
						#                  [-0.00503064,  0.00243913,  0.00136081, ..., -0.00143727, 0.00729038, -0.00344706],
						#                  ...,
						#                  [-0.00949919, -0.00647061, -0.001888  , ...,  0.0021475 , 0.00136053,  0.0170434 ],
						#                  [ 0.00203296,  0.00029484,  0.00065279, ...,  0.00071566,-0.00333344, -0.00376848],
						#                  [ 0.01293693,  0.0024846 ,  0.00790328, ...,  0.00487464,-0.00440114,  0.00766999]], dtype=float32),
						#           bias(ndarray)]
						else:
							var = tf.get_variable('weights', trainable=False)
							session.run(var.assign(data))


# 自定义的一个卷积函数, 函数内调用tf代码: lambda函数convolve;
# 卷积函数需要的参数: 输入, 滤核尺寸, 滤核个数, 步幅大小, name(如:conv1/norm1/pool1...), 填充模式, groups(?!);
# 卷积函数返回一个输出: 在这里就是relu;
def conv(x, filter_height, filter_width, num_filters, stride_y, stride_x, name, padding='SAME', groups=1):
	""" Create a convolution layer. Adapted from: https://github.com/ethereon/caffe-tensorflow """
	# Get number of input channels: shape的最后一维(-1)是channel数量;
	input_channels = int(x.get_shape()[-1])
	
	# Create lambda function for the convolution, 卷积函数;
	# https://tensorflow.google.cn/api_docs/python/tf/nn/conv2d
	# TF Api: tf.nn.conv2d(input, filter=None, strides=None, padding=None,
	#   use_cudnn_on_gpu=True, data_format='NHWC', dilations=[1,1,1,1], name=None, filters=None)
	# With the default format "NHWC", the data is stored in the order of: [batch, height, width, channels];
	# Returns: A Tensor. Has the same type as input;
	convolve = lambda i, k: tf.nn.conv2d(i, k, strides=[1, stride_y, stride_x, 1], padding=padding)
	
	# 某个scope_name为name的scope, 在此scope中有weights和biases变量, 以下with块中的操作都在此scope_name内进行, 此scope_name范围内没有需要的值, 那就没有了;
	with tf.variable_scope(name) as scope:
		# Create tf variables for the weights and biases of the conv layer;
		# 因为是AlexNet, 所以groups是用来区分shape中input_channels值的?!;
		# input_channels/groups?!
		# https://tensorflow.google.cn/api_docs/python/tf/get_variable
		weights = tf.get_variable('weights', shape=[filter_height, filter_width, input_channels / groups, num_filters])
		biases = tf.get_variable('biases', shape=[num_filters])
		# 分组是什么操作?! 然后还除以input_channels?!
		if groups == 1:
			conv = convolve(x, weights)
		else:  # In the cases of multiple groups, split input and weights and convolve them separately;
			input_groups = tf.split(axis=3, num_or_size_splits=groups,
			                        value=x)  # axis=3(channel维), 此channel维变动, 其它axis(batch/height/width)不能变动, 这样理解?!;
			weight_groups = tf.split(axis=3, num_or_size_splits=groups,
			                         value=weights)  # 故split的意思是: 将总共所有的channels分成groups(=2)个组;
			output_groups = [convolve(i, k) for i, k in
			                 zip(input_groups, weight_groups)]  # 这种用法(list中的函数迭代)真让我无法从Java/C++中适应过来, 要"拥抱世界"..;
			# Concat the convolved output together again: output_groups就是滤核数量?!;
			# 分开conv之后再concat, 有意思伐?!;
			conv = tf.concat(axis=3, values=output_groups)
		# Add biases: bias_add可以Broadcasting的, 每一个feature层加一次bias;
		bias = tf.reshape(tf.nn.bias_add(conv, biases), tf.shape(conv))
		# Apply relu function: 作用于features中的每个值, 从以下tf api中的描述可以看出(features即此处bias参数): (https://tensorflow.google.cn/api_docs/python/tf/nn/relu)
		# features: A Tensor. Must be one of the following types: float32, float64, int32, uint8, int16, int8, int64, bfloat16, uint16, half, uint32, uint64, qint8
		relu = tf.nn.relu(bias, name=scope.name)
		return relu
	# AlexNet中, conv1/2含有relu和norm处理, 而conv3/4/5后只有relu, 故所有conv层可以内含relu计算;


# 自定义全连接操作: 调用tf.xw_plus_b();
# 参数: 输入数据, in的数量, out的数量, 变量scope的name, 是否relu的bool;
# 输出: fc之后的logits;
# 公式: wx+b, 或者relu(wx+b)
def fc(x, num_in, num_out, name, relu=True):
	"""Create a fully connected layer."""
	# 在这里定义一个以name为值的name scope, 假设就在默认图中, 以便和'tf.trainable_variables()'搭配使用(finetune.py中);
	with tf.variable_scope(name) as scope:  # name = conv1, norm1, pool1, fc6, fc7, fc8, etc.;
		# Create tf variables for the weights and biases;
		weights = tf.get_variable('weights', shape=[num_in, num_out], trainable=True)
		biases = tf.get_variable('biases', [num_out], trainable=True)
		# Matrix multiply weights and inputs and add bias;
		act = tf.nn.xw_plus_b(x, weights, biases, name=scope.name)
	if relu:  # Apply ReLu non linearity;
		# relu    = tf.nn.relu(act)
		return tf.nn.relu(act)  # relu
	else:
		return act  # "raw act": logits;


# 自定义最大池化层: 直接调用tf.nn.max_pool();
# 参数: 输入x(4-D Tensor), 滤核高宽, 步长大小, "Optional name for the operation", padding类型;
# 返回: A Tensor of format specified by data_format. The max pooled output tensor;
def max_pool(x, filter_height, filter_width, stride_y, stride_x, name, padding='SAME'):
	"""Create a max pooling layer."""
	# Default format "NHWC": [batch,height,width,channels];
	# 这里的ksize已经做了工程处理: 可以进行批次的操用(batch参数为证), 而数学中的推导只有[高/宽/通道数], 所以不要奇怪;
	return tf.nn.max_pool(x, ksize=[1, filter_height, filter_width, 1], strides=[1, stride_y, stride_x, 1],
	                      padding=padding, name=name)


# 自定义AlexNet中的LRN层;
def lrn(x, radius, alpha, beta, name, bias=1.0):
	"""Create a local response normalization layer."""
	return tf.nn.local_response_normalization(x, depth_radius=radius, alpha=alpha, beta=beta, bias=bias, name=name)


# 自定义的dropout和调用的没什么区别;
# P.s. tf框架会自己寻找依赖, 中间有些输出被dropout掉了, 它要记录控制这些被dropout掉的路径, 前向和反向要统一;
# 输入: x: A floating point tensor.
# 返回: A Tensor of the same shape of x.
def dropout(x, keep_prob):
	"""Create a dropout layer."""
	return tf.nn.dropout(x, keep_prob)

# AlexNet:
# conv1_relu1_norm1 --> pool1 -->
# conv2_relu2_norm2 --> pool2 -->
# conv3_relu3 -->
# conv4_relu4 -->
# conv5_relu5 --> pool5 -->
# fc6_relu6_dropout6 -->
# fc7_relu7_dropout7 -->
# fc8(logits) --> softmax
