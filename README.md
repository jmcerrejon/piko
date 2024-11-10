# PIKO

![piko.png](res/piko.jpg)

I'm PIKO! The new AI created from the collective mind of trillions of flies.

🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰🪰

## Table of Contents 🪰

-   [Introduction](#introduction)
-   [Installation](#installation)
-   [Setting Up](#setting-up)
-   [Usage](#usage)
-   [Testing](#testing)
-   [TODO](#todo)
-   [License](#license)
-   [Reference Links](#reference-links)

## Introduction

**PIKO** is an AI designed to harness the collective intelligence of trillions of flies. This `README` will guide you through the process of setting up and using _PIKO_.

## Installation

### Install Requirements? It's not necessary!

The script will install the necessary dependencies when It's run for the first time. 🤯

## Setting Up

Copy the example environment file `.env.example` to `.env` and add your _API keys_:

```sh
cp .env.example .env
```

Edit the `.env` file to include your _API key_.

## Usage

The script will make a virtual environment If doesn't exists and install the necessary dependencies for the first time.

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
-   [x] Check venv and install requirements automatically.
-   [x] Add testing.
-   [ ] Add other models.
-   [ ] Detect and use your local language.
-   [ ] Add more commands.
-   [ ] GUI/TUI mode.
-   [ ] Refactor stuffs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Reference Links

-   [OpenAI Python Library](https://github.com/openai/openai-python)

Made with :heart: and 🪰 using _Python_.
