name = 'Clasificador2'
path = '/content/drive/MyDrive/Proyecto5to/IA/'
print('Ejecutando IA ...')
from google.colab import drive
drive.mount('/content/drive')

import json
from keras.models import Sequential
from keras.saving import load_model

model_type = Sequential()
model_type = load_model(path + name + '.h5')

image_desired_size = None
types = None
with open(path + name + '.json') as f:
    d = json.load(f)
    print(d)
    image_desired_size = d['image_desired_size']
    types = d['image_types']

from PIL import Image
from keras import utils
#from tensorflow.image import resize

def Padding(i):
  padding = (0, image_desired_size[0] - np.shape(i)[0]), (0, image_desired_size[1] - np.shape(i)[1]), (0, 0)
  return np.pad(i, padding, 'constant', constant_values = ((0, 0), (0, 0), (0, 0)))
  #return np.pad(i, padding, 'median')

def GetFileList(dir = path):
    return os.listdir(dir)

def resize_image_with_aspect_ratio(img, base_width=None, base_height=None):
  if base_width > base_height:
    base_height = None
  else:
    base_width = None
  # Get original dimensions
  original_width, original_height = img.size[0], img.size[0]
  
  if base_width and not base_height:
      # Calculate height to maintain aspect ratio
      w_percent = base_width / float(original_width)
      new_height = int((float(original_height) * float(w_percent)))
      new_size = (base_width, new_height)
  elif base_height and not base_width:
      # Calculate width to maintain aspect ratio
      h_percent = base_height / float(original_height)
      new_width = int((float(original_width) * float(h_percent)))
      new_size = (new_width, base_height)
  else:
      raise ValueError("Specify either base_width or base_height")

  return img.resize(new_size, Image.ANTIALIAS)

def ReadImage(path):
  #img = load_img(path)
  img = Image.open(path)
  img = resize_image_with_aspect_ratio(img, image_desired_size[0], image_desired_size[1])
  img = utils.img_to_array(img)
  #img = resize(img, image_desired_size, preserve_aspect_ratio=True)
  img = img * 1/255 # Dividimos el valor de los pixeles por 255 para que el valor permanesca entre 1 y 0
  return img

def GetPred(array):
  max = 0
  for i in range(len(array)):
    if(array[i] > array[max]):
      max = i
  return types[max]

def PassImage(path):
    a = model_type.predict(ReadImage(path))
    return GetPred(a)