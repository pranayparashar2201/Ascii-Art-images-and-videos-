# Asciify-videos-and-images
ASCII(American Standard Code for Information Interchange) is a common encoding format used for representing strings and text data in computers.
Images can also be shown by setting different characters and their colour based on the input image and hence representing an image using a matrix of characters.

### Description
This project aims to convert images(jpg) and videos(mp4) into ASCII strings that will have the close resemblance to the input file we provided.
### Dependencies
This projects mainly required the following:

.openCV

.os

.shutil

.numpy

.PIL


### How to use
.clone the repository on your system

.save the file (mp4/jpg) you want to convert in the data directory

.open the terminal to the directory where you have stored this project

.run the file by using 'python ascii.py'

.enter the name of the file you want to convert along with the file type name(.mp4/.jpg)

.if you used an image as an input, the resultant ascii image will be available in the data directory named as 'output.jpg'

. if the input is a video then, the resultant ascii video will be stored in the 'outputvideo' directory

Video demo to run this file is [here](https://drive.google.com/file/d/11OvGPgJIfenFAkjijBvrtA1MyJRZI57R/view?usp=sharing).

### Internaal working
The working can be explained in two parts:

1. Image to ASCII

 Using openCV we can represent an image in a 2/3 dimensional matrix depending on it being grayscale or color. Our main motive will be to find the Characters sutiable to represent each pixel, depending on the intensity we will creat a Character string with characters which will be used for varying intensities depending on the area they occupy in a block.
 
    a. character string
    
![tutu](https://user-images.githubusercontent.com/76247052/174784738-1d5507f6-2b96-43d0-b49a-78221bd464f2.png)

    b. We can choose a suitable font for this, i have used DejaVuSansMono. 

![Screenshot (249)1](https://user-images.githubusercontent.com/76247052/174785012-f0136421-c91b-4560-92ed-2bfaa2f731b7.png)

The background color can be changed depending on the type of output ascii image required, we can set the value of variabe bg to 'black' and 'white'  

![Screenshot (251)](https://user-images.githubusercontent.com/76247052/174785227-c661ca4c-2858-43aa-8c22-7ff09a9d866b.png)

The number of columns of the output image can be set by ourselves depending on the quality of the image we want and the time we have to process it. 

![Screenshot (253)](https://user-images.githubusercontent.com/76247052/174785890-2cfefdf6-be5a-4557-94a8-3dbbb03220e1.png)


    c. We will input an image which we would have saved in our data directory, this function will be performed using openCV. Based on number of columns, input image height and width, we could use the scale to form the output dimension of our image.

![Screenshot (252)](https://user-images.githubusercontent.com/76247052/174786004-394fc50e-952a-415f-ac45-46ab07b2a9f9.png)

    d. Then we can use ImageDraw from PIL and fill it with characters and color based on the input image pixels we need to replace. We will have to calculate the the average color, character and intensity to represent the output pixel as the input - output images are having different pixels in an image. So to represent the input to the closest in terms of these characterstics, we will have to average all the input pixels forming 1 output pixel.
    
![avgchar](https://user-images.githubusercontent.com/76247052/174789068-82532d06-c21c-4314-8020-7147fc812b8a.png)

    e. Now we will invert the image and get rid of excess borders.
    
![invert](https://user-images.githubusercontent.com/76247052/174789106-99a3a44b-b142-43b5-ad37-8a528b7829b4.png)

    f. We will then save this image in the data directory itself as the name outputimage.
    
![saving](https://user-images.githubusercontent.com/76247052/174789133-38df5de9-09dc-444a-b83a-b7e7311928b2.png)
Demo:
input:![image](https://user-images.githubusercontent.com/76247052/174790184-58986e4c-4582-4ec8-a627-0281bbe5ce4b.jpg)
output:![outputimage](https://user-images.githubusercontent.com/76247052/174825773-eb11ba23-aa81-459b-96e3-53b5905dc62a.jpg)



  2. Videos to ASCII videos
  A genral idea to do this will be dividing the input video into frames, then converting each and every frames using the funstion mentioned in part1 and then merging all these frames back into a video form. Using openCV we will convert videos to frames and then sequentially convert them to ASCII, then we will save these frames in a new output mp4 file.
  
    a. input video to fame conversion
    
![Screenshot (255)](https://user-images.githubusercontent.com/76247052/174791637-b1caf6f3-3953-4671-a64a-6c4563a5bdee.png)
    
    b. image frame to ascii frame using the same procedure in part 'a'.
    
    
    c. merging ascii frames to form an output video. Saving this video and then deleting the the intermediate directory created to store the ascii frames.
    
![Screenshot (257)](https://user-images.githubusercontent.com/76247052/174791663-17c0748a-1e2c-4795-a80a-17ce8b923808.png)
![Screenshot (258)](https://user-images.githubusercontent.com/76247052/174791678-77568167-04a5-45e0-ae30-64876339858b.png)
    
    d. The final video will be stored in 'outputvideo' directory.
![Screenshot (256)](https://user-images.githubusercontent.com/76247052/174791404-93920b30-dbe3-4c24-bd2e-073021df651a.png)

#### Sample: 
##### input: [input video](https://drive.google.com/file/d/1lg759RnXnciHxEFKiFcrPltEPVxqjVwW/view?usp=sharing)
##### output : [output ascii video](https://drive.google.com/file/d/1u96CKEESFsvmiC4zaTRiQ0dnEf-E-JG0/view?usp=sharing)
  
### Resources and references
1. [medium](https://medium.com/analytics-vidhya/the-ultimate-handbook-for-opencv-pillow-72b7eff77cd7)
2. [hackmd](https://hackmd.io/@xenorivai/H12U8cwv5)
3. [docs.opencv](https://docs.opencv.org/4.x/d7/dbd/group__imgproc.html)
4. [wikipedia](https://en.wikipedia.org/wiki/ASCII_art#Types_and_styles)
5. [analytics](https://www.analyticsvidhya.com/blog/2021/03/grayscale-and-rgb-format-for-storing-images/)
6. [alekya3.med](https://alekya3.medium.com/how-images-are-stored-in-a-computer-f364d11b4e93)
  
