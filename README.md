<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/douglasdubois/GameStop-Scraper">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">GameStop Scraper</h3>

  <p align="center">
    A lightweight program designed to pull product data from www.gamestop.com and send an email notification once a desired product becomes available. 
    <br />
    <a href="https://github.com/douglasdubois/GameStop-Scraper"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/douglasdubois/GameStop-Scraper">View Demo</a>
    ·
    <a href="https://github.com/douglasdubois/GameStop-Scraper/issues">Report Bug</a>
    ·
    <a href="https://github.com/douglasdubois/GameStop-Scraper/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

A lightweight program designed to pull product data from www.gamestop.com and send an email notification once a desired product becomes available.

### Built With

* [Python](https://www.python.org/)

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* python3

  To see which version of Python 3 you have installed, open a command prompt and run

  `python3 --version`

  If you are using Ubuntu 16.10 or newer, then you can easily install Python 3.6 with the following commands:

  ```sh
  sudo apt-get update
  sudo apt-get install python3.6
  ```

### Installation

1. Clone the repo
   `git clone https://github.com/douglasdubois/GameStop-Scraper.git`

2. Download [ChromeDriver](https://chromedriver.chromium.org/downloads), extract to project root, and add to path
   `echo 'export PATH=$PATH:/path/to/chromedriver' >> ~/.bashrc`

<!-- USAGE EXAMPLES -->
## Usage

1. Replace variables in [`.env`](https://github.com/douglasdubois/GameStop-Scraper/blob/main/.env).

2. Replace name and url in [`products.json`](https://github.com/douglasdubois/GameStop-Scraper/blob/main/products.json) with the product you want to be notified of when available. You can add as many products following the same format.

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/douglasdubois/GameStop-Scraper/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch
   `git checkout -b feature/AmazingFeature`
3. Commit your Changes
   `git commit -m 'Add some AmazingFeature'`
4. Push to the Branch
   `git push origin feature/AmazingFeature`
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the GNU General Public License. See [`LICENSE`](https://github.com/douglasdubois/GameStop-Scraper/blob/main/LICENSE) for more information.

<!-- CONTACT -->
## Contact

Douglas DuBois - [@douglasadubois](https://twitter.com/douglasadubois) - douglas.dubois1@gmail.com

Project Link: [https://github.com/douglasdubois/GameStop-Scraper](https://github.com/douglasdubois/GameStop-Scraper)

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Dalton Edmisten](https://github.com/deuce109)
