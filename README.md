# pokeGAN

## Overview
This is the code for [this](https://youtu.be/yz6dNf7X7SA) video on Youtube by Siraj Raval. We'll use a WGAN to create new kinds of Pokemon.

## Dependencies (pip install)
```
cv2
tensorflow( >=1.0)
scipy
numpy
```
## Usage
```
cd pokeGAN
python resize.py
python RGBA2RGB.py
python pokeGAN.py
```

And open the notebook by typing in `jupyter notebook` in the root directory. Install it [here](http://jupyter.readthedocs.io/en/latest/install.html) if you haven't  

## example pokemon
![image1](https://github.com/moxiegushi/pokeGAN/raw/master/images/Notes_1500532347861.jpeg)

![image2](https://github.com/moxiegushi/pokeGAN/raw/master/images/Notes_1500532371830.jpeg)

## Credits

The credits for this code go to [moxiegushi](https://github.com/moxiegushi/pokeGAN). I've merely created a wrapper to get people started.

# Martin's notes:
To set up the files, you need to first coppy in your pokemon into the data folder.
Then run the RGBA2RGB.py file. Then open the resize file and you will need to run that to resize everything.
Lastly you will be able to run the GAN. 
