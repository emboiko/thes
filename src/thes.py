from sys import argv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Thesaurus_Page import Thesaurus_Page


def main():
    if (
        (len(argv) < 2) or (len(argv) >=4)
        ):
        print("Usage:\n")
        print("thes {word | \"a phrase\"} [limit]\n\n")
        return

    limit = None
    if len(argv) == 3:
        limit = int(argv[2])

    search_term = argv[1]

    options = Options()
    options.headless = True
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = webdriver.Chrome(options=options)

    thes_page = Thesaurus_Page(driver=browser)
    thes_page.go()
    thes_page.search_input.input_text(search_term)
    thes_page.search_button.click()

    results = browser.find_elements_by_xpath(
        ".//div/h2[text()='other words for ']/../ul/li/div/a"
    )

    if (results):
        for i, result in enumerate(results):
            if limit and i >= limit:
                break
            print(i+1, ": ", result.text.strip())
    else:
        print("No results found.")

    browser.quit()


if __name__ == "__main__":
    main()
