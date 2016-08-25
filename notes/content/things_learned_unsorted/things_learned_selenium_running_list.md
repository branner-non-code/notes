## Things learned, Selenium in the version at MediaMath

 1. Use:
 
    ```python
    import selenium.webdriver
    import src.pages.placebo.placebo_main_page as pmp
    import src.pages.placebo.placebo_filters_page as pfp
    import src.pages.placebo.placebo_create_page as pcp
    c = selenium.webdriver.Chrome()
    main_placebo = pmp.PlaceboMainPage(c)
    main_placebo.driver.switch_to.frame(c.find_element_by_id("T1App-placebo"))
    main_placebo.click_add_new_placebo()
    ```
    
 1. To add text use:
 
    ```python
    main_placebo.set_field_value(*(By.CSS, ".some.class#"), "some_text")
    ```
    
    Get classes using right-click and Inspect Element.
    
 1. He recommends: to make things simpler, inspect elements at  https://t1apps-qa.mediamath.com/placebo/index.html#/new after logging in. That seems to mean:

    ```python
    import src.pages.placebo.placebo_main_page as pmp
    url = 'https://t1apps-qa.mediamath.com/placebo/index.html#/new'
    c = selenium.webdriver.Chrome()
    main_placebo = pmp.PlaceboMainPage(c, url)
    main_placebo.open(url)
    ```
    
    This works, after that:

    ```python
    from selenium.webdriver.common.by import By
    main_placebo.set_field_value(By.CSS_SELECTOR, "#search-text", "test of adding test")
    ```
    
    But note that a locator (`By.CSS_SELECTOR, "#search-text"`) would normally come in as a variable, so 
    
    ```python
    main_placebo.set_field_value(*locator, "test of adding test")
    ```

    would be the more usual construction.

 1. Finding and clicking button
 
    ```python
    from selenium.webdriver.common.by import By
    element = main_placebo.find_element(*(By.CSS_SELECTOR, "button#to_new"))
    element.click()
    ```

 1. 
 
    ```python
    import selenium.webdriver
    from importlib import import_module
    import logging
    from src.utils.logger_helper import setup_logging, create_log_directory
    import src.pages.login
    import src.pages.placebo.placebo_create_page as pcp
    import src.pages.placebo.placebo_filters_page as pfp
    import src.pages.placebo.placebo_main_page as pmp

    c = selenium.webdriver.Chrome()
    url = 'https://t1qa2.mediamath.com'

    def process_config_file(request):
        user_config = None
        config_name = request.config.getoption('--config')
        try:
            user_config = import_module(config_name)
            return user_config
        except ImportError:
            error_message = 'No config named {}'.format(config_name)
            raise ImportError(error_message)
    
        except AttributeError:
            error_message = 'Specify a config to use or remove the config flag'
            raise ImportError(error_message)
        
    def valid_login(driver, user_name, pass_word, base_url):
        logger = logging.getLogger(__name__)
        logger.info('Default valid log in with provided username and password')
        login_page = src.pages.login.LoginPage(driver, base_url)
        login_page.open_page()
        return login_page.login_user(user_name, pass_word)
    
    def time_out(request):
        time_out = request.config.getoption("--timeout")
        if not time_out:
            time_out = process_config_file(request).TIMEOUT
        return time_out
    
    logger = logging.getLogger(__name__)
    home_page = valid_login
    home_page.click_module_icon('apps')
    org_name = home_page.return_selected_org()
    assert "ACME Org" in org_name

    
    ```

[end]