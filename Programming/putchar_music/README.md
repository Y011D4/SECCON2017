# putchar music
__Genre__: Programming
__Point__: 100pts

> putchar music  
> This one line of C program works on Linux Desktop. What is this movie's title?   
> Please answer the flag as SECCON{MOVIES_TITLE}, replace all alphabets with capital letters, and spaces with underscores.
> 
> ```c
> main(t,i,j){unsigned char p[]="###<f_YM\204g_YM\204g_Y_H #<f_YM\204g_YM\204g_Y_H #+-?[WKAMYJ/7 #+-?[WKgH #+-?[WKAMYJ/7hk\206\203tk\\YJAfkkk";for(i=0;t=1;i=(i+1)%(sizeof(p)-1)){double x=pow(1.05946309435931,p[i]/6+13);for(j=1+p[i]%6;t++%(8192/j);)putchar(t>>5|(int)(t*x));}}
> ```

## Writeup
First, I compiled the one-line program.
(It is needed to modify the code to include some libraries like math.h)
```bash
$ gcc putchar_music.c -o putchar_music -lm
```
Google says that SoX ([here](http://royal-paw.com/2012/01/bytebeats-in-c-and-python-generative-symphonies-from-extremely-small-programs/)) can work for this problem.

```bash
$ ./putchar_music | sox -r 8000 -b 8 -c 1 -t raw -s - -d
```

The music is well known!

```
SECCON{STAR_WARS}
```
