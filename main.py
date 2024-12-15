"""
import bs4
import requests
from selenium import webdriver 
from selenium.webdriver.support import select
import time
soup = bs4.BeautifulSoup()

link = "https://icanhazip.com/"
link2 = "https://browser-info.ru/"
link3 = "https://2ip.ru/browser-info/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
}

#response = requests.get(link3, timeout=30, headers=headers)
#print(response.text)



browser = webdriver.Chrome()
time.sleep(10)
browser.get(link3)
time.sleep(10)
generated_html = browser.find_element("xpath", "/html/body/div[1]/div[3]/div/div[2]/div[1]/div/div[2]/div/section[2]/table/tbody")
print(generated_html)
input()
browser.quit()"""
import numpy as np

# Define the resistances
R1 = 20
R2 = 40
R3 = 18
R4 = 10
R5 = 10
R6 = 25
R7 = 20
RE = 16
E = 100

# Coefficient matrix
A = np.array([
    [1/R1 + 1/R2 + 1/R3, -1/R2, -1/R3, 0],
    [-1/R2, 1/R2 + 1/R4 + 1/R5, -1/R4, -1/R5],
    [-1/R3, -1/R4, 1/R3 + 1/R4 + 1/R6, -1/R6],
    [0, -1/R6, -1/R5, 1/R5 + 1/R6 + 1/R7]
])

# Right-hand side vector
b = np.array([
    0,
    0,
    0,
    (E / RE)
])

# Solve the system of equations
voltages = np.linalg.solve(A, b)

# Extract node voltages
V1, V2, V3, V4 = voltages

# Calculate currents through each resistor
I1 = V1 / R1
I2 = (V2 - V1) / R2
I3 = (V3 - V1) / R3
I4 = (V3 - V4) / R4
I5 = (V4 - V3) / R5
I6 = (V2 - V4) / R6
I7 = V4 / R7

# Calculate power dissipated in each resistor
P1 = I1**2 * R1
P2 = I2**2 * R2
P3 = I3**2 * R3
P4 = I4**2 * R4
P5 = I5**2 * R5
P6 = I6**2 * R6
P7 = I7**2 * R7

# Print results
print(f"Node Voltages: V1 = {V1:.2f} V, V2 = {V2:.2f} V, V3 = {V3:.2f} V, V4 = {V4:.2f} V")
print(f"Currents: I1 = {I1:.2f} A, I2 = {I2:.2f} A, I3 = {I3:.2f} A, I4 = {I4:.2f} A, I5 = {I5:.2f} A, I6 = {I6:.2f} A, I7 = {I7:.2f} A")
print(f"Powers: P1 = {P1:.2f} W, P2 = {P2:.2f} W, P3 = {P3:.2f} W, P4 = {P4:.2f} W, P5 = {P5:.2f} W, P6 = {P6:.2f} W, P7 = {P7:.2f} W")