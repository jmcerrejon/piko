# PIKO

![piko.png](res/piko.jpg)

I'm PIKO! The new AI created from the collective mind of trillions of flies.

🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰

## Table of Contents 🪰

-   [Introduction](#introduction)
-   [Prerequisites](#prerequisites)
-   [Installation](#installation)
-   [Setting Up](#setting-up)
-   [Usage](#usage)
-   [Testing](#testing)
-   [TODO](#todo)
-   [License](#license)
-   [Reference Links](#reference-links)

## Introduction

PIKO is an AI designed to harness the collective intelligence of trillions of flies. This README will guide you through the process of setting up and using PIKO.

## Prerequisites

Before you begin, ensure you have the following installed:

-   Python 3

## Installation

### Install Dependencies

To install the necessary dependencies, run:

```sh
python3 -m pip install --upgrade pip
```

### Create and Activate Virtual Environment

Create a virtual environment to manage dependencies & activate the virtual environment:

```sh
python3 -m venv venv
source venv/bin/activate
```

### Install Requirements

Install the required Python packages:

```sh
pip install -r requirements.txt
```

## Setting Up

Copy the example environment file `.env.example` to `.env` and add your _API keys_:

```sh
cp .env.example .env
```

Edit the `.env` file to include your _API key_.

## Usage

To start using PIKO, run the following command:

```sh
python3 -u main.py
```

## Testing

To run the tests, run the following command:

```sh
python -m unittest discover -s tests/units
```

## TODO

-   [x] Add .env file.
-   [x] CLI mode.
-   [ ] Add testing (WIP).
-   [ ] Add other models.
-   [ ] Add more commands.
-   [ ] GUI/TUI mode.
-   [ ] Refactor stuffs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Reference Links

-   [OpenAI Python Library](https://github.com/openai/openai-python)

Made with :heart: and 🪰 using _Python_.
