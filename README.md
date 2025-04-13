# Twitch.tv Test Automation Framework

A robust, maintainable test automation framework using Selenium in Python to automate scenarios on Twitch.tv. This framework follows the Page Object Model (POM) design pattern and uses pytest for test execution.

## Framework Structure

```
WapProject/
│
├── .env                      # Environment variables
├── .env.example              # Example environment variables
├── poetry.lock               # Poetry lock file
├── pyproject.toml            # Poetry dependencies
├── pytest.ini                # Pytest configuration
├── README.md                 # Documentation
│
├── tests/                    # Test files
│   ├── __init__.py
│   ├── conftest.py           # Pytest fixtures
│   └── test_search_streamer.py # Main test case
│
├── pages/                    # Page Objects
│   ├── __init__.py
│   ├── base_page.py          # Base page with common methods
│   ├── home_page.py          # Twitch homepage
│   ├── search_results_page.py # Search results page
│   └── streamer_page.py      # Streamer page
│
├── locators/                 # Element locators
│   ├── __init__.py
│   ├── home_locators.py      # Homepage locators
│   ├── search_results_locators.py # Search results locators
│   └── streamer_page_locators.py # Streamer page locators
│
├── utils/                    # Utilities
│   ├── __init__.py
│   └── browser_setup.py      # WebDriver setup
│
└── screenshots/              # Directory for screenshots
    ├── starcraft_streamer_*.png  # Test run screenshots
    └── test_results.png      # Example test results
```

## Features

- **Page Object Model**: Separates test logic from page interactions
- **Pytest Fixtures**: Reusable components for test setup and teardown
- **Type Hints**: Improved code readability and IDE support
- **Mobile Emulation**: Tests run in mobile emulation mode
- **Screenshot Capture**: Automatically save screenshots during test execution
- **Environment Variables**: Configure test behavior through .env file

## Prerequisites

- Python 3.8 or higher
- Poetry (dependency management)
- Chrome browser
- ChromeDriver (matching your Chrome version)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/iacretan/WapProject.git
cd WapProject
```

### 2. Install Poetry

If you don't have Poetry installed:

#### Windows:
```bash
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

#### macOS/Linux:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### 3. Install Dependencies

```bash
poetry install
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory with the following content:

```
BROWSER_TYPE=chrome
BASE_URL=https://www.twitch.tv
IMPLICIT_WAIT=10
EXPLICIT_WAIT=20
MOBILE_EMULATION=true
MOBILE_WIDTH=430
MOBILE_HEIGHT=932
MOBILE_PIXEL_RATIO=3.0
```

### 5. ChromeDriver Setup

The framework is configured to use ChromeDriver from a specific path. You may need to update this path in `utils/browser_setup.py` to match your ChromeDriver location:

```python
# In utils/browser_setup.py
chromedriver_path = r"C:\Users\alexa\.wdm\drivers\chromedriver\win32\135.0.7049.84\chromedriver-win32\chromedriver.exe"
```

Alternatively, you can use webdriver-manager to automatically download and manage the ChromeDriver:

```python
from webdriver_manager.chrome import ChromeDriverManager
chromedriver_path = ChromeDriverManager().install()
```

### 6. Create Screenshots Directory

The framework will automatically create a `screenshots` directory if it doesn't exist, but you can create it manually:

```bash
mkdir screenshots
```

## Running Tests

### Using Poetry

The recommended way to run tests is using Poetry:

```bash
poetry run pytest tests/test_search_streamer.py -v
```

### Using pytest directly

If you want to use pytest directly, you need to activate the Poetry virtual environment:

#### Windows (PowerShell):
```powershell
poetry shell
pytest tests/test_search_streamer.py -v
```

#### macOS/Linux:
```bash
poetry shell
pytest tests/test_search_streamer.py -v
```

## Test Scenario

The main test case (`test_search_streamer.py`) implements the following scenario:
1. Navigate to Twitch.tv
2. Accept cookies if present
3. Search for "StarCraft II"
4. Scroll down twice on the results page
5. Select a streamer
6. Wait for the streamer page to load
7. Take a screenshot

## Test Results

Here's an example of a captured screenshot from a test run:

![Starcraft Streamer Screenshot](./screenshots/Screenshot%202025-04-13%20164222.png)

The test will also generate screenshots in the `screenshots/` directory with timestamps.

## Troubleshooting

### WebGL Warnings
The framework includes configuration to suppress common WebGL warnings that appear when running Chrome in automated mode. These settings can be found in `utils/browser_setup.py`.

### ChromeDriver Path
The framework uses a hardcoded path to ChromeDriver. If you need to use a different ChromeDriver, update the path in `utils/browser_setup.py`.

### Common Issues

1. **Element Not Found Exceptions**:
   - Twitch UI may change frequently. Check and update locators in the locators directory.
   - Increase the `EXPLICIT_WAIT` value in your `.env` file.

2. **ChromeDriver Version Mismatch**:
   - Ensure your ChromeDriver version matches your Chrome browser version.
   - Consider using webdriver-manager to automatically manage ChromeDriver versions.

3. **Mobile Emulation Issues**:
   - If you encounter issues with mobile emulation, you can disable it by setting `MOBILE_EMULATION=false` in your `.env` file.

## Framework Components

### Page Objects

The framework uses the Page Object Model pattern to represent web pages as classes:

- `BasePage`: Contains common methods for all pages
- `HomePage`: Represents the Twitch.tv homepage
- `SearchResultsPage`: Represents the search results page
- `StreamerPage`: Represents an individual streamer's page

### Locators

Element locators are separated into their own classes:

- `HomeLocators`: Locators for the homepage
- `SearchResultsLocators`: Locators for the search results page
- `StreamerPageLocators`: Locators for the streamer page

### Fixtures

The framework provides several fixtures in `conftest.py`:

- `driver`: Creates and manages the WebDriver instance
- `home_page`: Creates a HomePage instance
- `search_results_page`: Creates a SearchResultsPage instance
- `streamer_page`: Creates a StreamerPage instance

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request
