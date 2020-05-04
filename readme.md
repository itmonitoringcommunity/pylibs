## pysched

This application provides automatic sending processes via bulletin-api. It is possible to use many python libraries.

## FIRST

* Configure system environment on Windows OS
* Download Pyhton from visualstudio code extensions

## SECOND

```
-- pysched folder right click open in terminal

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

python -m venv env
. env/Scripts/activate.bat

python app.py

```

## THIRD

Enable gmail smtp settings

https://mail.google.com/mail/u/0/#settings/fwdandpop

https://myaccount.google.com/lesssecureapps

https://accounts.google.com/DisplayUnlockCaptcha


## FORTH

```
docker build -t pysched .
docker run -it pysched
docker rmi pysched .

```