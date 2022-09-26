espeak -ven+f2 -k5 -s150 --stdout  "Can you please input your phone number, zipcode, number of pets you have, and how old you are?" | aplay
arecord -D hw:3,0 -f cd -c1 -r 16000 -d 5 -t wav recorded_mono.wav
python3 test_words.py recorded_mono.wav