import pyautogui
from PIL import Image
import pytesseract
import time

# Set the path to the Tesseract OCR executable (change this according to your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save('screenshot.png')
    return 'screenshot.png'

def extract_text(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def move_and_click():
    # Adjust these coordinates according to your needs
    target_x, target_y = 500, 500
    pyautogui.moveTo(target_x, target_y)
    pyautogui.click()

def main():
    # Take a screenshot
    screenshot_path = take_screenshot()

    # Extract text from the screenshot
    extracted_text = extract_text(screenshot_path)
    print("Extracted Text:", extracted_text)

    # Check if a certain text is present
    target_text = "Your target text"
    if target_text in extracted_text:
        print(f"Target text '{target_text}' found!")

        # Move the mouse and click
        move_and_click()
        print("Mouse moved and clicked.")
    else:
        print(f"Target text '{target_text}' not found.")

if __name__ == "__main__":
    main()