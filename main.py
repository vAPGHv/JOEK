# -------=imports=-------
import pyautogui
import pyautogui
import keyboard


def click(key):
    if keyboard.is_pressed(key):
        pyautogui.click()


def clicks():
    while True:
        click("a")
        click("b")
        click("c")
        click("d")
        click("e")
        click("f")
        click("g")
        click("h")
        click("i")
        click("j")
        click("k")
        click("1")
        click("m")
        click("n")
        click("o")
        click("p")
        click("q")
        click("r")
        click("s")
        click("t")
        click("u")
        click("v")
        click("w")
        click("x")
        click("y")
        click("z")


clicks()
