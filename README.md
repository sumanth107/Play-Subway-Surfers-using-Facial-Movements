# Play-Subway-Surfers-using-Facial-Movements  
This is a pretty exciting project where you get to play Subway Surfers using face movements!! 
  
  
![final.gif](final.gif)   
  
  
I felt it was really fun playing this way, perhaps because you feel more involved like this!!  
In this project first I used opencv for face detection. [haarcascade_frontalface_default.xml](haarcascade_frontalface_default.xml) is an already trained ML model to recognise faces available on the official opencv repo. I've created a small region on the screen as reference. The position of the face relative to this region is translated into keyboard function (up, down, left and right for this game). This translation is achieved using pynput module.  
P.S : You can can also play Temple Run or any other similar game using this program
