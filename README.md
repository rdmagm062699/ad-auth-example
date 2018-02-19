---
services: active-directory-b2c
platforms: python
---

# Sign in Azure AD Users using Python-Flask Open Source Libraries

This sample demonstrates how to use a 3rd party Python-Flask library ([flask-oauthlib](https://github.com/lepture/flask-oauthlib)) to do oAuth 2.0 against Azure AD.  It then validates the access token using another 3rd party library ([python-jose](https://github.com/mpdavis/python-jose)).


## How To Run This Sample

Getting started is simple! To run this sample you will need to install your dependencies.  Create an appropriate virtual environment and run the following command:    

```
pip install -r requirements.txt
```

### Step 1:  Clone or download this repository

From your shell or command line:

`git clone [THIS REPOSITORY]`

### Step 2: Run the sample using our sample tenant

TODO: Fix this documentation (copied from another Microsoft example:

If you'd like to see the sample working immediately, you can simply run the app as-is without any code changes. The default configuration for this application performs sign-in & sign-up using our sample B2C tenant, `fabrikamb2c.onmicrosoft.com`.  It uses a [policy](https://azure.microsoft.com/documentation/articles/active-directory-b2c-reference-policies) named `b2c_1_susi`. Sign up for the app using any of the available account types, and try signing in again with the same account.

Run this sample with the following by setting your flask environment variable and running the sample in the terminal.

```
$ export FLASK_APP=example_app.py && flask run
```

You can then navigate to `http://localhost:5000`.

### Step 3: Create your own application

TODO: Fix this documentation (copied from another Microsoft example:

Now you need to create your own appliation in your B2C tenant, so that your app has its own client ID.  You can do so following [the generic instructions here](https://azure.microsoft.com/documentation/articles/active-directory-b2c-app-registration).  Be sure to include the following information in your app registration:

- Enable the **Web App/Web API** setting for your application.
- Add a redirect_uri for your app. For this sample, it should be in the form of: `https://yourwebsite/login/authorized`. The OAuth library
- Copy the client ID generated for your application, so you can use it in the next step.
- Generate a client secret for your application.

### Step 6: Configure the sample to use your Application

TODO: Fix this documentation (copied from another Microsoft example:

Now you can replace the app's default configuration with your own.  Open the `b2cflaskapp.py` file and replace the following values with the ones you created in the previous steps.  

```python
tenant_id = 'fabrikamb2c.onmicrosoft.com'
client_id = 'fdb91ff5-5ce6-41f3-bdbd-8267c817015d'
client_secret = 'YOUR_SECRET'
policy_name = 'b2c_1_susi'
```
## Questions and Issues

TODO: Fix this documentation (copied from another Microsoft example:

Please file any questions or problems with the sample as a github issue.  You can also post on StackOverflow with the tag ```azure-ad-b2c```.  For oAuth2.0 library issues, please see note above.

This sample was tested with Python 2.7.10, Flask 0.11.1, Flask-OAuthlib 0.9.3 and python-jose 1.3.2

## Acknowledgements

TODO: Fix this documentation (copied from another Microsoft example:

The flask & django libraries are built ontop of the core python oauthlib.

[flask-oauthlib](https://github.com/lepture/flask-oauthlib)

[python-jose](https://github.com/mpdavis/python-jose)

[oauthlib](https://github.com/idan/oauthlib)

[django-oauth-toolkit](https://github.com/evonove/django-oauth-toolkit)
