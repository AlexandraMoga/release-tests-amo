import pytest
from selenium.webdriver.common.by import By

from pages.desktop.frontend.blog_homepage import BlogHomepage
from pages.desktop.frontend.home import Home


@pytest.mark.nondesstructive
def test_header_logo_button(base_url, selenium):
    selenium.get(f'{base_url}/blog/')
    page = BlogHomepage(selenium, base_url).wait_for_page_to_load()
    page.header.click_title()
    homepage = Home(selenium, base_url)
    assert homepage.hero_banner


@pytest.mark.nondesstructive
def test_articles_elements_are_displayed(base_url, selenium):
    selenium.get(f'{base_url}/blog/')
    page = BlogHomepage(selenium, base_url).wait_for_page_to_load()
    for article in page.articles:
        assert article.image.is_displayed()
        assert article.title
        assert article.date
        assert article.intro_text
        assert article.read_more_link


@pytest.mark.nondesstructive
def test_click_article_image(base_url, selenium):
    selenium.get(f'{base_url}/blog/')
    page = BlogHomepage(selenium, base_url).wait_for_page_to_load()
    article_title = page.articles[0].title.text
    page.articles[0].image.click()
    assert (
        article_title.lower()
        in page.find_element(By.CLASS_NAME, 'header-title').text.lower()
    )


@pytest.mark.nondesstructive
def test_click_article_title(base_url, selenium):
    selenium.get(f'{base_url}/blog/')
    page = BlogHomepage(selenium, base_url).wait_for_page_to_load()
    article_title = page.articles[0].title.text
    page.articles[0].title.click()
    assert (
        article_title.lower()
        in page.find_element(By.CLASS_NAME, 'header-title').text.lower()
    )


@pytest.mark.nondesstructive
def test_read_more_link(base_url, selenium):
    selenium.get(f'{base_url}/blog/')
    page = BlogHomepage(selenium, base_url).wait_for_page_to_load()
    article_title = page.articles[0].title.text
    page.articles[0].read_more_link.click()
    assert (
        article_title.lower()
        in page.find_element(By.CLASS_NAME, 'header-title').text.lower()
    )
