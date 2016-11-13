~/.virtualenvs/cv/bin/python main.py
opencv_createsamples -info car_pos.info -num 550 -w 100 -h 40 -vec cars_pos.vec
opencv_traincascade -data data -vec cars_pos.vec -bg car_neg.info -numPos 240 -numNeg 290 -numStages 5 -w 100 -h 40 -featureType HAAR 
