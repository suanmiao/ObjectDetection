~/.virtualenvs/cv/bin/python main.py
opencv_createsamples -info aed_pos.info -num 32 -w 50 -h 50 -vec aed_pos.vec
opencv_traincascade -data data -vec aed_pos.vec -bg aed_neg.info -numPos 31 -numNeg 20 -numStages 5 -w 50 -h 50 -featureType  HAAR 
