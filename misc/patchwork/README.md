# Patchwork

## Description

One of the new cabin boys has turned all of our important details into a new patchwork sail. Can you save our secret key?

**Category:** misc

**Difficulty:** Easy

**Author:** Darkflame72

**Flag:** AHOY{QR_1s_v3ry_fun}

## Exploit
You are provided with an mp4 file which appears to be parts of a qr code on each frame. You can use `ffmpeg` to extract all the frames where you can work out that there is 8 qr codes. The parts can be manually stiched together or done automatically with a script using a tool such as `ImageMagick's convert`.

The 8 qr codes are:

1. https://en.wikipedia.org/wiki/Blackbeard
2.  djNyeV9mdW59
3. https://www.youtube.com/watch?v=qP-7GNoDJ5c
4.  https://www.legislation.govt.nz/act/public/1961/0043/latest/DLM328572.html
5. https://en.nospoiler.it/posts/pirates-of-the-caribbean-film-historical-inaccuracies-errors
6. https://www.youtube.com/watch?v=p7YXXieghto
7. QUhPWXtRUl8xc18=
8. https://www.piratesahoy.net