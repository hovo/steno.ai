<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h1 align="center">Steno.Ai</h1>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [License](#license)



<!-- ABOUT THE PROJECT -->
## About The Project
![](ezgif.com-video-to-gif.gif)

### Built With
Steno.ai utilizes the following frameworks and libraries:
* [Flask](http://flask.pocoo.org/)
* [Google Cloud](https://cloud.google.com/speech-to-text/docs/reference/libraries)
* [Vue.js](https://vuejs.org/)
* [Buefy](https://buefy.org/)



<!-- GETTING STARTED -->
## Getting Started
To run the client library, you must first set up authentication by creating a service account and setting an environment variable. For more information visit: https://cloud.google.com/docs/authentication/production
### Prerequisites

Provide authentication credentials to your application code by setting the environment variable GOOGLE_APPLICATION_CREDENTIALS. Replace [PATH] with the file path of the JSON file that contains your service account key, and [FILE_NAME] with the filename. This variable only applies to your current shell session, so if you open a new session, set the variable again.


```sh
export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"
```

### Installation

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

