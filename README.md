---
services: azure-graph-api, active-directory-b2c
platforms: python
author: adammartin-hisc
---

# Sign in Azure AD Users using Python-Flask Open Source Libraries

This sample demonstrates how to use a 3rd party Python-Flask library ([flask-oauthlib](https://github.com/lepture/flask-oauthlib)) to do oAuth 2.0 against Azure AD.  This then grabs identities from Azure B2C and shows them as a list.


## How To Run This Sample

Getting started is simple! To run this sample you will need to install your dependencies.  Create an appropriate virtual environment and run the following command:    

```
pip install -r requirements.txt
```

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

### Step 2: Run the sample using our sample tenant

Run this sample with the following by setting your flask environment variable and running the sample in the terminal.

Create a `config/config.yml` file and add the following content (with appropriate data from previous steps):

```json
client_id: [YOUR CLIENT ID FROM PREVIOUS STEP]
client_secret: [YOUR CLIENT SECRET FROM PREVIOUS STEP]
microsoft_graph_api_url: 'https://graph.microsoft.com/v1.0/'
user_attributes: 'id,businessPhones,city,companyName,country,department,displayName,givenName,hireDate,imAddresses,interests,jobTitle,mail,mailNickname,mobilePhone,mySite,officeLocation,pastProjects,postalCode,preferredLanguage,preferredName,proxyAddresses,responsibilities,schools,skills,state,streetAddress,surname,usageLocation,userPrincipalName,userType'
ad_graph_url: 'https://graph.windows.net'
graph_tenant_id: [YOUR GRAPH TENANT ID]
graph_client_id: [YOUR GRAPH CLIENT APP ID]
graph_client_secret: [YOUR GRAPH CLIENT SECRET]
```

run the following from command line

```
$ python run.py
```

You can then navigate to `http://localhost:8080`.
