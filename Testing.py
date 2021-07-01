import os
import imageio

path = 'C:/Users/teng448/Desktop/16505/V02/Fe'

folder = os.fsencode(path)

filenames = []

for file in os.listdir(folder):
        filename = os.fsdecode(file)
        if filename.endswith(('.jpg')):
            filenames.append(filename)

filenames.sort()

output = 'test.gif'
frames_path = 'C:/Users/teng448/Desktop/16505/V02/Fe'

with imageio.get_writer(output, mode='I') as writer:
   for filename in frames_path:
        image = imageio.imread(filename)
        writer.append_data(image)
