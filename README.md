# Script for controlling Tapo's smart Wi-Fi Light Bulbs
__I have used [This Repo](https://github.com/fishbigger/TapoP100) inorder to write this script.__

__Lightbulb used:__

<img src="https://m.media-amazon.com/images/I/41leEy+MFDL._AC_SY1000_.jpg" width="300">




__What you need for this project__
- One or more Tapo Smrt Wi-Fi Light Bulbs
- Access to your router inorder to get the ip of the bulb
- A code editor
- Download the app and create an account.

Please note that the code is not optimal in any way however it works for me. If you want to try this out, make sure to install the pip package for this bulb:
```py
pip install PyP100
```
Also you have to make two JSON files, one containing the ip of the device running the script, the other containing the IP, email and password of the lamp.

__PLEASE NOTE THAT YOU MUST CREATE A FOLDER NAMED TEMPLATES AND PUT ALL HTML FILES IN THERE INORDER FOR FLASK RUN FIND IT__

If you want further information about what you can do with the bulb, please visit the authors github repo.
