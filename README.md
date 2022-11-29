# CutAi

 CutAi is our web application project that helps you get highlights from your videos by pulling out the best clips from your video.

## Dependencies

You can install the required dependencies by running the following command:

pip install -r requirements.txt

## About The Project

This project was developed with the following frameworks:
    Flask
  / PyTube
  / Webflow
  
## Installation
  1. Clone the repo:
```
  https://github.com/khalil-asli/proj_cutIA.git 
```
  
  2. Create a virtual enviroment:
```
  python3 -m venv env
```

 3. Activate the virtual enviroment:
 If operating on Windows:
 ```
  .venv\scripts\activate  
```

4. Install all required dependicies:
 ```
  pip install -r requirements.txt  
```

5. Run the app:
 ```
  flask run  
```

## In case :
ImageMagick is not strictly required, but needed if you want to incorporate texts. It can also be used as a backend for GIFs, though you can also create GIFs with MoviePy without ImageMagick.

Once you have installed ImageMagick, it will be automatically detected by MoviePy, except on Windows! Windows users, before installing MoviePy by hand, need to edit moviepy/config_defaults.py to provide the path to the ImageMagick binary, which is called convert. It should look like this:
 ```
  IMAGEMAGICK_BINARY = "C:\\Program Files\\ImageMagick_VERSION\\convert.exe"
```
You can also set the IMAGEMAGICK_BINARY environment variable See moviepy/config_defaults.py for details.

If you are using an older version of ImageMagick, keep in mind the name of the executable is not magick.exe but convert.exe. In that case, the IMAGEMAGICK_BINARY property should be ``` C:\\Program Files\\ImageMagick_VERSION\\convert.exe```

## Contact:
Equipe 10 : Célia GUYOBON ● Morgane LAUTONE ● Thanina KALI ● Ronad MABIKANA ● 
Mohamed Khalil ASLI ● Riswane MARICAR ● Sandro DA SILVA ● Louis MARTIN DU NORD
