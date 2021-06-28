# Genshin-Auto-Daily-Check-In


### What the hell is this?
One question, do you always forget to do daily check-in at Hoyolab to claim rewards? <br>
Well, if it's true, we are both f*cked up .-. <br>
But don't worry, this code might be the solution :)


### What this code does:
This code will automate to do daily check-in in Hoyolab to claim rewards using **cron** and **selenium**


## Install
Requires [Docker](https://www.docker.com/) and docker-compose

Install docker-compose (ubuntu):

```
sudo apt install docker-compose
```


## Usage
- Clone this repository:
```
git clone https://github.com/cacadosman/Genshin-Auto-Daily-Check-In
cd Genshin-Auto-Daily-Check-In
```
- Open genshin daily check in website
- If you are using chrome/firefox, just press f12 and go to console
- Type `document.cookie` on console, press enter and copy all its content
- Paste the cookie that have been copied in **cookie.txt**:
```
echo "paste_the_cookie_here" > cookie.txt
```
- Run
```
docker-compose up -d
```
Done


## Contact
Nope.
