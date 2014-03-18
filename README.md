<h2>Python Music Note Recognition</h3>
<p>Run standardize.py when images are added or changed in the newimages directory. This method resizes all images to the same size, converts them to black and white, and updates the noteArEx.txt file. Scale method originally from this <a href="https://gist.github.com/enagorny/2966369">gist</a></p>
<p>
noterec.py returns a list of the notes a given image most closely matches. The most likely note has the highest number of matched pixels. Notes that do not match 3/4 or more of the total number of pixels should be rejected.
</p>
