#this file is a shell scrift used for automating task .
#it can be run using bash filename.sh or making it executable using chmod +x filename.sh
#this is to facilitate hot reload when we change files , it should be modified for production remove the debug mode

#to run just type ./boostrap.sh
#use pipenv to install packages
export FLASK_APP=./track-id-api/index.py
pipenv run flask --debug run -h 0.0.0.0