# Launch Calendar 🚀

![](images/IMG_0015.JPG)

# Setup guide
After downloading the app, you will need your own Google Calendar API key in order to use it.
1) Go to https://developers.google.com/calendar/quickstart/python and follow step 1 to get your own API key.
2) Download the file. It should save under the filename ```credentials.json```
3) Afterwards, create a ```.env``` file in the main directory.
4) Copy over the contents of the ```.env.default``` file to your newly created ```.env``` file.
5) Open the ```credentials.json``` you downloaded in a text editor.
6) Following the format of the ```.env.default``` file you copied into ```.env```, locate the 
corresponding fields in your ```credentials.json``` and replace the variable values in ```.env``` with these new values.
    - No punctuation - just replace the entire default value with the value from ```credentials.json```

Next, run main.py from your IDE or from command-line:
```python3 main.py```

The app will prompt you to log into your Google Account. Choose the account you would like to give the app calendar access to.
- If you encounter an error, you may have input invalid .env values.


You should be all set. Follow the prompts and input command line inputs to start browsing and scheduling upcoming launches!

# Functionality

Launch Calendar lets you view 


# Credits

Launch Library v2 by The Space Devs
https://ll.thespacedevs.com/2.0.0/swagger

Google Calendar API by Google
https://developers.google.com/calendar/v3/reference

