Title: How I implemented googleSignIn in R (shiny) and lived
Date: 2019-03-16
Category: HowTo
Tags: R, google, login, googleAuthR, shiny, oauth2

Known user identity when building shiny apps can sometimes come really handy. While you can implement your own user login, for instance [using cookies](https://calligross.de/post/using-cookie-based-authentication-with-shiny/), you can also use some of the services which authenticate a user for you, such as Google. This way, you don't have to handle cookies or passwords, just a small part of bureaucracy in your database.

Enter [googleAuthR](https://code.markedmondson.me/googleAuthR/). You can use the Google Authentication system, which enables you to call its APIs (e.g. see [here](https://lesliemyint.wordpress.com/2017/01/01/creating-a-shiny-app-with-google-login/)), but sometimes a user login is just enough. This is where the accompanying module `googleSignIn` comes into play. Below is how I was able to implement this same name module with four lines of code, one line being loading the aforementioned library.

If you would be kind enough to scroll to the [`googleSignIn`](https://code.markedmondson.me/googleAuthR/articles/google-authentication-types.html#googlesignin-module-example) part of the page, you will notice code for a shiny app that (almost) just works. Read on to see what I mean by "almost".

The demo app has all the key components, it loads libraries, prepares `options("client_id")`, creates sign in button in `ui` (`googleSignInUI("demo")`), does the auth dance for you in the `server` part (`shiny::callModule(googleSignIn, "demo")`) when this button is pressed and, as gratis, displays the name, email and your google image. I run the app using `runApp(port = 1221)`!

<img src="{static}/images/googlesignin_app.png" class="center">

When I press the Sign in button, I get - bleh. Doesn't work.

<img src="{static}/images/googlesingin_invalid_request.png" class="center">

What is going on? The google console parameters check out.

<img src="{static}/images/googlesingin_console_restrictions.png" class="center">

Let me save you hours of clicking by pointing out this little bit from the documentation from the [`googleAuth` module](https://code.markedmondson.me/googleAuthR/articles/google-authentication-types.html#googleauth-module-example):

>... then make sure if you launch your app locally to change the ip address from `127.0.0.1` to `localhost` in your browser (Google doesn’t accept ip addresses).

In other words, in your web browser, just change `http://127.0.0.1:1221` to `http://localhost:1221`. The page should reload on its own. Click the sign in button et voilà.

<img src="{static}/images/googlesignin_signedin.png" class="center">
