<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Forks][forks-shield]][forks-url]
[![Issues][issues-shield]][issues-url]
[![GNU General License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT ICON -->
<br />
<p align="center">
  <a href="https://github.com/
           /canvas-discord-bot">
    <img src="images/icon.png" alt="ICON" width="80" height="80">
  </a>

  <h3 align="center">UW Canvas Bot</h3>
  <p align="center">
    This script is for a discord bot that uses the instructor canvas api to retrieve assignments, quizzes, and discussion topics in version 1.0
    <br />
    <a href="https://github.com/khuongma/canvas-discord-bot"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/khuongma/canvas-discord-bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/khuongma/canvas-discord-bot/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)


### Built With

* [Python3.6](https://www.python.org/downloads/release/python-360/)
* [Discord Py](https://discordpy.readthedocs.io/en/latest/api.html)
* [Canvas LMS API](https://canvas.instructure.com/doc/api/)



<!-- GETTING STARTED -->
## Getting Started

Download the entire github repo and make sure you have the following things installed below.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* pip3.6
```sh
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
```sh
python get-pip.py
```
### Installation

1. Clone the repo
```sh
git clone https://github.com/khuongma/canvas-discord-bot.git
```
2. Install PIP packages
```sh
pip3.6 install bs4
```
```sh
pip3.6 install varname
```
```sh
pip3.6 install datetime
```
```sh
pip3.6 install pytz
```
```sh
pip3.6 install html
```
```sh
pip3.6 install json
```
```sh
pip3.6 install discord
```



<!-- USAGE EXAMPLES -->
## Usage

Currently this is only for channels. Further updates will feature private messaging of the bot and a more scalable for any school and any body to use. As well as a more intuitive design.

1. Download the repo
2. Replace these variables: 
discord_bot_token = '' #bot token here
canvas_api = token = '' #canvas api you generated from your account
canvas_course_id = \[''\] #course id found through the canvas api
<br> ** for multiple courses, format canvas_course_id as ['', '', ''] ex: ['1234567', '7654321', '4567890']**
3. Run the python script

Detailed documentation coming.



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the GNU GENERAL PUBLIC LICENSE. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Khuong Ma - khuongma@uw.edu

Project Link: [https://github.com/khuongma/canvas-discord-bot](https://github.com/khuongma/canvas-discord-bot)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/khuongma/repo.svg?style=flat-square
[contributors-url]: https://github.com/khuongma/canvas-discord-bot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/khuongma/canvas-discord-bot.svg?style=flat-square
[forks-url]: https://github.com/khuongma/canvas-discord-bot/network/members
[stars-shield]: https://img.shields.io/github/stars/khuongma/canvas-discord-bot.svg?style=flat-square
[stars-url]: https://github.com/khuongma/canvas-discord-bot/stargazers
[issues-shield]: https://img.shields.io/github/issues/khuongma/canvas-discord-bot.svg?style=flat-square
[issues-url]: https://github.com/khuongma/canvas-discord-bot/issues
[license-shield]: https://img.shields.io/github/license/khuongma/canvas-discord-bot.svg?style=flat-square
[license-url]: https://github.com/khuongma/canvas-discord-bot/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/khuongma
[product-screenshot]: images/screenshot.png
