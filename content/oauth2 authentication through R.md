Title: How to authenticate using OAuth2 through R
Date: 2019-01-20
Category: HowTo
Tags: R, oauth2, httr, curl, API, token, scope

If you need to have authentication of users in your application, you could invent the proverbial warm water by implementing register, login, logout and other features. Or, you could outsource part of that functionality to well established establishments such as Google, Facebook, Github and other. In addition to knowing the identity of your user, you can potentially gain access to service's APIs, which can be very handy (such as access to users' calendars, e-mail boxes, etc...).

In this post, you will learn how to set up authentication using OAuth2 using google, but the process is similar(ly painful) for other services.

If you do not know how OAuth2 works, you may want to check out the figures [here](https://www.joyofdata.de/blog/oauth2-google-api-python-google-analytics/) and [here](https://developers.google.com/identity/protocols/OAuth2). Basically it works by sending your user (pops up a website) to a service (e.g. Google), where they confirm access to their data (scope). On return, they will bring with them a "code". This code is then traded in by you at the service desk for a token, which acts as a pass to see particular user's data. Store this somewhere safe.

To accomplish this, R package [`httr`](https://github.com/r-lib/httr) comes equipped with all the lingo needed to successfully talk to services. There are some good demos in package [source code](https://github.com/r-lib/httr/blob/master/demo), however, it perhaps lacks some minor details. This post will perhaps shine some light on those details, but who knows how long the screenshots will be relevant. Hopefully at least ideas will be evergreen for the foreseeable future.

If you haven't done so yet, head over to the [google developers' console]() and create a new project. In the Credentials menu, create new OAuth client ID credentials.

<img src="{static}/images/create_client_id.png" width="760">

Select Web application and fill out application name and Authorized redirect URIs. This is the URI where user will be diverted to once the authentication has been confirmed. For testing purposes, make sure this is `http://localhost/` (notice the trailing slash). Once deployed, the URI here would be sent back to your application's address.
You can fetch `secret` and `key` from the Client ID for Web application menu, depicted as black stripes on the figure below.

<img src="{static}images/client_secret.png" width="760">

Make sure you visit the OAuth consent screen tab and fill in any necessary information needed for transparent functioning of your application.

```
# Below are mock secret and key, they will not work. They are just an example of what they
#  would look like. Replace with your.
secret <- "vxR9AuyJ4cEwrPNaylaTyC3AfXWIEdQnFotju9Yc6Q4og.apps.googleusercontent.com
key <- "afL4IguOXCXC6-bPV9lObvxT"
```

We send the user to choose which account to authenticate with (a new window pops open) and then are returned a token. This token is then used to request any information needed by your app and authorized by the user. To read more on Google scopes, read [here](https://developers.google.com/identity/protocols/googlescopes).

This is an example of scope for OAuth2 API.
<img src="{static}/images/google_scopes.png" width="760">

```
# Ask user to authorize access to his or her data and gain a token.
auth.code <- oauth2.0_token(endpoint = oauth_endpoints("google"),
                            app = app,
                            scope = "https://www.googleapis.com/auth/userinfo.profile")

# Use token to fetch the actual data.
req <- GET("https://www.googleapis.com/oauth2/v1/userinfo",
           config(token = auth.code))

# This step is needed so that if the call fails, you will be
#  able to detect it and handle it R-way. You are best off wrapping this into
#  a `tryCatch` call if not in interactive session.
stop_for_status(req)
```

The result would look something along these lines.

```
# I changed sensitive information for this display, so don't bother. :)
> str(content(req))
List of 8
 $ id         : chr "754846239037474839489"
 $ name       : chr "Roman Luštrik"
 $ given_name : chr "Roman"
 $ family_name: chr "Luštrik"
 $ link       : chr "https://plus.google.com/754846239037474839489"
 $ picture    : chr "https://lh500600.googleusercontent.com/-32gefACRE/ACCAXSDFCASC/XAAXEXF/asdCac_/photo.jpg"
 $ gender     : chr "other"
 $ locale     : chr "en"
```

If you would also like to fetch user's e-mail address, you will need to extend the scope. Note that the query has changed and you will be, once again, asked to confirm that you allow your e-mail address be accessed by the app.

```
auth.code <- oauth2.0_token(endpoint = oauth_endpoints("google"),
                            app = app,
                            scope = c("https://www.googleapis.com/auth/userinfo.profile",
                                      "https://www.googleapis.com/auth/userinfo.email")
)

req <- GET("https://www.googleapis.com/oauth2/v1/userinfo",
           config(token = auth.code))

stop_for_status(req)
str(content(req))

List of 10
 $ id           : chr "754846239037474839489"
$ email         : chr "name@gmail.com"
$ verified_email: logi TRUE
$ name          : chr "Roman Luštrik"
$ given_name    : chr "Roman"
$ family_name   : chr "Luštrik"
$ link          : chr "https://plus.google.com/754846239037474839489"
$ picture       : chr "https://lh500600.googleusercontent.com/-32gefACRE/ACCAXSDFCASC/XAAXEXF
$ gender        : chr "other"
$ locale        : chr "en"
```
#### Error log
Restarting my R session, updating `httr` and making sure that the redirect URI was set to `http://localhost/` solved my problem with this error below.
```
> ggl.token <- oauth2.0_token(endpoint = oauth_endpoints("google"),
+                             app = app,
+                             scope = "https://www.googleapis.com/auth/userinfo.profile")
Waiting for authentication in browser...
Press Esc/Ctrl + C to abort
Authentication complete.
Error in curl::curl_fetch_memory(url, handle = handle) :
  Could not resolve host: accounts.google.com
```

I came to the idea of restarting my R session when surefire stuff didn't work, such as updating R package(s) using `devtools::install_github`.

```
> devtools::install_github("r-lib/httr")
Installation failed: curl::curl_fetch_disk(url, x$path, handle = handle) : Could not resolve host: raw.githubusercontent.com
```
