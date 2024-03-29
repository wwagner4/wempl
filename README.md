# WEMPL

## Description
Dynamic Content with Environment Variables

This webserver offers a powerful feature for generating dynamic content: environment variable substitution. You can embed placeholders within your webpages or configurations that automatically get replaced with the corresponding environment variable values. This allows you to:

* Centralized Configuration: Manage critical settings like database connection strings, API keys, or file paths in environment variables. Update these values in one place, and they propagate throughout your entire web application.

* Flexible Deployment: Easily adapt your webserver to different environments (development, staging, production) by setting specific environment variables for each. No need to modify code for each deployment.

The webserver is based on [nginx](https://www.nginx.com/) and the [nginx  substitution module](https://www.nginx.com/resources/wiki/modules/substitutions/). It uses the 
docker image [cecton/nginx-with-substitution-filter](https://github.com/cecton/nginx-with-substitution-filter)

## Configuration

### Variables
A variable looks like "WEMPL_<NAME>" where name can be any string
you can use in [environment variabels](https://en.wikipedia.org/wiki/Environment_variable). Environment variables are not case sensitive. The WEMPL_
prefix is mandatory.

Examples:
* WEMPL_HELLO="hello wempl"
* WEMPL_HOST="localhost"
* WEMPL_URL="http://entelijan.net"

### Usage of environment variables

The following example shows the usage of WEMPL_HELLO
```html
<!DOCTYPE html>
<style>
    body {
        background-color: rgb(238, 255, 53);
        font-family: monospace;
        font-size: 120px;
    }
    .wempltext {
        margin-top: 1em;
        text-align: center;
    }
</style>
<body>
    <div class="wempltext">{{ WEMPL_HELLO }}</div>
</body>
```
There must be exactly one space character after "\{\{" and before "\}\}"

## Getting started

Prerequisites: 
* Have docker or another container runtime installed on your computer.
* Inside the 'example' directory of this repository call
```docker run -v .:/usr/share/nginx/html -p 80:80 -e WEMPL_HALLO="Hallo Wempl :)" wwagner4/wempl-nginx:1.0```
* If you open your browser on ```http://localhost``` you should see "Hallo Wempl :)" 