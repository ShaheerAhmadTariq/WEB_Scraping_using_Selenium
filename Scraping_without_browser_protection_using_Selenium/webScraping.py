from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pprint
import time
def startWebScrapping():
    driver = webdriver.Firefox()
    driver.get("https://www.analog.com/en/products.html")

    # To click accept all for cookie consent form
    driver.find_element(By.XPATH, '//a[text()=" Accept All "]').click()

    time.sleep(5)
    # To find all products
    categories = driver.find_elements(By.CLASS_NAME, 'prodsubcat')

    """ categories will contain following products
    Amplifiers
    Analog Functions
    A/D Converters (ADC)
    Audio Products
    Clock and Timing
    D/A Converters (DAC)
    Embedded Security and 1-Wire
    High Speed Logic and Data Path Management
    iButton and Memory
    Industrial Ethernet Solutions
    Interface and Isolation
    Power Monitor, Control, and Protection
    Optical Communications and Sensing
    Power Management
    Processors and Microcontrollers
    RF and Microwave
    Sensors and MEMS
    Switches and Multiplexers
    Video Products"""

    # To find all subcategories of each product
    # To store each product and subcategories in dictionary
    """the dict will look like this
        {'product1_name':[list of subcategories],
        'product2_name':[list of subcategories],..}
        """
    # to find the subcategories
    """ the structure of html page looks like this

        <div>
            <div>
                <div>
                    <div class="category">products</div>
                </div>
            </div>
            <ul>
                <li>subcategories01</li>
                <li>subcategories02</li>
            </ul>
        </div>
        we have category div. so to get to the subcategory <li> we have to find the parents,grandparents,great-grandparents
    """

    categories_Dict = {}
    for category in categories:
        parent_node = category.find_element(By.XPATH, "..")
        grand_parent = parent_node.find_element(By.XPATH, "..")
        great_grand_parent = grand_parent.find_element(By.XPATH, "..")
        subcategories = great_grand_parent.find_elements(By.XPATH, ".//ul/li")
        
        categories_Dict[category.text] = []
        for subcategorie in subcategories:
            try:
                categories_Dict[category.text].append(subcategorie.text)
            except:
                continue
    """ categories_Dict contains
    {'A/D Converters (ADC)': ['High Speed A/D Converters >10 MSPS',
                            'Integrated/Special Purpose A/D Converters',
                            'Precision A/D Converters'],
    'Amplifiers': ['Differential Amplifiers and ADC Drivers',
                    'Instrumentation Amplifiers',
                    'Isolation Amplifiers',
                    'Operational Amplifiers (Op Amps)',
                    'RF Amplifiers',
                    'RF Power Detectors',
                    'Specialty Amplifiers',
                    'Variable Gain Amplifiers (VGA)'],
    'Analog Functions': ['Analog Multipliers & Dividers',
                        'Comparators',
                        'Current Mirrors',
                        'Filters',
                        'Matched Transistors',
                        'Precision Modulators/Demodulators',
                        'Precision Resistor Network',
                        'RMS to DC Converters',
                        'Switched Cap Building Blocks',
                        'Voltage References'],
    'Audio Products': ['Audio A/D Converters',
                        'Audio Amplifiers',
                        'Audio CODECs',
                        'Audio D/A Converters',
    ...
                        'Video Compression',
                        'Video Decoders',
                        'Video Encoders'],
    'iButton and Memory': ['iButton Devices and Accessories', 'Memory IC']}"""



    driver.quit()
    return categories_Dict
    