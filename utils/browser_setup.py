import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv

load_dotenv()

class BrowserSetup:
    def __init__(self):
        self.implicit_wait = int(os.getenv("IMPLICIT_WAIT", 10))
        self.browser_type = os.getenv("BROWSER_TYPE", "chrome").lower()
        self.mobile_emulation = os.getenv("MOBILE_EMULATION", "true").lower() == "true"
        self.mobile_width = int(os.getenv("MOBILE_WIDTH", 430))
        self.mobile_height = int(os.getenv("MOBILE_HEIGHT", 932))
        self.mobile_pixel_ratio = float(os.getenv("MOBILE_PIXEL_RATIO", 3.0))
        self.driver = None

    def get_driver(self):
        if self.browser_type == "chrome":
            return self._setup_chrome_driver()
        else:
            # Default to Chrome if browser type is not recognized
            print(f"Browser type '{self.browser_type}' not supported. Using Chrome instead.")
            return self._setup_chrome_driver()

    def _setup_chrome_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Comment for headed mode
        options.add_argument("--disable-gpu")
        options.add_argument(f"--window-size={self.mobile_width},{self.mobile_height}")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-notifications")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        # Add arguments to suppress WebGL warnings while keeping important errors visible
        options.add_argument("--log-level=3")  # Only show severe errors (still shows critical errors)
        options.add_argument("--enable-unsafe-swiftshader")  # Address the specific WebGL warnings
        options.add_argument("--disable-features=WebUSB,UsbDeviceDetection")  # Disable USB warnings
        
        # Suppress only DevTools logging but keep other important errors
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        # Add mobile emulation if enabled
        if self.mobile_emulation:
            mobile_emulation = {
                "deviceMetrics": { 
                    "width": self.mobile_width, 
                    "height": self.mobile_height, 
                    "pixelRatio": self.mobile_pixel_ratio 
                },
                "userAgent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36"
            }
            options.add_experimental_option("mobileEmulation", mobile_emulation)
        
        # Use the known chromedriver.exe path directly
        chromedriver_path = r"C:\Users\alexa\.wdm\drivers\chromedriver\win32\135.0.7049.84\chromedriver-win32\chromedriver.exe"
        
        # Create a service with log redirection
        service = Service(
            executable_path=chromedriver_path,
            log_path=os.devnull,  # Redirect logs to null device
            service_args=["--verbose", "--log-path=NUL"]  # Additional args to suppress logs
        )
        
        self.driver = webdriver.Chrome(service=service, options=options)

        self.driver.implicitly_wait(self.implicit_wait)
        return self.driver

    def quit_driver(self):
        if self.driver:
            self.driver.quit()

    @staticmethod
    def take_screenshot(driver, name="screenshot"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_dir = "screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        
        filename = f"{screenshot_dir}/{name}_{timestamp}.png"
        driver.save_screenshot(filename)
        return filename
