import imageio
import os

dir = 'C:/Users/teng448/Desktop/16505/V02/Fe'
images = []
for file_name in sorted(os.listdir(dir)):
    if file_name.endswith('*.jpg'):
        file_path = os.path.join(dir, file_name)
        images.append(imageio.imread(file_path))
imageio.mimsave('PLEAASEWORKK.gif', images)