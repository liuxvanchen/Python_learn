from sklearn import datasets
import matplotlib.pyplot as plt

# 加载 digits 数据集
digits = datasets.load_digits()

# 打印数据集的一些基本信息
print("Images shape:", digits.images.shape)
print("Data shape:", digits.data.shape)
print("Target shape:", digits.target.shape)
print("Number of classes:", len(digits.target_names))

# 选择几张图片进行显示
n_images = 5
images_and_labels = list(zip(digits.images, digits.target))
for index, (image, label) in enumerate(images_and_labels[:n_images]):
    plt.subplot(1, n_images, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Training: %i' % label)

# 显示图片
plt.show()
