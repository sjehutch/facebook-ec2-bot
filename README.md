# faceboot-ec2-bot

### What it does 
This facebook bot allows you to create an ec2 instance by texting the word ec2 to the bot 

### What you need 
1 Python3 
1 BOTO3 - (AWS)
1 ngrok (Unless you have a https server handy)

### In action 

![Image of AWS Console](https://dl.dropboxusercontent.com/u/32232546/Screenshot%202017-04-28%2020.33.52.png)

![Image of Facebook Bot](https://dl.dropboxusercontent.com/u/32232546/Screenshot%202017-04-28%2020.33.24.png)

### How to get it all set up (Document this later cause i am about to watch a movie)

1  Create a facebook app
2  Select messaging for the facebook app type 
3  Get your access token and associate it to a facebook page (you can create one on the app screen)
4  Get the access token 
5  run a curl request with the access token
```
curl -X POST "https://graph.facebook.com/v2.6/me/subscribed_apps?access_token=EAAM4FiGDZCk0BAD7fZCNhTMquL8hjSlXZBDcE2TolBhxeFP898oGunmccqDxGYDCYfGMsSzErecMIBQZAcgHzegpT1rZAxX
```


