## CGI
### Along the way, data typically passes through three programs: 
1. from the client browser, 
2. to the web server, 
3. to the CGI script, 
4. and back again to the browser.

cgi_intro.py

## Web server

* To run CGI scripts at all, we need a web server that will serve up our HTML and launch our Python scripts on request. The server is a required mediator between the browser and the CGI script. If you don’t have an account on a machine that has such a server available, you’ll want to run one of your own. We could configure and run a full production-level web server such as the open source Apache system (which, by the way, can be tailored with Python-specific support by the mod_python extension). 
* In short, because Python provides precoded support for various types of network servers, we can build a CGI-capable and portable HTTP web server in just 8 lines of code (and a whopping 16 if we include comments and blank lines).
* It’s also easy to build proprietary network servers with low-level socket calls in Python, but the standard library provides canned implemen- tations for many common server types, web based or otherwise. The socketserver module, for instance, supports threaded and forking versions of TCP and UDP servers. Third-party systems such as Twisted provide even more implementations.