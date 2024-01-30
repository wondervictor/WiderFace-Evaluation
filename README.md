# WiderFace-Evaluation
Python Evaluation Code for [Wider Face Dataset](http://mmlab.ie.cuhk.edu.hk/projects/WIDERFace/)


## Usage


##### before evaluating ....

installation from github

````
git clone <URLL>
cd WiderFace-Evaluation
pip install .
````

##### evaluating

**GroungTruth:** `wider_face_val.mat`, `wider_easy_val.mat`, `wider_medium_val.mat`,`wider_hard_val.mat`

````
python3 evaluation.py -p <your prediction dir> -g <groud truth dir>
````

## Bugs & Problems
please issue

## Acknowledgements

some code borrowed from Sergey Karayev
