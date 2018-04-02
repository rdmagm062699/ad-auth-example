---
services: azure-graph-api, active-directory-b2c
platforms: python
author: adammartin-hisc
---

# Prerequisites

Before working this repository you will need:

* (Pyenv)[https://github.com/pyenv/pyenv] - This is for the purpose of managing python version consistently.  Please check the .python-version file for the current version required for the spike.
* (Virtualenv or Equivalent)[http://docs.python-guide.org/en/latest/dev/virtualenvs/] - There are multiple ways to manage virtual environments but you should control/isolate both your python version and the dependencies you leverage.

# Sign in Azure AD Users using Python-Flask Open Source Libraries

This sample demonstrates how to use a 3rd party Python-Flask library ([flask-oauthlib](https://github.com/lepture/flask-oauthlib)) to do oAuth 2.0 against Azure AD.  This then grabs identities from Okta and shows them as a list.  In addition it allows for the creation of new CAREGivers in Okta.


## How To Run This Sample

### Step 1:  Clone or download this repository

From your shell or command line:

`git clone [THIS REPOSITORY]`

### Step 2: Create your own application

Now you need to create your own appliation in your AD tenant, so that your app has its own client ID.

- Enable the **Web App/Web API** setting for your application.
- Add a redirect_uri for your app. For this sample, it should be in the form of: `https://yourwebsite/login/authorized`. The OAuth library
- Copy the client ID generated for your application, so you can use it in the next step.
- Generate a client secret for your application.

You will also need a Graph API app if you are going to properly generate the list of identities.

### Step 3: Run the sample using our sample tenant

Create an appropriate virtual environment and run the following command:    

```
pip install -r requirements.txt
```

Run this sample with the following by setting your flask environment variable and running the sample in the terminal.

Create a `config/config.yml` file and add the following content (with appropriate data from previous steps):

```json
client_id: [YOUR_CLIENT_ID]
client_secret: [YOUR_CLIENT_SECRET]
microsoft_graph_api_url: 'https://graph.microsoft.com/v1.0/'
user_attributes: 'id,businessPhones,city,companyName,country,department,displayName,givenName,hireDate,imAddresses,interests,jobTitle,mail,mailNickname,mobilePhone,mySite,officeLocation,pastProjects,postalCode,preferredLanguage,preferredName,proxyAddresses,responsibilities,schools,skills,state,streetAddress,surname,usageLocation,userPrincipalName,userType'
ad_graph_url: 'https://graph.windows.net'

iam_server_url: https://homeinstead-poc.okta.com
iam_client_secret: [TOKEN_SUPPLIED_BY_OKTA]
iam_user_attributes: 'id,login,first_name,last_name,franchises,status'
iam_default_password: [DEFAULT_PASSWORD_WHEN_CREATING_A_USER]
iam_default_caregiver_group_ids:
  - [DEFAULT_CAREGIVER_GROUP_ID]
```

run the following from command line

```
$ python run.py
```

You can then navigate to `http://localhost:8080`.
